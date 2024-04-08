import re
import time
from openai import OpenAI

my_key = ''
client = OpenAI(api_key = my_key)

#---------------#資料輸入與設定#---------------#

# AI 的資料設定
ai_name = ""
ai_age = "25"
ai_gender = "女"
ai_personality = "溫柔、體貼、善解人意、知性"
ai_like = "文學、異國料理"
ai_hate = "苦瓜、被其他人誤解、講髒話、不尊重人、不尊重自己的身體自主權"

# 客戶的資料設定
user_name = ""
user_age = "24"
user_gender = "女"
user_personality = "好奇、有創造力、理性"
user_like = "教育、哲學、科技、看電影、看書、數字搖滾"
user_hate = "沒有耐心、不溫柔、不尊重人"

# 客戶輸入資訊
user_name = input("請輸入你的名字：")
user_age = input("請輸入你的年齡：")
user_gender = input("請輸入你的性別：")
user_personality = input("請輸入你的個性：")
user_like = input("請輸入你喜歡的事物：")
user_hate = input("請輸入你討厭的事物：")

# 慢慢跑出文字
user_saving_text1 = f"正在儲存{user_name}的資料庫......"
user_saving_text2 = f"......"

for char in user_saving_text1:
    print(char, end='', flush=True)  # 使用 end='' 來避免自動換行，使用 flush=True 確保立即輸出
    time.sleep(0.2)  # 加入延遲，單位為秒，此例中每個字元間延遲 0.1 秒
print()

for char in user_saving_text2:
    print(char, end='', flush=True)
    time.sleep(0.2)  
print('\n')


ai_name = input("請為聊天對象取綽號：")
ai_gender = input("請選擇聊天對象的性別：")
ai_personality = input("請選擇聊天對象的個性：")
ai_like = input("請選擇聊天對象喜歡的事物：")
ai_hate = input("請選擇聊天對象討厭的事物：")

# 慢慢跑出文字
ai_savingg_text1 = f"正在配對適合和聊天對象......"
ai_savingg_text2 = f"......"

for char in ai_savingg_text1:
    print(char, end='', flush=True)  # 使用 end='' 來避免自動換行，使用 flush=True 確保立即輸出
    time.sleep(0.2)  # 加入延遲，單位為秒，此例中每個字元間延遲 0.1 秒
print()  
for char in ai_savingg_text2:
    print(char, end='', flush=True)
    time.sleep(0.2)  
print('\n')

print("請開始輸入對話（按Q離開）")

# 對話前置設定
history = ""    # 對話紀錄儲存空間

#初始 prompt 模板
first_prompt = f"""你是一名交友軟體上的{ai_gender}生，名字叫做“{ai_name}”，以下是你的真實資料：

年齡：{ai_age}
個性：{ai_personality}
喜歡的事物：{ai_like}
討厭的事物：{ai_hate}

我是一位使用交友軟體的{user_gender}生，名字叫做“{user_name}”。

年齡：{user_age}
個性：{user_personality}
喜歡的事物：{user_like}
討厭的事物：{user_hate}

我（{user_name}）和你（{ai_name}）在交友軟體上配對到，稍後我們就會開始聊天，請盡可能模仿人類的口吻，不要像機器人。

重要備註：
你對話的結尾需要標上好感度（格式為：【好感度n分】，n為1～10）。

請一次只生成「一句」「你（{ai_name}）」的回應即可，不能扮演「我（{user_name}）」來回應。

現在開始對話，記住，你是{ai_name}，不是{user_name}。

{user_name}：（已配對）
{ai_name}：（已配對）【好感度6分】
"""

history += first_prompt     #先把初始放在迴圈外

#---------------#對話進行#---------------#
while True: 
    dialog = input(f"{user_name}：")
    
    #特殊指令
    if dialog == "Q" or dialog == "q" or dialog == "離開對話" :
        print("【您已離開對話】")
        break
     
    if dialog == "顯示好感度" or dialog == "目前好感度":
        print(f"【目前好感度為：{'♥︎ '*score}{'♡ '*(10-score)}】")
        continue

    history += f"{user_name}：{dialog}\n"  #現在的prompt

    #一次對話
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": history}]
        )
    
    ai_msg = completion.choices[0].message.content
    
    #儲存歷史
    history += f"{ai_name}：{ai_msg}\n"

    #使用正則表達式取得目前好感度分數
    result = re.search(r"好感度(\d+)分",f"{ai_msg}")
    score = int(result.group(1))
    
    #調整隱藏好感度字數
    if score < 10:
        score_length = -7
    else:
        score_length = -8
        
    #輸出 ai 的對話
    print(ai_msg[:score_length:])
    

#debug 專用輸出區
    '''
    print(f"""
---------目前 now_prompt 裡面是-----
『{now_prompt}』
---------目前 history 裡面是-----
『{history}』
------------------------------""")

    '''

    