# Implementation-of-Redis

OVERVIEW
Most of you have heard the term redis ( https://en.wikipedia.org/wiki/Redis )
which is a key-value store. The essence of a key-value store is the ability to
store some data, called a value, inside a key. The value can be retrieved
later only if we know the specific key it was stored in. it is persistent, i.e.
when your application ends, the data doesn't go away.


GOALS
A working implementation of redis with some basic functionalities like
1. GET ( https://redis.io/commands/get )
2. SET ( https://redis.io/commands/set )
3. EXPIRE ( https://redis.io/commands/expire )
4. ZADD ( https://redis.io/commands/zadd )
5. ZRANK ( https://redis.io/commands/zrank )
6. ZRANGE ( https://redis.io/commands/zrange )
