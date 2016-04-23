import tensorflow as tf

hello = tf.constant('hello, tesorflow!')

sess = tf.Session()
print sess.run(hello)

print hello


a = tf.constant(2)
b = tf.constant(3)

c = a+b

print c

print sess.run(c)