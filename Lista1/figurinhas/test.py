import subprocess

with open("in.txt", "r") as f:
    entrada = f.read()

with open("out.txt", "r") as f:
    saida_esperada = f.read()

resultado = subprocess.run(
    ["python", "figurinhas.py"],
    input=entrada.encode(),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

saida = resultado.stdout.decode()

if saida.strip() == saida_esperada.strip():
    print("✅ Teste passou!")
else:
    print("❌ Teste falhou!")
    print("\nEntrada usada:")
    print(entrada)
    print("\nSaída esperada:")
    print(saida_esperada)
    print("\nSaída obtida:")
    print(saida)
