from __future__ import absolute_import, division, print_function

import tensorflow as tf

tf.enable_eager_execution()
tf.executing_eagerly()

a = [[3.]]
b = [[4.]]

t1 = tf.matmul(a, a)
t2 = tf.matmul(b, b)
t3 = tf.add(t1, t2)

print("Resultado: {}".format(t3))