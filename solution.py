import os
import time
from typing import Any, Callable
from openai import OpenAI

COST_PER_1K_OUTPUT_TOKENS = {
    "gpt-4o": 0.010,
    "gpt-4o-mini": 0.0006,
}

OPENAI_MODEL = "gpt-4o"
OPENAI_MINI_MODEL = "gpt-4o-mini"


# ---------------------------------------------------------------------------
# Task 1 — Call GPT-4o
# ---------------------------------------------------------------------------
def call_openai(
    prompt: str,
    model: str = OPENAI_MODEL,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    start_time = time.time()

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    )

    latency = time.time() - start_time
    response_text = response.choices[0].message.content

    return response_text, latency


# ---------------------------------------------------------------------------
# Task 2 — Call GPT-4o-mini
# ---------------------------------------------------------------------------
def call_openai_mini(
    prompt: str,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    return call_openai(
        prompt=prompt,
        model=OPENAI_MINI_MODEL,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    )


# ---------------------------------------------------------------------------
# Task 3 — Compare GPT-4o vs GPT-4o-mini
# ---------------------------------------------------------------------------
def compare_models(prompt: str) -> dict:
    res4o, lat4o = call_openai(prompt)
    res_mini, lat_mini = call_openai_mini(prompt)

    word_count = len(res4o.split())
    estimated_tokens = word_count / 0.75
    cost_estimate = (estimated_tokens / 1000) * COST_PER_1K_OUTPUT_TOKENS["gpt-4o"]

    return {
        "gpt4o_response": res4o,
        "mini_response": res_mini,
        "gpt4o_latency": lat4o,
        "mini_latency": lat_mini,
        "gpt4o_cost_estimate": cost_estimate,
    }


# ---------------------------------------------------------------------------
# Task 4 — Streaming chatbot
# ---------------------------------------------------------------------------
def streaming_chatbot() -> None:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    history = []

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["quit", "exit"]:
            break

        history.append({"role": "user", "content": user_input})

        stream = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=history,
            stream=True,
        )

        print("Assistant: ", end="", flush=True)
        assistant_reply = ""

        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            assistant_reply += delta
            print(delta, end="", flush=True)

        print()

        history.append({"role": "assistant", "content": assistant_reply})

        # giữ 3 turns cuối (1 turn = user + assistant)
        history = history[-6:]


# ---------------------------------------------------------------------------
# Bonus Task A — Retry with exponential backoff
# ---------------------------------------------------------------------------
def retry_with_backoff(
    fn: Callable,
    max_retries: int = 3,
    base_delay: float = 0.1,
) -> Any:
    for attempt in range(max_retries):
        try:
            return fn()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)


# ---------------------------------------------------------------------------
# Bonus Task B — Batch compare
# ---------------------------------------------------------------------------
def batch_compare(prompts: list[str]) -> list[dict]:
    results = []

    for p in prompts:
        res = compare_models(p)
        res["prompt"] = p
        results.append(res)

    return results


# ---------------------------------------------------------------------------
# Bonus Task C — Format comparison table
# ---------------------------------------------------------------------------
def format_comparison_table(results: list[dict]) -> str:
    def truncate(text):
        return text[:40] + "..." if len(text) > 40 else text

    header = f"{'Prompt':<20} | {'GPT-4o Response':<40} | {'Mini Response':<40} | {'4o Lat':<10} | {'Mini Lat':<10}"
    lines = [header, "-" * len(header)]

    for r in results:
        line = (
            f"{truncate(r['prompt']):<20} | "
            f"{truncate(r['gpt4o_response']):<40} | "
            f"{truncate(r['mini_response']):<40} | "
            f"{r['gpt4o_latency']:<10.2f} | "
            f"{r['mini_latency']:<10.2f}"
        )
        lines.append(line)

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    test_prompt = "Explain the difference between temperature and top_p in one sentence."

    print("=== Comparing models ===")
    result = compare_models(test_prompt)
    for key, value in result.items():
        print(f"{key}: {value}")

    print("\n=== Starting chatbot (type 'quit' to exit) ===")
    streaming_chatbot()