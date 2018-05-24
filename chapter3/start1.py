import tensorflow as tf

hello = tf.constant("hello")
print(hello)

session = tf.Session();

print(session.run(hello))

session.close()


a = tf.constant(3)
b = tf.constant(4)
with tf.Session() as sess:
    print(sess.run(a*b))


## 占位符







