#!/usr/bin/env python3
"""
Scan the `video/` directory and write `video/videos.json` containing
an array of objects: { name: <filename>, url: <relative-url> }

Run from repository root (where this script is at scripts/):
  python3 scripts/generate_videolist.py

This writes `video/videos.json` which the frontend fetches.
"""
import os
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent
VIDEO_DIR = PROJECT_ROOT / 'video'
OUT_FILE = VIDEO_DIR / 'videos.json'

ALLOWED_EXTS = {'.mp4', '.webm', '.ogg', '.mov', '.m4v'}

def main():
    if not VIDEO_DIR.exists() or not VIDEO_DIR.is_dir():
        print(f"video ディレクトリが見つかりません: {VIDEO_DIR}")
        return

    items = []
    for p in sorted(VIDEO_DIR.iterdir()):
        if p.is_file() and p.suffix.lower() in ALLOWED_EXTS:
            items.append({
                'name': p.name,
                'url': f"video/{p.name}"
            })

    OUT_FILE.write_text(json.dumps(items, ensure_ascii=False, indent=2))
    print(f"書き出しました: {OUT_FILE} ({len(items)} 件)")

if __name__ == '__main__':
    main()
