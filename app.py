import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

# .env 読み込み
load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.title("llmアプリ: 専門家に相談Webアプリ")

st.write("##### 動作モード1: ドラえもんの専門家")
st.write("ドラえもんの専門家に質問することで、ドラえもんに関する様々な情報を得ることができます。")
st.write("##### 動作モード2: ポケモンの専門家")
st.write("ポケモンの専門家に質問することで、ポケモンに関する様々な情報を得ることができます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["ドラえもんの専門家", "ポケモンの専門家"]
)

st.divider()

input_text = st.text_input(
    "テキストを入力してください。",
)

if st.button("実行"):
    st.divider()

    if not input_text:
        st.error("テキストを入力してください。")
    else:
        text_count = len(input_text)
        st.write(f"文字数: {text_count}文字")

        # モードに応じて system メッセージを切り替え
        system_message = (
            "あなたはドラえもんに関するアドバイザーです。"
            if selected_item == "ドラえもんの専門家"
            else "あなたはポケモンに関するアドバイザーです。"
        )

        # OpenAI API 呼び出し
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": input_text}
            ],
            temperature=0.5
        )

        st.write(response.choices[0].message.content)