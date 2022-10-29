# Port-scanner
Ferramenta com o objetivo de mapear portas de TCP e UDP

Neste teste ele identifica o status das portas, se estão fechadas ou abertas.

Peguei de um artigo da Cloudflare aonde dizia quais são as portas mais utilizadas atualmente, peguei o número das portas e coloquei elas dentro de uma array.

O IP utilizado no código é de um site aonde seu objetivo é para treinar testes de invasão.

Então criei um 'for' para que todas as portas fossem testadas, se a porta retornar o 'status=0' então ela está aberta ou seja funcionando, caso contrário não. O 'if' compara se o status for igual a 0 ele da um print na tela dizendo que determinada porta esta aberta.