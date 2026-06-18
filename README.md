# Prime Numbers Generator

A TypeScript program to find all prime numbers up to 2000 using the Sieve of Eratosthenes algorithm.

## Features

- Efficient prime number generation up to 2000
- Uses the Sieve of Eratosthenes algorithm for optimal performance
- Written in TypeScript with strict type checking

## Installation

```bash
npm install
```

## Usage

### Build

```bash
npm run build
```

### Run

```bash
npm start
```

### Development (with ts-node)

```bash
npm run dev
```

## Algorithm

The program uses the Sieve of Eratosthenes, which:
1. Marks all numbers as potentially prime
2. Iterates from 2, marking multiples of each prime as composite
3. Returns all remaining unmarked numbers as primes

## Results

The program finds 303 prime numbers up to 2000.