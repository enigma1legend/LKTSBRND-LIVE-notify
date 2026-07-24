import asyncio
import json
import os
from pathlib import Path

import requests
from TikTokLive import TikTokLiveClient

STATE_FILE = Path(__file__).parent / "state.json"
TIKTOK_USERNAME = os.environ["TIKTOK_USERNAME"]
NTFY_TOPIC = os.environ["NTFY_TOPIC"]


def load_previous_state() -> bool:
    if not STATE_FILE.exists():
        return False
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8")).get("is_live", False)
    except (json.JSONDecodeError, OSError):
        return False


def save_state(is_live: bool) -> None:
    STATE_FILE.write_text(json.dumps({"is_live": is_live}), encoding="utf-8")


def notify_live() -> None:
    message = (
        f"{TIKTOK_USERNAME} élőben van a TikTokon! "
        f"https://www.tiktok.com/@{TIKTOK_USERNAME}/live"
    )
    requests.post(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=message.encode("utf-8"),
        headers={
            "Title": "TikTok LIVE ertesites",
            "Priority": "high",
            "Tags": "tiktok,red_circle",
        },
        timeout=15,
    )


async def check_is_live() -> bool:
    client = TikTokLiveClient(unique_id=f"@{TIKTOK_USERNAME}")
    return await client.is_live()


def main() -> None:
    was_live = load_previous_state()

    try:
        is_live = asyncio.run(check_is_live())
    except Exception as exc:
        print(f"Hiba a TikTok statusz lekerdezesekor: {exc}")
        return

    print(f"{TIKTOK_USERNAME} elo statusz: {is_live}")

    if is_live and not was_live:
        print("Uj elo adas eszlelve, ertesites kuldese...")
        notify_live()

    save_state(is_live)


if __name__ == "__main__":
    main()
