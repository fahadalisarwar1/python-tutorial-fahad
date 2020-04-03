if __name__ == "__main__":
    msg = "this is my new message"
    print(len(msg)) # length doesnt start at 0 
    print(msg[3::2])
    print(msg[0:len(msg):5])

    print(msg.capitalize())
    print(msg.count('i'))
    print(msg.startswith('t'))
    print("this" in msg)
    print(msg.upper())
    print(msg.lower())
    print(msg.encode())

    print(msg.find('new'))
    print(msg.replace('new', "old")) # not inplace
    print(msg) # original message

