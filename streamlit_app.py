
import streamlit as st
import pandas as pd

st.title("📊 FollowCheck - Monitoramento de Seguidores no Instagram")

st.write("1️⃣ Primeiro, faça o download da lista atual de seguidores de um perfil e envie aqui.")
file1 = st.file_uploader("📥 Envie o arquivo CSV da primeira análise", type=["csv"], key="file1")
file2 = st.file_uploader("📥 Envie o arquivo CSV da nova análise", type=["csv"], key="file2")

if file1 and file2:
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Garante que os nomes das colunas sejam consistentes
    col = df1.columns[0]

    seguidores_antes = set(df1[col])
    seguidores_depois = set(df2[col])

    novos = sorted(seguidores_depois - seguidores_antes)
    sairam = sorted(seguidores_antes - seguidores_depois)

    st.subheader("📈 Novos Seguidores")
    st.write(novos if novos else "Nenhum novo seguidor.")

    st.subheader("📉 Deixaram de seguir")
    st.write(sairam if sairam else "Ninguém deixou de seguir.")

    # Botão para baixar os relatórios
    df_novos = pd.DataFrame(novos, columns=["Novos Seguidores"])
    df_sairam = pd.DataFrame(sairam, columns=["Deixaram de Seguir"])

    st.download_button("⬇️ Baixar Novos Seguidores", df_novos.to_csv(index=False), file_name="novos_seguidores.csv")
    st.download_button("⬇️ Baixar Quem Saiu", df_sairam.to_csv(index=False), file_name="seguidores_perdidos.csv")
else:
    st.info("Envie os dois arquivos para comparar as listas de seguidores.")
