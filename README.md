# Speaker Detection System Collections

Mô hình nhận diện người nói (ECAPA-TDNN và SamResNet34) cho bài toán **Speaker Identification**, sử dụng bộ dữ liệu tiếng Việt tự tổng hợp.

## 1. Tạo và kích hoạt môi trường ảo

```bash
conda create -n spk python=3.11.13
conda activate spk
```

## 2. Cài đặt các thư viện cần thiết

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Chạy chương trình huấn luyện

Script dưới đây sẽ:

* Tải bộ dữ liệu
* Chạy file `train.py` để huấn luyện mô hình

```bash
bash run_ECAPA.sh
```