from src.models.store import Store
from src.models.usuario import Usuario
from src.services.service_usuario import ServiceUsuario

#usuario = Usuario("Bruno","QA")
#print(usuario.nome)
#print(usuario.profissao)

#usuario = Usuario("Rafael","Engenheiro")
#print(usuario.nome)
#print(usuario.profissao)

store = Store()
#print(store.bd)

service = ServiceUsuario()
result = service.add_usuario("Bruno", "QA")
print(result)
