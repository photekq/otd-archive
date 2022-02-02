import json

raw_html = "[책상/인증] 투표합시다"

json_html = json.dumps(raw_html)
print(json_html)