function getPrimesUpTo(limit: number): number[] {
  if (limit < 2) return [];

  const primes: number[] = [];
  const isPrime: boolean[] = new Array(limit + 1).fill(true);
  isPrime[0] = isPrime[1] = false;

  for (let i = 2; i <= limit; i++) {
    if (isPrime[i]) {
      primes.push(i);
      for (let j = i * i; j <= limit; j += i) {
        isPrime[j] = false;
      }
    }
  }

  return primes;
}

const primes = getPrimesUpTo(2000);
console.log(`Found ${primes.length} prime numbers up to 2000`);
console.log(`First 10 primes: ${primes.slice(0, 10).join(', ')}`);
console.log(`Last 10 primes: ${primes.slice(-10).join(', ')}`);