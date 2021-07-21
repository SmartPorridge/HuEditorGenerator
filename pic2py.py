import base64


def pic2py(picture_names, py_name):

    write_data = []
    for picture_name in picture_names:
        filename = picture_name.replace('.', '_')
        open_pic = open("%s" % picture_name, 'rb')
        b64str = base64.b64encode(open_pic.read())
        open_pic.close()
        write_data.append('%s = "%s"\n' % (filename, b64str.decode()))

    f = open('%s.py' % py_name, 'w+')
    for data in write_data:
    	f.write(data)
    f.close()
 


def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()



if __name__ == '__main__':
    # 将图片写入.py文件
    pics = ["QR_arxivdaily.jpg",]
    pic2py(pics, 'memory_pic')	 # 将pics里面的图片写到 memory_pic.py 中
    print("ok")


    # 从.py读取图片
    # #产生临时图片，保存在当前目录下
    # get_pic(favicon3_ico, 'favicon3.ico')
    # #隐藏图片
    # win32api.SetFileAttributes('favicon3.ico', win32con.FILE_ATTRIBUTE_HIDDEN)
    # '''
    # 正常使用图片....
    # '''

    # #删除临时图片
    # os.remove('favicon3.ico')
