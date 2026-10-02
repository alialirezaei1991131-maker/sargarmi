"""ابزار مشترک ساخت نسخهٔ فارسی هر برنامه از نسخهٔ انگلیسی با جایگزینی متن."""
import os
import sys

# مسیرها نسبت به ریشهٔ مخزن‌اند، از هر جا که اجرا شود
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def build(src, dst, pairs):
    s = open(src, encoding='utf-8').read()
    missing = []
    for en, fa in pairs:
        if en not in s:
            missing.append(en)
            continue
        s = s.replace(en, fa)
    if missing:
        print('NOT FOUND in', src)
        for m in missing:
            print('  ', m[:100])
        sys.exit(1)
    open(dst, 'w', encoding='utf-8').write(s)
    print('wrote', dst)
