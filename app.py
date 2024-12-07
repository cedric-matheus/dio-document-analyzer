import streamlit as st

def configure_interface():
    st.title('Upload de Arquivos - DIO - Document Analyzer')
    uploadade_file = st.file_uploader("Escolha um arquivo", type=['png', 'jpg', 'jpeg'])

    if uploadade_file is not None:
        file_name = uploadade_file.name
        # Enviar para o Azure Storage
        blob_url = ''
        if blob_url:
            st.write(f'Arquivo {file_name} enviado com sucesso para o Azure Storage')
        else:
            st.write(f'Erro ao enviar o arquivo {file_name} para o Azure Storage')

if __name__ == '__main__':
    configure_interface()