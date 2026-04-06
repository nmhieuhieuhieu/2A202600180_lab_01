# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> *Khi temperature tăng từ 0.0 lên 1.5, câu trả lời chuyển từ ngắn gọn sang gen nhiều hơn và ngẫu hứng. Ở mức 0.0, mô hình luôn chọn từ có xác suất cao nhất nên câu trả lời gần như không đổi nếu hỏi lại; ở mức 1.5, văn phong trở nên dài dòng, có thể xuất hiện các từ lạ*

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> *Em sẽ đặt temperature thấp, khoảng 0.0 đến 0.3. Lý do là chatbot hỗ trợ khách hàng cần sự chính xác, và độ tin cậy cao, tránh lan man, không đúng trọng tâm.*

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> *khoảng 16.6 lần*

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> *GPT-4o phù hợp khi cần thực hiện các tác vụ suy luận phức tạp, phân tích hoặc xử lý các tác vụ khó. Còn GPT-4o-mini tốt hơn cho các tác vụ đơn giản như phân loại, làm chatbot hội thoại thông thường.*

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> *Streaming rất hữu ích trong các chatbot tương tác trực tiếp, nhất là khi câu trả lời dài. Thay vì bắt người dùng chờ vài giây nhìn màn hình trống, việc hiển thị nội dung từng chút một giúp họ cảm thấy phản hồi đến nhanh hơn và tự nhiên hơn, như thể hệ thống đang suy nghĩ và trả lời ngay lập tức. Ngược lại, non-streaming phù hợp với những tác vụ chạy ngầm như xử lý dữ liệu hàng loạt hoặc trích xuất thông tin để lưu vào database. Trong những trường hợp này, hệ thống chỉ cần kết quả cuối cùng đầy đủ để tiếp tục xử lý, nên không cần hiển thị từng phần cho người dùng.*


## Danh Sách Kiểm Tra Nộp Bài
- [ ] Tất cả tests pass: `pytest tests/ -v`
- [ ] `call_openai` đã triển khai và kiểm thử
- [ ] `call_openai_mini` đã triển khai và kiểm thử
- [ ] `compare_models` đã triển khai và kiểm thử
- [ ] `streaming_chatbot` đã triển khai và kiểm thử
- [ ] `retry_with_backoff` đã triển khai và kiểm thử
- [ ] `batch_compare` đã triển khai và kiểm thử
- [ ] `format_comparison_table` đã triển khai và kiểm thử
- [ ] `exercises.md` đã điền đầy đủ
- [ ] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
