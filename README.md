# EDA de Vendas — E-commerce Brasil (2024–2025) com Pandas

Análise exploratória em **Python + Pandas + Matplotlib** usando um dataset **sintético** de e-commerce no Brasil (🎯 ideal para portfólio e posts de divulgação).  
Foco em KPIs, sazonalidade, mix por categoria/canal, meios de pagamento e qualidade de atendimento (NPS/devolução).

> **Resumo rápido**
> - 🧾 **40.000** linhas × **35** colunas  
> - ⏱️ Período: 2024-01 a 2025-08  
> - 📈 KPIs, receita mensal, top produtos/cidades, devolução, desconto × margem, etc.

## 📂 Dados
- `data/ecommerce_brasil_2024_2025.csv` — base principal (sintética)
- `data/dicionario_colunas.csv` — dicionário de dados
- Principais colunas: `data_pedido`, `categoria`, `subcategoria`, `produto`, `canal`, `meio_pagto`, `uf`, `cidade`,  
  `qtd`, `preco_unit`, `desconto_pct`, `frete`, `prazo_entrega_dias`, `receita`, `cogs`, `margem_bruta`,  
  `devolvido`, `avaliacao_1a5`, `nps_0a10`, `recorrente`, `tenure_dias`.

> ⚠️ **Aviso**: A base de dados é gerada com dados ficticios para estudo. Qualquer semelhança com dados reais é coincidência.
