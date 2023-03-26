import deepl
import streamlit as st

LANGUEGES = {"英語": "EN", "日本語": "JA", "中国語":"ZH","スペイン語":"ES"}

def deepl_translate(text, src_lang="JA", target_lang="EN"):
    translated_text = deepl.translate(
        source_language=src_lang, target_language=target_lang, text=text
    )
    print(translated_text)
    return translated_text

def main():
    st.title('日本語-英語-中国語-スペイン語')
    main_container = st.container()

    left_col, right_col = main_container.columns(2)

    src_lang = left_col.selectbox(
        "入力テキストの言語",
        options = LANGUEGES
    )
    print(src_lang)
    input_text = left_col.text_area("テキストを入力して下さい", height = 300)


    target_lang = right_col.selectbox(
        "翻訳語のテキストの言語",
        options = LANGUEGES,
    )
    right_col.text_area(
        "翻訳語のテキスト",
        value=deepl_translate(
            input_text, src_lang=LANGUEGES[src_lang], target_lang=LANGUEGES[target_lang]
        ),
        height = 300,
    )


if __name__ == "__main__":
    main()