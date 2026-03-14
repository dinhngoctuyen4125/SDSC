## 1. Add and activate venv

```bash
conda create -n prod python=3.11.13
conda activate prod
```

## 2. Install dependencies

```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Run training

```bash
bash run_ECAPA.sh
```