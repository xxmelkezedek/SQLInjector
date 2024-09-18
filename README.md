# Script de Teste de Injeção de SQL em Python

Este script simples em Python permite realizar testes básicos de injeção de SQL em uma URL fornecida pelo usuário. Ele envia payloads de teste para a URL e verifica possíveis respostas que possam indicar vulnerabilidades de injeção de SQL. O resultado indica se o site é vulnerável, possivelmente vulnerável ou não vulnerável.

## Funcionalidades
- Solicita uma URL ao usuário.
- Testa diferentes payloads de injeção de SQL.
- Retorna um diagnóstico indicando:
  - **Vulnerável**: se o site parece expor falhas de injeção de SQL.
  - **Possivelmente Vulnerável**: se há uma resposta suspeita, mas inconclusiva.
  - **Não Vulnerável**: se não há indícios de vulnerabilidade.

## Requisitos
- Python 3.x
- Biblioteca `requests` (instalar via pip)

## Instalação
1. Instale a biblioteca `requests`:
   ```bash
   pip install requests
