# Qwen-VL Frame Index Demo

This repository demonstrates one of several ideas explored for improving temporal reasoning in multi-frame vision-language models.

The focus here is a lightweight and practical approach called **Text-guided Frame Indexing**, which inserts explicit frame order information into prompts.

## 🚨 Problem

When multiple frames are given to VLMs:

- Video mode → frame merge issue
- Multi-image mode → weak temporal understanding

## 💡 Idea

Insert explicit frame index text between images:

&lt;Frame 1&gt;

&lt;Frame 2&gt;

...

This improves temporal reasoning.

## ⚙️ Environment
```bash
pip install -r requirements.txt -f https://download.pytorch.org/whl/cu128
pip install qwen-vl-utils

# If you want to use flash attention 2
pip install flash-attn --no-build-isolation
```

## 🧪 Demo
Implement [Demo](./demo.ipynb)

## 📊 Observation
Using explicit frame index text:

- Improves temporal consistency
- Reduces frame confusion
- +2% performance gain in our internal experiments

## 🧩 Engineering Decision

Several approaches were explored for improving temporal reasoning:

- Video-mode input
- Multi-image input without guidance
- Text-guided frame indexing (this demo)

Video mode showed frame merging behavior, while plain multi-image input weakened temporal consistency.

This repository focuses on the frame-index approach because it provides a lightweight and practical improvement without modifying model architecture.

## License

This project is built upon **Qwen3-VL**, which is released under the
Apache License, Version 2.0.

Accordingly, this project is also distributed under the
**Apache License, Version 2.0**.

See the [LICENSE](./LICENSE) file for details.