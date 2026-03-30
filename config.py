"""スリープ＆マインドLab - ブログ固有設定

睡眠の質とメンタルヘルスを科学する。エビデンスベースの改善法を発信。
YMYL対策: エビデンス重視・出典明記・断定表現回避・医師相談推奨
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "スリープ＆マインドLab"
BLOG_DESCRIPTION = "睡眠の質とメンタルヘルスを科学する。エビデンスベースの改善法・サプリ・ガジェットを徹底レビュー"
BLOG_URL = "https://musclelove-777.github.io/sleep-mental-lab"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/sleep-mental-lab"

# ブログカテゴリ
TARGET_CATEGORIES = [
    "睡眠の質改善",
    "不眠症対策",
    "睡眠ガジェット・グッズ",
    "メンタルヘルス基礎",
    "ストレスマネジメント",
    "マインドフルネス・瞑想",
    "サプリ・栄養",
    "仕事×メンタル",
]

# テーマカラー: 深い紺〜紫系（夜・安眠イメージ）
THEME = {
    "primary": "#1a1a4e",
    "accent": "#6366f1",
    "gradient_start": "#1a1a4e",
    "gradient_end": "#312e81",
    "dark_bg": "#0f0f2e",
    "dark_surface": "#1e1b4b",
    "light_bg": "#f0f0ff",
    "light_surface": "#ffffff",
}

# 記事生成設定
MAX_ARTICLE_LENGTH = 3000
ARTICLES_PER_DAY = 3
SCHEDULE_HOURS = [7, 12, 19]

# Gemini API設定
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

# SEO最適化設定
ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 70
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

# アフィリエイトリンク設定
AFFILIATE_LINKS = {
    "睡眠サプリ": [
        {
            "service": "Amazon 睡眠サプリ",
            "url": "https://www.amazon.co.jp/s?k=%E7%9D%A1%E7%9C%A0+%E3%82%B5%E3%83%97%E3%83%AA",
            "description": "グリシン・GABA・テアニンなど睡眠サプリが豊富",
        },
        {
            "service": "楽天 睡眠サプリ",
            "url": "https://search.rakuten.co.jp/search/mall/%E7%9D%A1%E7%9C%A0+%E3%82%B5%E3%83%97%E3%83%AA/",
            "description": "ポイント還元でお得に睡眠サプリを購入",
        },
    ],
    "睡眠ガジェット": [
        {
            "service": "Oura Ring",
            "url": "https://www.amazon.co.jp/s?k=Oura+Ring",
            "description": "睡眠スコアを自動計測するスマートリング",
        },
        {
            "service": "スマートウォッチ 睡眠計測",
            "url": "https://www.amazon.co.jp/s?k=%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%82%A6%E3%82%A9%E3%83%83%E3%83%81+%E7%9D%A1%E7%9C%A0",
            "description": "睡眠トラッキング機能付きスマートウォッチ",
        },
    ],
    "枕・マットレス": [
        {
            "service": "Amazon 枕・マットレス",
            "url": "https://www.amazon.co.jp/s?k=%E6%9E%95+%E5%AE%89%E7%9C%A0",
            "description": "快眠枕・マットレスの人気ランキング",
        },
    ],
    "メンタルヘルスアプリ": [
        {
            "service": "メンタルヘルスアプリ",
            "url": "https://www.amazon.co.jp/s?k=%E3%83%9E%E3%82%A4%E3%83%B3%E3%83%89%E3%83%95%E3%83%AB%E3%83%8D%E3%82%B9+%E6%9C%AC",
            "description": "瞑想・マインドフルネス関連アプリ・書籍",
        },
    ],
    "書籍": [
        {
            "service": "Amazon 睡眠・メンタルヘルス書籍",
            "url": "https://www.amazon.co.jp/s?k=%E7%9D%A1%E7%9C%A0+%E3%83%A1%E3%83%B3%E3%82%BF%E3%83%AB%E3%83%98%E3%83%AB%E3%82%B9+%E6%9C%AC",
            "description": "睡眠科学・メンタルヘルスの良書を厳選",
        },
        {
            "service": "楽天ブックス",
            "url": "https://books.rakuten.co.jp/search?sitem=%E7%9D%A1%E7%9C%A0+%E3%83%A1%E3%83%B3%E3%82%BF%E3%83%AB",
            "description": "睡眠・メンタルヘルス関連書籍をポイントで",
        },
    ],
}
AFFILIATE_TAG = "musclelove07-22"

# AdSense設定
ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")

# ダッシュボードポート
DASHBOARD_PORT = 8099

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
