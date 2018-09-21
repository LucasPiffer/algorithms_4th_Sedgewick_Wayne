def gcd(p, q)
  return p if q == 0
  remainder = p % q
  return gcd(q, remainder)
end

puts gcd(54, 24)

def binary_search(data_set, to_find)
  lo = 0
  hi = data_set.size - 1
  
  while(lo <= hi)
    mid = lo + (hi - lo) / 2

    if(to_find > data_set[mid])
      lo = mid + 1
    elsif(to_find < data_set[mid])
      hi = mid - 1
    else
      return mid
    end
  end 

  -1

end

data_set = [1, 2, 5, 10]
puts binary_search(data_set, 5)


