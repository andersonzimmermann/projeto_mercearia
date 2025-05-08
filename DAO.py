from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categorias.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')


    @classmethod
    def ler(cls):
        with open('categorias.txt', 'r') as arq:
            cls.categorias = arq.readlines()
        
        cls.categorias = list(map(lambda x: x.replace('\n', ''), cls.categorias))
        cat = []
        for i in cls.categorias:
            cat.append(Categoria(i))
        return cat

DaoCategoria.salvar('teste1')

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + "|" + venda.itensVendido.preco + "|" + venda.itensVendido.categoria + "|" + venda.vendedor + "|" + venda.comprador + "|" + str(venda.quantidadeVendida) + "|" + str(venda.data))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arq:
            cls.vendas = arq.readlines()
        
        cls.vendas = list(map(lambda x: x.replace('\n', ''), cls.vendas))
        cls.vendas = list(map(lambda x: x.split('|'), cls.vendas))
        vend = []
        for i in cls.vendas:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return vend

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|" + produto.preco + "|" + produto.categoria + "|" + str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
        return est

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.telefone + "|" + fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()
        
        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))
        forn = []
        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return forn

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoa.nome + "|" + pessoa.telefone + "|" + pessoa.cpf + "|" + pessoa.email + "|" + pessoa.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()
        
        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))
        
        clientes = []
        for i in cls.clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return clientes

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + "|" + funcionario.nome + "|" + funcionario.telefone + "|" + funcionario.cpf + "|" + funcionario.email + "|" + funcionario.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()
        
        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))
        func = []
        for i in cls.funcionarios:
            func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        return func