import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv(
    "ecommerce_brasil_2024_2025.csv",
    encoding='utf-8-sig',
    parse_dates=["data_pedido"],
    low_memory=False
)

print(df.shape)
print(df.dtypes.head())
print(df.head(3))

kpis = {
    "faturamento_total": df["receita"].sum(),
    "pedidos": len(df),
    "ticket_medio": df["receita"].mean(),
    "margem_bruta_total": df["margem_bruta"].sum(),
    "% devolução": df["devolvido"].mean()*100,
    "NPS_médio": df["nps_0a10"].mean()
}
print({k:round(v, 2) for k, v in kpis.items()})

mensal = (df
        .assign(mes=df['data_pedido'].dt.to_period('M').dt.to_timestamp())
        .groupby('mes', as_index=False)["receita"].sum()
)

top_cat = (df.groupby("categoria", as_index=False)["receita"].sum()
           .sort_values("receita", ascending=False))

print(mensal.head())
print(top_cat.head())

df["mes"] = df["data_pedido"].dt.to_period("M").dt.to_timestamp()

mensal = df.groupby("mes", as_index=False)["receita"].sum()
plt.figure(figsize=(9,4))
plt.plot(mensal["mes"], mensal["receita"])
plt.title("Receita mensal (R$)")
plt.xlabel("Mês"); plt.ylabel("Receita")
plt.tight_layout(); plt.show()

by_cat = (df.groupby("categoria", as_index=False)["receita"].sum()
            .sort_values("receita", ascending=False).head(8))
plt.figure(figsize=(9,4))
plt.bar(by_cat["categoria"], by_cat["receita"])
plt.title("Receita por categoria (top 8)")
plt.xlabel("Categoria"); plt.ylabel("Receita")
plt.xticks(rotation=30, ha="right")
plt.tight_layout(); plt.show()

plt.figure(figsize=(9,4))
plt.scatter(df["desconto_pct"], df["margem_bruta"], alpha=0.5)
plt.title("Desconto (%) x Margem Bruta (R$)")
plt.xlabel("Desconto (%)"); plt.ylabel("Margem Bruta (R$)")
plt.tight_layout(); plt.show()
