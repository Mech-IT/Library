while True:
    import datetime
    def gatedate():
        return datetime.datetime.now()
    print("Press 1 if you  want list of total books")
    print("Press 2 if you want to donate the books")
    print("Press 3 if you want to lend the books")
    print("Press 4 if you want to return the books")
    print("What you want to do?")
    x=int(input())
    class Library:
        def __init__(self, content):
            self.own_books = content
        def add_books(self):
            a = input("Enter the name of book which has to be donated\n")
            z = open("books", "a")
            z.write(a + '\n')
            z.close()
        def lend_books(self):
            b=input("Enter the name of book which has to be lend \n")
            d=open("books")
            c=d.read()
            if b in c:
                print("Book available")
                k=input("Enter your name\n")
                m=open("books","r")
                lines=m.readlines()
                m.close()
                h=open("books","w")
                for line in lines:
                    if line.strip("\n") != b:
                      h.write(line)
                y = open("books_lend", "a")
                y.write(str([str(gatedate())]) + ": " + b +" is lend by " + k + "\n")
            else:
                print("Book is not available ")
                s=open("books_lend", "r")
                lines=s.readlines()
                new_list = []
                idx=0
                for line in lines:
                    if b in line:
                        new_list.insert(idx,line)
                        idx+=1
                        leng=len(new_list)
                        for i in range(leng):
                           print(end=new_list[i])
        def return_books(self):
                b = input("Enter the name of book which has to be return \n")
                d = open("books_lend")
                c = d.read()
                if b in c:
                    print("Ok return of book is valid")
                    k = input("Enter your name\n")
                    m = open("books_lend", "r")
                    lines = m.readlines()
                    m.close()
                    h = open("books_lend", "w")
                    for line in lines:
                        for line in lines:
                            if line.find(b) != -1:
                                pass
                            else:
                                h.write(line)
                    z = open("books", "a")
                    z.write(b + '\n')
                    y = open("books_return", "a")
                    y.write(str([str(gatedate())]) + ": " + b +" is return by " + k + "\n")
    f = open("books", "r")
    content = f.read()
    Pritam_Library = Library(content)
    if x==1:
        print(Pritam_Library.own_books)
        continue
    if x == 2:
        Pritam_Library.add_books()
        continue
    if x == 3:
        Pritam_Library.lend_books()
        continue
    if x == 4:
        Pritam_Library.return_books()
        continue










