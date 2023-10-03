import streamlit as st
import pandas as pd


def main():
    st.header("Compare the different options for choosing the best clusters")

    st.number_input("number of clusters", min_value=1, max_value=15, step=1, key="num_clusters")

    if 'df' not in st.session_state:
        st.session_state['df'] = pd.read_csv("meta_filtered.csv")

    df = st.session_state['df']

    clusters_by_doc_coverage = df[df["rank"] <= st.session_state["num_clusters"]]["representative"].unique()
    # str_by_doc_cover = ("\n".join(clusters_by_doc_coverage))

    clusters_by_corpus_coverage = df[df[f"best_{st.session_state['num_clusters']}_corpus"] == True]["representative"].unique()
    # str_by_corpus_cover = ("\n".join(clusters_by_corpus_coverage))

    clusters_by_combined_coverage = df[df[f"best_{st.session_state['num_clusters']}_combined"] == True]["representative"].unique()
    # str_by_combined_cover = ("\n".join(clusters_by_combined_coverage))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("By document coverage")
        st.write(clusters_by_doc_coverage)

    with col2:
        st.subheader("By corpus coverage")
        st.write(clusters_by_corpus_coverage)

    with col3:
        st.subheader("Combined coverage")
        st.write(clusters_by_combined_coverage)


if __name__ == '__main__':
    main()
