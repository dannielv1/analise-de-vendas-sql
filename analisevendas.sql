create database analisevendas;
use analisevendas; 

-- Total de vendas por região
select Regiao, sum(Valor*Quantidade) as TotalFaturamento
from vendascsv
group by Regiao;

-- Produto mais vendido
select Produto, sum(Quantidade) as TotalVendido
from vendascsv
group by Produto
order by TotalVendido desc
limit 5;

-- Clientes mais recorrentes
select ClienteID, count(*) as NumeroCompras
from vendascsv
group by ClienteID
order by NumeroCompras desc;

