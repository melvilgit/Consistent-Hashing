 https://en.wikipedia.org/wiki/Consistent_hashing . 

Simplest Explanation
====================
What is normal hashing ? </br>
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
Assume we have 3 servers - (s1 , s2 and s3)
We can do a modulo of hash by the no of servers ie 3 , to map each each key to a server and we are left with following.
<table style="width:100%">
  <tr>
    <th>Id</th>
    <th>Name</th>
    <th>Hash</th>
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


