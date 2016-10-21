import sys
import tensorflow as tf

task_index = int(sys.argv[1])

import json

with open('clusterspec.json', 'r') as f:
    clusterspec = json.load(f)

    cluster = tf.train.ClusterSpec(clusterspec)
    server = tf.train.Server(cluster, job_name="worker", task_index=task_index)
    server.join()
