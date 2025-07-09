
# Jogo da Velha com Inteligência Artificial (IA Especialista)

Este é um projeto de Jogo da Velha (Tic-Tac-Toe) desenvolvido em Python, com um sistema especialista implementado para o jogador de IA. A IA segue regras definidas em ordem de prioridade para jogar de forma inteligente e estratégica.

## 🧠 Estratégia da IA

A IA toma decisões com base nas seguintes regras, testadas nesta ordem:

1. **R1**: Se a IA ou o adversário tiver duas marcações em sequência, marca o terceiro espaço para vencer ou bloquear.
2. **R2**: Se houver uma jogada que crie duas ameaças de vitória ao mesmo tempo, faz essa jogada.
3. **R3**: Se o centro estiver livre, marca o centro.
4. **R4**: Se o oponente tiver marcado um canto, marca o canto oposto (se livre).
5. **R5**: Marca qualquer canto livre.
6. **R6**: Marca qualquer casa livre restante.

---


