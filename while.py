count=0
while count<=5:
    # print("Hello World")
    count=count+1#print 6 times
    # print(count)
    print(f"{count}:{'Hello World'}")

    # Let’s skip printing when count == 3 and add a special message when count == 5.
count=0
while count<=5:
    count+=1
    if count==3:
        continue
    if count==5:
        print("special message")
    else:
        print("hello world ")
        #skip when count is 3 and print special message when count is 5
count =0
while count<=5:
    print("hello world")
    print(count)
    count+=2# it print 0,2,4
        