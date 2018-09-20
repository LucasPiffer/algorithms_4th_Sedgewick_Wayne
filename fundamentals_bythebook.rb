def gcd(p, q)
  return p if q == 0
  remainder = p % q
  return gcd(q, remainder)
end

puts gcd(54, 24)
