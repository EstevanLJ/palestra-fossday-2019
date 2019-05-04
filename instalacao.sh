#https://www.tensorflow.org/install/pip

# Instalação das dependências
sudo apt-get update
sudo apt install python3-dev python3-pip
sudo pip3 install -U virtualenv 

# Criação do venv
virtualenv --system-site-packages -p python3 ./venv-tensorflow

# Inicializa no venv
source ./venv-tensorflow/bin/activate

#Atualiza o pip
pip install --upgrade pip

#Instala o tensorflow
pip install --upgrade tensorflow
pip install --upgrade matplotlib

#Verifica a instalação
python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"

#Sair do venv
deactivate