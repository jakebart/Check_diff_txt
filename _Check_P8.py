#test program for project P8

def main():

    orig_pixel_list = []
    user_pixel_list = []
    cam_pgm = open("_cam.txt", "r")

    user_file_in = input("Which file do you want to check?: \n")
    user_file = open(user_file_in, "r")
    
    line = ""
    for strip in cam_pgm:
        line = strip.rstrip('\n')
        orig_pixel_list.append(line)

    for strip in user_file:
        line = strip.rstrip('\n')
        user_pixel_list.append(line)
    
    int_num = 0
    for x in orig_pixel_list:
        if orig_pixel_list[int_num] != user_pixel_list[int_num]:
            print("Oops, there's a difference")
            cam_pgm.close()
            user_file.close()
            quit()
        int_num += 1
    print("No difference found!")    
    cam_pgm.close()
    user_file.close()

main()
