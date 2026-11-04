Web VPython 3.2
import random
d0 = box(size=vec(3, 3, 3),pos=vec(0,2.4,2),texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_iWjwdE8K9i3glZnshH0N_jtM9KBxWQ6ekI4hWRXeQw&s=10")
d1 = box(size=vec(3, 3, 3),pos=vec(2.4,2.4,-2),texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_iWjwdE8K9i3glZnshH0N_jtM9KBxWQ6ekI4hWRXeQw&s=10")
d2 = box(size=vec(3, 3, 3),pos=vec(-2.4,2.4,-2),texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_iWjwdE8K9i3glZnshH0N_jtM9KBxWQ6ekI4hWRXeQw&s=10")
d3 = box(opacity=0)
ds =[d0,d1,d2,d3]
box(size=vec(8, 8, 8),opacity = 1, color = vec(0.5,0.25,0))

while True :
    rate(10)
    k = keysdown()
    rx = random.randint(0,3)
    ds[rx].pos.y = ds[rx].pos.y + 2.7
    sleep(0.3)
    ds[rx].pos.y = ds[rx].pos.y - 2.7
    sleep(0.3)
    print(rx)
