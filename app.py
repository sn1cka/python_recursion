import functions_drawer

drawer = functions_drawer.Drawer(20000, 20000, "black")
drawer.draw_dragon_curve("white")

drawer.draw_farn("purple")
drawer.save_image()
