from src.services.service_usuario import ServiceUsuario


class TestServiceUsuario:
    def setup(self):
        self.service = ServiceUsuario()
        self.nome_valido = "Bruno"
        self.nome_int = 1
        self.nome_none = None
        self.profissao_valida = "QA"
        self.profissao_int = 1
        self.profissao_none = None
        self.ID_valido = 1
        self.ID_inexistente = 999
        self.ID_invalido = "1"
        self.ID_none = None
        self.store_vazio = []

    def test_add_usuario_valido(self):
        resultado_esperado = "Usuário adicionado"
        result = self.service.add_usuario(self.nome_valido, self.profissao_valida)
        assert (result == resultado_esperado)
        assert (self.service.store.bd[0].nome == self.nome_valido)
        assert (self.service.store.bd[0].profissao == self.profissao_valida)

    def test_add_usuario_nome_valido_profissao_invalida(self):
        resultado_esperado ="Usuário inválido"
        result = self.service.add_usuario(self.nome_valido, self.profissao_int)
        assert (result == resultado_esperado)
        assert (self.service.store.bd == self.store_vazio)

    def test_add_usuario_nome_invalida_profissao_valido(self):
        resultado_esperado = "Usuário inválido"
        result = self.service.add_usuario(self.nome_int, self.profissao_valida)
        assert (result == resultado_esperado)
        assert (self.service.store.bd == self.store_vazio)

    def test_add_usuario_nome_valido_profissao_none(self):
        resultado_esperado = "Usuário inválido"
        result = self.service.add_usuario(self.nome_valido, self.profissao_none)
        assert (result == resultado_esperado)
        assert (self.service.store.bd == self.store_vazio)

    def test_add_usuario_nome_nome_profissao_valido(self):
        resultado_esperado = "Usuário inválido"
        result = self.service.add_usuario(self.nome_none, self.profissao_valida)
        assert (result == resultado_esperado)
        assert (self.service.store.bd == self.store_vazio)

    def test_list_usuarios_valido(self):
        self.service.add_usuario(self.nome_valido, self.profissao_valida)
        result = self.service.list_usuarios()
        assert (len(result) > 0)

    def test_list_usuario_id_valido(self):
        resultado_esperado = "ID: {} | Nome: {} | Profissão: {}".format(1, self.nome_valido, self.profissao_valida)
        self.service.add_usuario(self.nome_valido, self.profissao_valida)
        result = self.service.list_usuarios_id(self.ID_valido)
        assert (len(result) > 0)
        assert (result == resultado_esperado)

    def test_list_usuario_id_inexistente(self):
        resultado_esperado = "ID inválido"
        self.service.add_usuario(self.nome_valido, self.profissao_valida)
        result = self.service.list_usuarios_id(self.ID_inexistente)
        assert (result == resultado_esperado)

    def test_list_usuario_id_invalido(self):
        resultado_esperado = "ID inválido"
        self.service.add_usuario(self.nome_valido, self.profissao_valida)
        result = self.service.list_usuarios_id(self.ID_invalido)
        assert (result == resultado_esperado)

    def test_list_usuario_id_none(self):
        resultado_esperado = "ID inválido"
        self.service.add_usuario(self.nome_valido, self.profissao_valida)
        result = self.service.list_usuarios_id(self.ID_none)
        assert (result == resultado_esperado)

    def test_remover_usuario(self):
        resultado_esperado = "Usuário excluído com sucesso"
        cadastrado = self.service.add_usuario(self.nome_valido, self.profissao_valida)
        result = self.service.remove_usuario_id(self.ID_valido)
        assert (result == resultado_esperado)
        assert (self.service.store.bd == self.store_vazio)

    def test_remover_usuario_ID_inexistente(self):
        resultado_esperado = "Usuário não encontrado"
        cadastrado = self.service.add_usuario(self.nome_valido, self.profissao_valida)
        result = self.service.remove_usuario_id(self.ID_inexistente)
        assert (result == resultado_esperado)
        assert (self.service.store.bd > self.store_vazio)

    def test_remover_usuario_ID_none(self):
        resultado_esperado = "ID inválido"
        cadastrado = self.service.add_usuario(self.nome_valido, self.profissao_valida)
        result = self.service.remove_usuario_id(self.ID_none)
        assert (result == resultado_esperado)
        assert (self.service.store.bd > self.store_vazio)

    def test_remover_usuario_ID_string(self):
        resultado_esperado = "ID inválido"
        cadastrado = self.service.add_usuario(self.nome_valido, self.profissao_valida)
        result = self.service.remove_usuario_id(self.ID_invalido)
        assert (result == resultado_esperado)
        assert (self.service.store.bd > self.store_vazio)

    # TODO Criar testes para as funções em service_usuario
    # Falta completar os testes para atualizar usuario