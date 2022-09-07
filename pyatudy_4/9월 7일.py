while True:
  string_input = input("정수 입력> ")
  if string_input.isdigit() :
    number_input_a = int(string_input)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2* 3.14 * numebr_input_a)
    print("원의 둘레:", 3.14 * number_input_a * number_input_a)
    break
  esle:
    print("정수를 입력하세요")


  numbers = [52, 273, 32, 103, 90, 10, 275]

  print("# (2) 요소 내부에 없는 값 찾기")
  number = 10000
  try:
    print("- {}는 {} 위치에 있다.".format(number, numbers.index(number)))
  except:
    print("- 리스트 내부에 없는 값이다.")



while True:
  print("test() 함수의 첫 줄입니다.")
  try:
    print("try 구문이 실행되었습니다.")
    break
    print("try 구문의 return 키워드 뒤입니다.")
  except:
    print("except 구문이 실행되었습니다.")
    break
  finally:
    print("finally 구문이 실행되었습니다.")
  print("test() 함수의 마지막 줄입니다.")


  class 학생:
    def __init__(self, name, korean, math, english, science):  # 클래스 내부함수 첫번째 매개변수로 반드시 self
      self.name = name
      self.korean = korean
      self.math = math
      self.english = english
      self.science = science

    def 총점(self):
      return self.korean + self.math + \
             self.english + self.science

    def 평균(self):
      return self.총점() / 4  # 함수 호출 :self.함수()

    def 출력(self):
      print(self.name, self.총점(), self.평균(), sep="\t")

students = [
  학생("윤인성", 84, 98, 78, 98),
  학생("연하진", 93, 95, 74, 92),
  학생("구지연", 92, 87, 76, 98),
  학생("김호창", 88, 95, 78, 84),
  학생("윤아린", 85, 87, 78, 81),
]
print("이름", "총점", "평균", sep="\t")
for student in students:
  student.출력()