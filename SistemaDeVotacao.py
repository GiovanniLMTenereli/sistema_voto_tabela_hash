#Feito por Giovanni Lisboa de Miranda Tenereli, GRR20230945
class SistemaDeVotacao:
    def __init__(self):
        self.ids: dict = {}
        self.candidatos: dict = {}
        
    def votar(self, idEleitor, candidato):
        if idEleitor not in self.ids:
            self.ids[idEleitor] = True
        else:
            return f"O Eleitor do id {idEleitor} já votou\n"
            
        if candidato in self.candidatos:
            self.candidatos[candidato] += 1
        else:
            self.candidatos[candidato] = 1
            
        return f"Voto registrado para o id {idEleitor}!\n"
    
    def contar_votos(self):
        if not self.candidatos:
            return "Nenhum voto registrado."
        else:
            resultado = "Resultados da eleição:\n"
            resultado += "\n".join(f"{candidato}: {votos} votos" for candidato, votos in self.candidatos.items())
            return resultado
        

if __name__ == "__main__":
    votacao = SistemaDeVotacao()

    print(votacao.votar(1, "C2"))
    print(votacao.votar(2, "C1"))
    print(votacao.votar(3, "C1"))
    print(votacao.votar(4, "C4"))
    print(votacao.votar(5, "C2"))
    print(votacao.votar(1, "C1"))  
    print(votacao.votar(7, "C5"))
    print(votacao.votar(2, "C1"))  
    print(votacao.votar(4, "C3"))  
    print(votacao.votar(8, "C2"))
    print(votacao.votar(10, "C3"))
    print(votacao.votar(3, "C1"))  

    print(votacao.contar_votos())

