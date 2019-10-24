 https://en.wikipedia.org/wiki/Consistent_hashing . 
 
>To Run python3.7 -m test 

Simplest Explanation
====================
>What is normal hashing ? </br>

Let's say we have to store the following key value pair in a distributed memory store like redis.
<table style="width:100%">
  <tr>
    <th>Id</th>
    <th>Name</th>
  </tr>
  <tr>
    <td>Id-1</td>
    <td>Smith</td>
  </tr>
  <tr>
    <td>Id-2</td>
    <td>Jackson</td>
  </tr>
  <tr>
    <td>Id-3</td>
    <td>Thomas</td>
  </tr>
  <tr>
    <td>Id-4</td>
    <td>Tom</td>
  </tr>
  <tr>
    <td>Id-5</td>
    <td>Jerry</td>
  </tr>
</table>

Let say we have a hash function f(id) ,that takes above ids and  creates hashes  from it . </br>
Assume we have 3 servers - (s1 , s2 and s3)</br>
We can do a modulo of hash by the no of servers ie 3 , to map each each key to a server and we are left with following.
<table style="width:100%">
  <tr>
    <th>Id</th>
    <th>Name</th>
    <th>Hash f(Id)</th>
    <th>Server(Hash % No of servers)</th>
  </tr>
  <tr>
    <td>Id-1</td>
    <td>Smith</td>
    <td>1123</td>
    <td>node-1</td>
  </tr>
  <tr>
    <td>Id-2</td>
    <td>Jackson</td>
    <td>1211</td>
    <td>node-2</td>
  </tr>
  <tr>
    <td>Id-3</td>
    <td>Thomas</td>
    <td>1600</td>
    <td>node-1</td>
  </tr>
  <tr>
    <td>Id-4</td>
    <td>Tom</td>
    <td>1801</td>
    <td>node-1</td>
  </tr>
  <tr>
    <td>Id-5</td>
    <td>Jerry</td>
    <td>1788</td>
    <td>node-0</td>
  </tr>
</table>
We could retreive the value for a key by simple lookup using f().
Say for key Jackson , f("Jackson")%(no of servers) => 1211*3 = 2 (node-2)

*This looks perfecto , yea close but not cigar !* </br>
But What if a server say node-1 went down ?
Applying the same formula ie f(id)%(no of servers)  for user Jackson,  ```1211%2 = 1``` ie we got ~~node-1~~ when the actual key is hashed to **node-2** from the above table .</br></br>
We could do remapping here , What if we have a billion keys ,in that case we have to remap a large no of keys which is tedious :(

*This is a major flow in traditional hashing technique.*

>What is Consistent Hashing ?

In Consistent hashing , we visualize  list of all nodes in a circular ring .(Basically a sorted array)

![alt text](https://github.com/melvilgit/Consistent-Hashing/blob/master/ch1.png)

```
start func
For each node:
 Find f(node) where f is the hash function
 Append each f(node) to a sorted array
For any key
  Compute the hash f(key)
  Find the first f(node)>f(key)
  map it
end func
```

for example, if we have to hash key smith, we compute the hash value 1123 , find the immediate node having hash value > 1123 ie node 3 with hash value 1500 

Now , What if we loose a server , say we loose node-2 , All the keys can be mapped to next server node-3 :) </br>
Yea , we only have to remap the keys of node-2
</br></br>
![alt text](https://github.com/melvilgit/Consistent-Hashing/blob/master/ch2.png)

