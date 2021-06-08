# Table of Contents

1. [What is Kafka?](#what-kafka)
2. [Why is Kafka needed here?](#why-kafka)



# What is Kafka?<a name="what-kafka"></a>

- LinkedIn developed Kafka in 2011 as a high-throughput message broker for its own use, then open-sourced and donated Kafka to the [Apache Software Foundation](https://kafka.apache.org/)
- initial problem
  - data streams create new data, which in turn may effect the presently deployed model.
  - hence, instead of re-training and re-deploying the model once every x months or annually, dynamic re-training strategy is employed so that continual re-deployment can be avoided.
- problem - version-2
  - incoming data streams can affect a key dynamical property of interest, thus valuing its tracking.
  - normally, servers that produce such data-streams, called *producers* and servers that consume and process this data, *consumers* would be directly interacting with each other, i.e. connected with each other.
    - each producer has to be connected to each consumer server , since each consumer should be updated such that all of them have the exact same data.
  - as an organisation grows, so does its amount of producer and consumer servers , and so does the number of connections between producer and consumer servers.
    - for n producers and m consumers, the total connections required would be nm .
    - as n and m both increase, the total connections increase even more, thus making it unmanageable for this type of architecture, when it comers to handling continually streamed data.
- problem - version-3
  - the solution to the exploding number of connections between the producers and consumers is solved by having an intermediary that handles the data feed instead.
  - this reduces the number of connections from nm to n + m
  - 
- 
- zookeeper manages brokers, which broker is taking from producer and sending to consumer , setting up back-up brokers when the main brokers fail.
- <font color="red">how does the server machine(producer) know which kafka-cluster to send the data to?</font>
-  <font color="red">which of these are logical and which are physical?</font>
  - multiple consumers in the consumer group
  - multiple topics, i.e. brokers in the Kafka server
  - zookeeper deployment
  - partitions of a topic.





# General use cases<a name="usecases"></a>

- field of finance
  - detect fraud, market activities, real-time risks, 
  - <font color="red">applicability in market-making , or rather order matching engines in stock exchanges = ?</font>.
- retail
  - inventory, sales, pricing
- 









## Why is Kafka needed here?<a name="why-kafka"></a>