Web VPython 3.2

#ellipsoid(size=vec(3, 3, 3),texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_iWjwdE8K9i3glZnshH0N_jtM9KBxWQ6ekI4hWRXeQw&s=10")
box(size=vec(3, 3, 3),pos=vec(0,2.5,2),texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_iWjwdE8K9i3glZnshH0N_jtM9KBxWQ6ekI4hWRXeQw&s=10")
box(size=vec(3, 3, 3),pos=vec(2.5,2.5,-2),texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_iWjwdE8K9i3glZnshH0N_jtM9KBxWQ6ekI4hWRXeQw&s=10")
box(size=vec(3, 3, 3),pos=vec(-2.4,2.5,-2),texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_iWjwdE8K9i3glZnshH0N_jtM9KBxWQ6ekI4hWRXeQw&s=10")
box(size=vec(8, 8, 8),opacity = 0.8)
b = box
while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        box.pos.y = box.pos.y + 0.1
