from src.services.service_usuario import ServiceUsuario


class TestServiceUsuario:
    def setup(self):
        self.service = ServiceUsuario()
        self.nome_valido = "Bruno"
        self.nome_invalido = 1
        self.nome_none = None
        self.profissao_valida = "QA"
        self.profissao_invalida = 1
        self.profissao_none = None

    def test_add_usuario_valido(self):
        resultado_esperado = "Usuário adicionado"
        result = self.service.add_usuario(self.nome_valido, self.profissao_valida)
        assert (result == resultado_esperado)
        assert (self.service.store.bd[0].nome == self.nome_valido)
        assert (self.service.store.bd[0].profissao == self.profissao_valida)

    def test_add_usuario_nome_valido_profissao_invalida(self):
        resultado_esperado ="Usuário inválido"
        store_esperado = []
        result = self.service.add_usuario(self.nome_valido, self.profissao_invalida)
        assert (result == resultado_esperado)
        assert (self.service.store.bd == store_esperado)

    def test_add_usuario_nome_invalida_profissao_valido(self):
        resultado_esperado = "Usuário inválido"
        store_esperado = []
        result = self.service.add_usuario(self.nome_invalido, self.profissao_valida)
        assert (result == resultado_esperado)
        assert (self.service.store.bd == store_esperado)

    def test_add_usuario_nome_valido_profissao_none(self):
        resultado_esperado = "Usuário inválido"
        store_esperado = []
        result = self.service.add_usuario(self.nome_valido, self.profissao_none)
        assert (result == resultado_esperado)
        assert (self.service.store.bd == store_esperado)

    def test_add_usuario_nome_nome_profissao_valido(self):
        resultado_esperado = "Usuário inválido"
        store_esperado = []
        result = self.service.add_usuario(self.nome_none, self.profissao_valida)
        assert (result == resultado_esperado)
        assert (self.service.store.bd == store_esperado)

#TODO Criar mais testes para as funções em service_usuario
    def test_remover_usuario(self):
        resultado_esperado = "Usuário {} removido".format(self.nome_valido)
        cadastrado = self.service.add_usuario(self.nome_valido, self.profissao_valida)
        result = self.service.remove_usuario_id(1)
        assert (result == resultado_esperado)
