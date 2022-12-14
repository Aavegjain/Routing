Consider a simple abstraction of a computer network consisting of n routers communicating information to
one another. The communication is established by connecting some pairs of routers using links in such a
way that for any pair of routers x and y, it is possible to send data from x to y through a sequence of links.
To send a large file over a network, it is customary to divide it into smaller packets, and send those packets
one-by-one. The choice of the packet size is determined the underlying network: if a packet is larger than
the capacity of a link, the link is unable to transfer the packet and simply drops it. On the other hand,
having too small packets is undesirable due to a per-packet overhead involved in the transfer. Therefore,
given a source and a destination in the network, it makes sense to determine the size of the largest packet
that can be transferred through the network from the source to the destination. 

Let n denote the number of routers in our network, and let’s say that the routers are labeled 0, . . . , n − 1.
Each link is specified by a tuple (u, v, c), where u and v are the endpoints of the link and c is its capacity.
Such a link is able to transfer a packet of size at most c from u to v and from v to u (every link is bidirectional
and has the same capacity in either direction). Given the identities s and t of the source and the target router
respectively, we wish to determine the largest C such that a packet of size C can be transferred over the
network from s to t.

We have written a program to find that C and a sequence of routers v0, v1, . . . , vr−1,
where s = v0 and vr−1 = t, such that for each i, there exists a link of capacity at least C between vi−1 and
vi.
Let m denote the number of links in the network. You may assume that the network is connected, that
is, it is possible to transfer a small enough packet from any node to any other node. Note that a pair of
routers can have zero, one, or more than one links of different capacities between them 

how to use - the file router.py contains a function findMaxCapacity which given 
1. n: the number of routers in the network,
2. links: a list of 3-tuples of integers. A tuple (u, v, c) in this list represents a bidirectional link of
capacity c between u and v, where u, v ∈ {0, . . . , n − 1},
3. s: the source router (s ∈ {0, . . . , n − 1}),
4. t: the target router (t ∈ {0, . . . , n − 1}).

returns a pair (C,route), where,
1. C is the largest number such that a packet of size C can be transferred over the network from s to t.
2. route is a list of numbers from the set {0, . . . , n − 1} such that route[0] is s, route[len(route)-1]
is t, and for each i, there exists a link of capacity at least C between route[i-1] and route[i]. 
