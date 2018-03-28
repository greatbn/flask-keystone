### Flask with Keystone middleware


- Flow

```s
                        +---------------+                   +--------------+
                        |               |                   |              |
                        |               |                   |              |
          Request       |               |     Authen        |              |
+----------------------->     Your APP  +------------------->  Openstack   |
                        |               |                   |  Keystone    |
                        |               |      Author       |              |
                        |               <-------------------+              |
                        +---------------+                   +--------------+
```


- Test

```s
➜  flask-keystone set TOKEN gAAAAABauyJGY56wccQXD6e8bne5R8UqHCx3R_y18UVqoM1hQVLpmyZH2uKPBKM_5z-i0nVNx_s-DqPu99xu50QnUCP6YBc8wLuzu49DFPZ0kx4-v0YYm8en2UP3cVOOyO1oZImVW2YSjApAS200XioYFRX1uBoqT7ovYJ-fBja8XKO5dwu2Su4
➜  flask-keystone curl -H "X-Auth-Token: $TOKEN" localhost:5000
Authenticated⏎   
```
