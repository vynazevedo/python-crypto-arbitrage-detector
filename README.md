# crypto-arbitrage-detector

> Bot de detecção de oportunidades de arbitragem em criptomoedas na exchange Kraken

## Sobre o Projeto

Este projeto foi desenvolvido como parte do meu portfólio para demonstrar habilidades em:
- Desenvolvimento Python
- Integração com WebSockets
- Manipulação de dados em tempo real
- Trading algorítmico
- Análise de mercado cripto

## Funcionalidades

- ✅ Conexão em tempo real com a Kraken via WebSocket
- ✅ Monitoramento de múltiplos pares de trading
- ✅ Detecção automática de oportunidades de arbitragem
- ✅ Cálculo de potencial de lucro
- ✅ Suporte a múltiplas rotas de arbitragem
- ✅ Foco inicial em pares com EUR

## 🔧 Tecnologias Utilizadas

- Python 3.8+
- WebSocket-client
- Threading
- JSON
- Kraken WebSocket API

## Como Funciona

O bot monitora continuamente os preços de diferentes pares de criptomoedas na Kraken e identifica oportunidades de arbitragem triangular. Por exemplo:
```
EUR -> BTC -> ETH -> EUR
```

### Processo:
1. Conecta-se ao WebSocket da Kraken
2. Subscreve aos tickers de pares relevantes
3. Atualiza preços em tempo real
4. Analisa rotas de arbitragem potenciais
5. Calcula possíveis lucros

## Instalação

```bash
# Clone o repositório
git clone https://github.com/vynazevedo/crypto-arbitrage-detector.git

# Entre no diretório
cd crypto-arbitrage-detector

# Instale as dependências
pip install -r requirements.txt

# Execute o bot
python kraken_arbitrage_bot.py
```

## Exemplos de Uso

```python
# Iniciar o bot
bot = KrakenArbitrageBotV2()
bot.start()

# Saída exemplo:
# Oportunidade de Arbitragem Detectada na Rota ['EUR', 'BTC', 'ETH', 'EUR']: Lucro potencial de 12.34 EUR
```

## Configuração

O bot pode ser configurado através do arquivo `config.py`:
```python
MINIMUM_PROFIT = 0.1  # Lucro mínimo em percentual
TRADE_AMOUNT = 1000   # Quantidade base para cálculos
PAIRS_TO_MONITOR = [  # Pares para monitorar
    'XBT/EUR',
    'ETH/EUR',
    'XRP/USD',
    'LTC/EUR',
    'ETH/XBT'
]
```

## Disclaimers

- Este é um projeto demonstrativo para portfólio
- Não é recomendado para uso em trading real sem modificações
- Não leva em consideração taxas de trading ou slippage
- Necessita de otimizações para uso em produção

## Segurança

- Não armazena chaves de API
- Utiliza apenas dados públicos da exchange
- Implementa reconnect automático em caso de desconexão

## Melhorias Futuras

- [ ] Suporte a mais pares de trading
- [ ] Implementação de backtesting
- [ ] Cálculo de taxas nas rotas
- [ ] Interface gráfica para monitoramento
- [ ] Logs detalhados de oportunidades
- [ ] Integração com mais exchanges

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas features
- Enviar pull requests

---
> Este projeto faz parte do meu portfólio pessoal e demonstra minhas habilidades em desenvolvimento Python, integração com APIs e análise de dados em tempo real.
