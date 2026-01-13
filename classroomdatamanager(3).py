class Student:
    def __init__(self,id,name,birth,student_class,score):
        self.id = id
        self.name = name
        self.birth = birth
        self.student_class = student_class
        self.score = score
    def chuanhoa(self):
        if self.birth[1] == '/':
            self.birth = '0'+ self.birth
        if self.birth[4] == '/':
            self.birth = self.birth[0:3] + '0' + self.birth[3:]
    def __str__(self):
        return f"{self.id} {self.name} {self.birth} {self.student_class} {self.score:.2f}"
class StudentManager:
    def __init__(self):
        self.students = []
    def add(self,student: Student):
        student.chuanhoa()
        return self.students.append(student)
    def remove(self,id):
        s = self.search(id)
        if s:
            self.students.remove(s)
            return True
        return False
    def search(self,id):
        for s in self.students:
            if s.id == id:
                return s
        return None
    def update(self,id,name=None,birth=None,student_class=None,score=None):
        s=self.search(id)
        if s:
            if name : s.name = name
            if birth :
                s.birth = birth
                s.chuanhoa()
            if student_class : s.student_class = student_class
            if score : s.score = score
            return True
        return False
    def show_all(self):
        if not self.students:
            print('Danh sách trống')
        for s in self.students:
            print(s)
if __name__=='__main__':
    
    s=StudentManager()
    
    while 1 :
        print('1: Thêm sinh viên')
        print('2: Xóa sinh viên')
        print('3: Tìm kiếm sinh viên')
        print('4: Cập nhật thông tin')
        print('5: Xuất danh sách sinh viên')
        print('6: Thoát')
        
        try:
            n = int(input('Chọn mục : '))
        except ValueError:
            print("Vui lòng nhập số!")
            continue
        if n == 1:
            student=Student(input('Nhập id : '),input('Nhập tên : '),input('Nhập ngày sinh : '),input('Nhập lớp : '),float(input('Nhập điểm : ')))
            s.add(student)
            print('Thêm thành công')
        elif n == 2:
            res = s.remove(input('Nhập ID cần xóa : '))
            if res:
                print('Xóa thành công')
            else:
                print('Không tìm thấy ID')
        elif n == 3:
            res = s.search(input('Nhập ID : '))
            if res:
                print(res)
            else:
                print('Không tìm thấy')
        elif n == 4:
            id_input = input('Nhập ID cần sửa : ')
            res = s.search(id_input)
            if res:    
                print('Ấn ENTER nếu bỏ qua ko muốn thay đổi')
                name = input('Nhập tên : ')
                birth = input('Nhập ngày sinh : ')
                student_class = input('Nhập lớp : ')
                score = input('Nhập điểm : ')
                score_fl = float(score) if score else None
                score = score_fl
                if s.update(id_input,name,birth,student_class,score):
                    print('Cập nhật thành công')
            else:
                print('Không tìm thấy sinh viên')

        elif n == 5:
            s.show_all()
                           
        else:
            break
