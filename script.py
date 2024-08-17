from datetime import datetime  # これをインポートします
import os

output_directory = "/Users/fukabooboo/kohya_ss/outputs/"
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y%m%d-%H%M%S")
tmpfilename = os.path.join(output_directory, f"config_lora-{formatted_datetime}.toml")

print(tmpfilename)  # 生成されたファイル名を確認するためのコード
