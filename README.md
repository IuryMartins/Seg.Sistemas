# Seg.Sistemas
 Neste código é implementado a cifra de Vernam que realiza uma operação XOR bit a bit para criptografar um arquivo de texto.
 A função encrypt_decrypt_file recebe três parâmetros: 
 file_name (nome do arquivo), 
 key (chave para criptografia/descriptografia) e mode (modo de operação, que pode ser 'encrypt' ou 'decrypt').
A função começa verificando se o modo fornecido é válido, ou seja, se é 'encrypt' ou 'decrypt'. 
Se o modo não for válido, exibe uma mensagem de erro e retorna.
Em seguida, o código tenta abrir o arquivo especificado em modo de leitura ('r') usando um bloco with. 
Se o arquivo não for encontrado, captura a exceção FileNotFoundError e exibe uma mensagem de erro.
Dentro do bloco with, o conteúdo do arquivo é lido e armazenado na variável data.
O código converte tanto o conteúdo do arquivo (data) quanto a chave fornecida (key) em bytes usando o método encode(). 
Isso é necessário para que possamos realizar a operação de criptografia/descriptografia em nível de bytes.
Em seguida, o código verifica se o tamanho dos bytes do conteúdo e da chave é igual. 
Se os tamanhos forem diferentes, isso significa que a chave não tem o tamanho adequado para criptografar/descriptografar o arquivo corretamente. 
Nesse caso, uma mensagem de erro é exibida e a função retorna.
Dependendo do modo fornecido ('encrypt' ou 'decrypt'), o código realiza a operação de criptografia ou descriptografia. 
Ele faz isso aplicando uma operação XOR bitwise entre cada byte do conteúdo e o byte correspondente da chave, usando uma compreensão de lista. 
O resultado é armazenado na variável result_bytes.
Em seguida, o código cria o nome do arquivo de saída, com base no nome do arquivo original e no modo de operação. 
Se o modo for 'encrypt', adiciona '_cripto.txt' ao nome original do arquivo. 
Se o modo for 'decrypt', substitui '_cripto.txt' por '_decripto.txt' no nome original do arquivo.
Escreve o resultado no arquivo de saída. 
O código abre o arquivo de saída no modo de escrita binária ('wb') usando um bloco with. 
No caso de criptografia ('encrypt'), ele grava os bytes resultantes diretamente no arquivo usando o método write(). 
No caso de descriptografia ('decrypt'), antes de gravar no arquivo, os bytes são convertidos de volta para texto usando o método decode().
Por fim, o código exibe uma mensagem de conclusão bem-sucedida, junto com o nome do arquivo de saída.

O exemplo de uso fornecido chama a função encrypt_decrypt_file com o nome do arquivo 'arquivo_teste.txt', uma chave 'chave_secreta' e o modo 'encrypt' para criptografar o arquivo. 
Esse exemplo pode ser personalizado para testar diferentes arquivos, chaves e modos de operação.
Lembre-se de substituir 'nome_arquivo.txt' pelo nome do arquivo de entrada desejado e 'chave_secreta' pela chave de criptografia apropriada.

Após a execução do script, você terá um arquivo de saída criptografado ou decriptografado com o sufixo "_crypto.txt". 
