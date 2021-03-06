import tensorflow as tf
import numpy as np
def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    Wx_plus_b = tf.matmul(Weights,inputs) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs
#add axis
x_data = np.linspace(-1,1,300,dtype=np.float32)[:,np.newaxis]
#add noise
noise = np.random.normal(0,0.05,x_data.shape).astype(np.float32)
#actural data model
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])

#hidden layer
l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)
#output layer
prediction = add_layer(l1,10,1,activation_function=None)
#loss
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))
#optimizer
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
#init
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
        if i % 50 == 0:
            print(sess.run(train_step,feed_dict={xs:x_data,ys:y_data}))


