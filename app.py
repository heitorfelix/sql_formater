import streamlit as st
import sqlparse
import re

# Função para formatar o SQL
def format_sql(sql, reindent_aligned, keyword_case, use_space_around_operators, comma_first, strip_comments):
    sql_formatted = sqlparse.format(
        sql,
        reindent_aligned=reindent_aligned,
        keyword_case=keyword_case,
        use_space_around_operators=use_space_around_operators,
        comma_first=comma_first,
        strip_comments=strip_comments
    )
    return sql_formatted


def put_comma_first(sql):

    formatted_sql = sql.replace(',\n', '\n,')

    matches = re.findall(r', +'  , formatted_sql)
    for match in matches:
        formatted_sql = formatted_sql.replace(match, ' '*(len(match)-1) + ', ')

    return formatted_sql

# Configuração do aplicativo Streamlit
st.title("Formatador SQL")

# Text Area para inserir o SQL
sql_input = st.text_area("Insira o SQL aqui")

# Controles deslizantes e seletores para os parâmetros
reindent_aligned = st.checkbox("Reindent Aligned", value = True)
keyword_case = st.selectbox("Keyword Case", ["upper", "lower"])
use_space_around_operators = st.checkbox("Use Space Around Operators", value = True)
comma_first = st.checkbox("Comma First", value = True)
strip_comments = st.checkbox("Strip Comments", value = False)

# Botão para formatar o SQL
if st.button("Formatar"):
    if sql_input:
        formatted_sql = format_sql(sql_input, reindent_aligned, keyword_case, use_space_around_operators, comma_first, strip_comments)
        st.text("SQL Formatado:")

        if comma_first:
            formatted_sql = put_comma_first(formatted_sql)

        st.code(formatted_sql, language="sql")
    else:
        st.warning("Por favor, insira um SQL para formatar.")


