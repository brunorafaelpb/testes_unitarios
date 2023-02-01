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
        for i in range(len(self.store.bd)):
            return "ID:{} | Nome: {} | Profissão {}".format(i + 1, self.store.bd[i].nome, self.store.bd[i].profissao)

    def remove_usuario_id(self, id_usuario):
        usuario_removido = self.store.bd.pop(id_usuario-1)
        return "Usuário {} removido".format(usuario_removido.nome)

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


