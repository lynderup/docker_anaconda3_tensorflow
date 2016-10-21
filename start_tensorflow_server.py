import sys
import tensorflow as tf

task_index = sys.argv[1]

cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})
server = tf.train.Server(cluster, job_name="local", task_index=task_index)
