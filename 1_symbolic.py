import tensorflow as tf

A = tf.placeholder(tf.int32, name='A')
B = tf.placeholder(tf.int32, name='B')

T1 = tf.multiply(A, A, name='T1')
T2 = tf.multiply(B, B, name='T2')

T3 = tf.add(T1, T2, name='T3')

with tf.Session() as sess:
    writer = tf.summary.FileWriter('./symbolicLogs/', sess.graph)
    output = sess.run(T3, feed_dict={A: 3, B: 4})
    print("Resultado: {}".format(output))

#tensorboard --logdir=symbolicLogs/