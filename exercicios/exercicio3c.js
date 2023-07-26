function soma(valor1, valor2) {
  return valor1 + valor2;
}

function comissao(vendas) {
  if (vendas > 5000) {
    return vendas * 1.2;
  } else if (vendas > 1000) {
    return vendas * 1.1;
  } else {
    return vendas;
  }
}

function calculoComissao() {
  vendasProdutos = 1200;
  vendasServicos = 500;
  vendasAssessorios = 300;
  totalVendas = soma(vendasProdutos, vendasServicos) + vendasAssessorios;

  return comissao(totalVendas);
}

console.log(calculoComissao());
