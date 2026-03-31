#!/usr/bin/env python3
"""MiniMax speech-2.8-hd TTS voice reply script."""
import sys, os, requests

# Default API Key (user should replace with their own)
DEFAULT_API_KEY = "Your API"
API_URL = "https://api.minimaxi.com/v1/t2a_v2"

def speak(text, voice_id="female-shaonv", speed=1.0, vol=1.0, pitch=0,
          out_path=None, api_key=None, play=True):
    """Generate TTS audio and optionally play it.
    
    Args:
        text: Text to synthesize
        voice_id: Voice ID from MiniMax voice list (default: female-shaonv)
        speed: Speech speed 0.5-2.0 (default: 1.0)
        vol: Volume 0-2.0 (default: 1.0)
        pitch: Pitch -12 to 12 (default: 0)
        out_path: Output file path (default: /tmp/tts_output.mp3)
        api_key: MiniMax API key (default: env MINIMAX_API_KEY or built-in key)
        play: Whether to play audio with afplay (default: True)
    """
    if not text or not text.strip():
        print("ERROR: text is empty", file=sys.stderr)
        return None

    if out_path is None:
        out_path = "/tmp/tts_output.mp3"

    if api_key is None:
        api_key = os.environ.get("MINIMAX_API_KEY", DEFAULT_API_KEY)

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "speech-2.8-hd",
        "text": text,
        "stream": False,
        "voice_setting": {
            "voice_id": voice_id,
            "speed": speed,
            "vol": vol,
            "pitch": pitch
        },
        "audio_setting": {
            "sample_rate": 32000,
            "bitrate": 128000,
            "format": "mp3"
        }
    }

    try:
        r = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        r.raise_for_status()
        data = r.json()
        audio_hex = data.get("data", {}).get("audio", "")
        if not audio_hex:
            err = data.get("base_resp", {}).get("status_msg", "unknown error")
            print(f"ERROR: API returned no audio - {err}", file=sys.stderr)
            return None
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Request failed - {e}", file=sys.stderr)
        return None

    audio_bytes = bytes.fromhex(audio_hex)
    with open(out_path, "wb") as f:
        f.write(audio_bytes)

    print(f"OK: {out_path} ({len(audio_bytes)} bytes)")

    if play and os.path.exists("/usr/bin/afplay"):
        os.system(f"/usr/bin/afplay {out_path} &")

    return out_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} '文字内容' [output.mp3] [voice_id]")
        print(f"Default voice: female-shaonv")
        sys.exit(1)

    text = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else "/tmp/tts_output.mp3"
    voice_id = sys.argv[3] if len(sys.argv) > 3 else "female-shaonv"

    result = speak(text, voice_id=voice_id, out_path=out_path)
    if result is None:
        sys.exit(1)
