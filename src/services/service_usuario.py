from src.models.store import Store
from src.models.usuario import Usuario


class ServiceUsuario:
    def __init__(self):
        self.store = Store()

    def add_usuario(self, nome, profissao):
        if nome is not None and profissao is not None:
            if type(nome) is str and type(profissao) is str:
                usuario = Usuario(nome, profissao)
                self.store.bd.append(usuario)
                return "Usuário adicionado"
            else:
                return "Usuário inválido"
        else:
            return "Usuário inválido"

    def list_usuarios(self):
        lista_usuario = []
        for i in range(len(self.store.bd)):
            lista_usuario.append("ID: {} | Nome: {} | Profissão: {}".format(i + 1, self.store.bd[i].nome, self.store.bd[i].profissao))
        return lista_usuario

    def list_usuarios_id(self, id_usuario):
        if id_usuario is not None:
            if type(id_usuario) is int:
                if id_usuario-1 <= len(self.store.bd):
                    return "ID: {} | Nome: {} | Profissão: {}".format(id_usuario, self.store.bd[id_usuario-1].nome, self.store.bd[id_usuario-1].profissao)
                else:
                    return "ID inválido"
            else:
                return "ID inválido"
        else:
            return "ID inválido"

    def remove_usuario_id(self, id_usuario):
        if id_usuario is not None and type(id_usuario) is int:
            for i in range(len(self.store.bd)):
                if len(self.store.bd) > id_usuario-1:
                    self.store.bd.pop(i)
                    return "Usuário excluído com sucesso"
                else:
                    return "Usuário não encontrado"
        else:
            return "ID inválido"

    def update_usuario_nome(self, id_usuario, nome_novo):
        if nome_novo is not None:
            if type(nome_novo) is str:
                self.store.bd[id_usuario].nome = nome_novo
                return "Usuário atualizado"
            else:
                return "Nome inválido"
        else:
            return "Nome inválido"

    def update_usuario_profissao(self, id_usuario, profissao_novo):
        if profissao_novo is not None:
            if type(profissao_novo) is str:
                self.store.bd[id_usuario].profissao = profissao_novo
                return "Profissão atualizada"
            else:
                return "Profissão inválida"
        else:
            return "Profissão inválida"


