import pytest
from Code import python2

def test_one():
    assert python2.one("hi","hello") == "hello"
    assert python2.one("three", "two") == "three"
    assert python2.one("three", "hello") == "three hello"
    assert python2.one("echo", "print") == "print"
    assert python2.one("fire","rib") == "fire"

def test_two():
    assert python2.two("bertclivebert") == "clive"
    assert python2.two("xxbertfridgebertyy") == "fridge"
    assert python2.two("xxBertfridgebERtyy") == "fridge"
    assert python2.two("xxbertyy") == ""
    assert python2.two("xxbeRTyy") == ""

def test_three():
    assert python2.three(3) == "fizz"
    assert python2.three(10) == "buzz"
    assert python2.three(15) == "fizzbuzz"
    assert python2.three(8) == "null"
    assert python2.three(75) == "fizzbuzz"

def test_four():
    assert python2.four("55 72 86") == 14
    assert python2.four("15 72 80 164") == 11
    assert python2.four("555 72 86 45 10") == 15
    assert python2.four("98 63 34 1 13") == 17
    assert python2.four("98 107 415") == 17

def test_five():
    assert python2.five("Jeff,private.key,False,1445") == ["Jeff"]
    assert python2.five("Bert,private.key,True,1447,Bert,public.key,True,1318,Jeff,private.key,False,1445") == ["Jeff"]
    assert python2.five("Bert,private.key,True,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445") == ["Jeff"]
    assert python2.five("Bert,private.key,False,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445") == ["Bert","Jeff"]
    assert python2.five("Bert,private.key,True,1447,Bert,public.key,True,1318,Jeff,private.key,True,1445") == []

def test_six():
    assert python2.six("ceiling") == True
    assert python2.six("believe") == True
    assert python2.six("glacier") == False
    assert python2.six("height") == False
    assert python2.six("receive") == True

def test_seven():
    assert python2.seven("Hello") == 2 
    assert python2.seven("hEelLoooO") == 6
    assert python2.seven("WhitEboarD") == 4
    assert python2.seven("as") == 1
    assert python2.seven("pass") == 1

def test_eight():
    assert python2.eight(1) == 1
    assert python2.eight(3) == 6
    assert python2.eight(4) == 24
    assert python2.eight(6) == 720
    assert python2.eight(8) == 40320

def test_nine():
    assert python2.nine("This is a Sentence","s") == 4
    assert python2.nine("This is a Sentence","S") == 8
    assert python2.nine("Fridge for sale","z") == -1
    assert python2.nine("I love Python", "L") == -1
    assert python2.nine("I LOVE PYTHON", "L") == 2

def test_ten():
    assert python2.ten("The",2,"h") == True
    assert python2.ten("AAbb",1,"b") == False
    assert python2.ten("Hi-There",10,"e") == False
    assert python2.ten("HEY",2,"e") == True
    assert python2.ten("on-premise",3,"-") == True
