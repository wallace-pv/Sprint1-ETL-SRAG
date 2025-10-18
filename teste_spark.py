from pyspark.sql import SparkSession

print("Iniciando o script de teste do Spark...")
try:
    spark = SparkSession.builder.appName("TesteTerminal").getOrCreate()
    print("\n!!! SUCESSO: Sessão Spark criada com sucesso !!!\n")
    spark.stop()
    print("Sessão Spark encerrada.")
except Exception as e:
    print(f"\nOcorreu um erro devastador: {e}")