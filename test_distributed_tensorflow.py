import tensorflow as tf
import json

with open('clusterspec.json', 'r') as f:
    clusterspec = json.load(f)

cluster = tf.train.ClusterSpec(clusterspec)
server = tf.train.Server(cluster, job_name="master", task_index=0)

a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')

with tf.device("/job:worker/task:0"):
    x = tf.matmul(a, b)

with tf.device("/job:worker/task:1"):
    y = tf.matmul(b, a)


sess = tf.Session(server.target, config=tf.ConfigProto(log_device_placement=True))
print(sess.run([x, y]))
