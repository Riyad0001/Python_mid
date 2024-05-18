class Star_Cinema:
    hall_list=[]

    def hall_list(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,colam,hall_no):
        self._seats={}
        self._show_list=[]
        self.rows=rows
        self.colam=colam
        self._hall_no=hall_no

    def hall_no(self):
        return self._hall_no

    def entry_show(self,show_id,movie_name,time):
        show=(show_id,movie_name,time)
        self._show_list.append(show)

        self._seats[show_id]=[['0' for i in range(self.colam)] for i in range(self.rows)]

    def book_seats(self,show_id,seat_list):
        if show_id not in self._seats:
            print("Invalid Show Id.")
            return

        for row,clm in seat_list:
            if row>=self.rows or clm >=self.colam or row<0 or clm<0:
                print(f'Invalid seat Position: ({row},{clm})')
                continue

            if self._seats[show_id][row][clm]=='X':
                print(f'seat at position ({row},{clm}) is already booked.')
                continue
            self._seats[show_id][row][clm]='X'
    def view_show_list(self):
        for show in self._show_list:
            print(f'Id: {show[0]},Movie: {show[1]},Time: {show[2]}')
    
    def view_available_seats(self,show_id):
        if show_id not in self._seats:
            print('Invalid show Id')
            return
        seats=self._seats[show_id]
        for row_ind,row in enumerate(seats):
            for col_ind,seats in enumerate(row):
                print(f'Seat ({row_ind},{col_ind}): {'Availablee' if seats=='0' else 'Boked'}')

#Examplee

halll=Hall(5,5,"Hall 01")
halll.entry_show(101,"Jawan Majhi",'6:00')
halll.entry_show(107,"3 Ediots",'21:00')

halll.view_show_list()
halll.book_seats(101,[(2,2),(3,3)])
halll.view_available_seats(101)

try:
    halll.book_seats(101, [(1, 1)]) 
except:
    print('Error happened')

try:
    halll.book_seats(101, [(4, 4)])
except:
    print('Error happened')

try:
    halll.book_seats(101, [(1, 1)])
except:
    print('Error happened')
