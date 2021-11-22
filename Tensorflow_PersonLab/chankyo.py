import tensorflow as tf
 tf.__version__                  // 출력 : '1.15.0' (tensorflow 버전 확인)
hello = tf.constant('Hello Tensorflow!')

sess = tf.Session()

print(sess.run(hello))       // 출력 : b'Hello tensorflow'

a = tf.constant(1)

b = tf.constant(2)

print(sess.run(a + b))