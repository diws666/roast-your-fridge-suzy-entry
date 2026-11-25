# Verified count: 105 characters (UTF-8 bytes identical, no trailing newline).
LINE = "My fridge just sent me a push notification: 'You opened me four times and took nothing. We need to talk.'"

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE))
