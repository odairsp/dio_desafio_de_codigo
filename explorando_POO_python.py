# Classe Pano, ela representa o plano de um usuário de telefone:


class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.saldo_atual = self.saldo

    # Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self):
        return self.saldo_atual

    # Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def custo_chamada(self, minutos, custo=0.1):
        return minutos * custo

    # Crie um método deduzir_saldo para deduz o valor do saldo do plano:
    def deduzir_saldo(self, custo_chamada):
        self.saldo_atual -= custo_chamada


# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano: Plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    # Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario, duracao):
        # Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
        custo_chamada = self.plano.custo_chamada(duracao)
        # Verifique se o saldo do plano é suficiente para a chamada.
        if custo_chamada <= self.plano.saldo_atual:
            # Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
            self.plano.deduzir_saldo(custo_chamada)
            saldo = self.plano.saldo_atual
            # E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
