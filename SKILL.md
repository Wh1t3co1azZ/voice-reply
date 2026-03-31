---
name: voice-reply
description: MiniMax speech-2.8-hd TTS voice reply skill. Use when generating speech audio after text replies and playing via macOS afplay. Triggers on voice broadcast, text-to-speech, audio playback requests. Supports 40 Chinese voice IDs (female-shaonv, male-qn-badao, etc.), configurable speed/pitch/vol. Requires requests library and macOS afplay.
---

# Voice Reply

MiniMax speech-2.8-hd TTS voice reply skill. Generate and play speech audio via `afplay`.

## When to Use

- User asks for voice broadcast / TTS / 语音播报
- Generate speech from text and play automatically
- Voice reply after AI assistant text response

## Usage

### Command Line

```bash
python3 voice_reply.py "文字内容" /tmp/output.mp3
python3 voice_reply.py "你好" /tmp/test.mp3 female-yujie  # 指定音色
python3 voice_reply.py "快速" /tmp/test.mp3 male-qn-badao 1.5  # 音色+语速
```

### Python API

```python
from voice_reply import speak
speak("义父好，这是一条语音播报。")
speak("你好", voice_id="female-yujie")
```

## Voice IDs

See full list: https://platform.minimaxi.com/docs/faq/system-voice-id

Common: `female-shaonv` (默认少女), `female-yujie` (御姐), `male-qn-badao` (霸道), `male-qn-jingying` (精英)

## Parameters

| Param | Default | Range |
|-------|---------|-------|
| voice_id | female-shaonv | 40+ voices |
| speed | 1.0 | 0.5–2.0 |
| vol | 1.0 | 0–2.0 |
| pitch | 0 | -12–12 |

## Setup

1. `pip3 install requests --user`
2. Edit `voice_reply.py` → replace `DEFAULT_API_KEY` with your key
3. Get API key: https://platform.minimaxi.com/

## Troubleshooting

| Issue | Solution |
|-------|---------|
| Connection refused | Try proxy or check network |
| Token error | Check API key is valid |
| No audio | Verify afplay exists on macOS |
