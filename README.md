# Gambler's Ruin Monte Carlo Simulation

## Overview

This project simulates the classical Gambler's Ruin problem using Monte Carlo methods. It models a simple random walk where a player repeatedly wins or looses a fixed amount until reaching either bankruptcy or a target wealth

The goal is to estimate how the probability of ruin changes with different win probabilities.

## Setup

A player starts with an initial balance and repeatedly plays a fair or biased game:
- Wins add 1 to your balance
- Losses subtract 1 to your balance
The game ends when the player either goes bankrupt or reaches their target wealth.

## Experiments

The experiments test 3 probabilities:
- p = 0.49
- p = 0.50
- p = 0.51

