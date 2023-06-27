def encrypt_decrypt_file(file_name, key, mode):
    # Verifica se a operação é válida
    if mode not in ['encrypt', 'decrypt']:
        print("Operação inválida. Escolha 'encrypt' para criptografar ou 'decrypt' para descriptografar.")
        return
    
    try:
        with open(file_name, 'r') as file:
            data = file.read()

        # Converte os dados e a chave em bytes
        data_bytes = data.encode()
        key_bytes = key.encode()

        # Verifica se a chave é do mesmo tamanho que o conteúdo
        if len(data_bytes) != len(key_bytes):
            print("Erro: Tamanho da chave diferente do tamanho do arquivo.")
            return

        # Realiza a operação de criptografia ou descriptografia
        if mode == 'encrypt':
            result_bytes = bytes([data_byte ^ key_byte for data_byte, key_byte in zip(data_bytes, key_bytes)])
        elif mode == 'decrypt':
            result_bytes = bytes([data_byte ^ key_byte for data_byte, key_byte in zip(data_bytes, key_bytes)])

        # Cria o nome do arquivo criptografado ou descriptografado
        if mode == 'encrypt':
            output_file_name = file_name.replace('.txt', '_cripto.txt')
        elif mode == 'decrypt':
            output_file_name = file_name.replace('_cripto.txt', '_decripto.txt')

        # Escreve o resultado no arquivo de saída
        with open(output_file_name, 'wb') as output_file:
            if mode == 'encrypt':
                output_file.write(result_bytes)
            elif mode == 'decrypt':
                output_file.write(result_bytes.decode())

        print("Operação concluída com sucesso. O arquivo resultante é: " + output_file_name)
    
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except IOError:
        print("Erro ao ler ou escrever no arquivo.")

# Exemplo de uso
file_name = 'arquivo_teste.txt'
key = 'chave_secreta'
mode = 'encrypt'  # Ou 'decrypt' para decriptografar

encrypt_decrypt_file(file_name, key, mode)