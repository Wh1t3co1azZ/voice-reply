# Voice Reply

MiniMax speech-2.8-hd TTS voice reply skill for AI assistants. Generate speech audio and play via macOS `afplay`.

## Install

```bash
git clone https://github.com/Wh1t3co1azZ/voice-reply.git
cd voice-reply
pip3 install requests --user
```

## Configure

Edit `voice_reply.py`, replace `DEFAULT_API_KEY`:

```python
DEFAULT_API_KEY = "your-minimax-api-key-here"
```

Get API key: https://platform.minimaxi.com/

## Use

```bash
# Basic
python3 voice_reply.py "你好" /tmp/test.mp3

# Specify voice
python3 voice_reply.py "你好" /tmp/test.mp3 female-yujie

# Voice + speed
python3 voice_reply.py "快速播报" /tmp/test.mp3 male-qn-badao 1.5
```

## Voice List

40+ Chinese voices available. Full list: https://platform.minimaxi.com/docs/faq/system-voice-id

Common voices: `female-shaonv` (少女), `female-yujie` (御姐), `male-qn-badao` (霸道), `male-qn-jingying` (精英)

## License

MIT
