#!/usr/bin/env python3

operacoes =  {
  "analista": "Denis",
  "age" : 39
}

operacoes.update({"analista1": "Diego"})

#print(type(operacoes))
print(operacoes["analista1"])