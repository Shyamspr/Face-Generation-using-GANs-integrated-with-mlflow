import mlflow
get_ipython().system('mlflow run . -P learning_rate=0.0001  -P noise_dim=100 -P num_examples_to_generate=16 -P buffer_size=202599 -P batch_size=256')

