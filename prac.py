class Person:
  def __init__(me, name, age):
    me.name = name
    me.age = age

  def myfunc(me):
    print("Hello my name is " + me.name)

p1 = Person("John", 36)
p1.myfunc()


