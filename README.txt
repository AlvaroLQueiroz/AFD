A leitura da maquina é realizada atraves de um arquivo. Este aquivo deve seguir o seguinte padrão:

<primeira linha deve conter os estados devidamente separados por virgula(Não importa se é numero, letra ou palavra).>
<segunda linha deve conter as letras do alfabeto devidamente separadas por virgula(Não importa se é numero, letra ou palavra).
<terceira linha deve conter a matriz de transição com as linhas separadas por ;(ponto e virgula) e as colunas separadas por ,(virgula)>
<quarta linha deve conter o estado inicial>
<quinta linha deve conter o(s) estado(s) de aceitação(quanto existir mais de um estado final, estes devem ser separados por virgula).>

Exemplo:

A, b, 1, estado1 														
0, 1, A, letra1  														
A, 1, b, estado1; estado1, b, 1, A; b, 1, estado1, A; estado1, 1, b, a
estado1
b, 1