def solve00():
  ans = 2**38
  print ans


def solve01():
  string1 = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
  bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
  qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
  ans = ""
  for char in string1:
    if char >= 'a' and char <= 'z':
      new = (ord(char) - 97 + 2) % 26 + 97
      ans += chr(new)
    else:
      ans += char
  # print ans

  string2 = 'map'
  ans = ""
  for char in string2:
    if char >= 'a' and char <= 'z':
      new = (ord(char) - 97 + 2) % 26 + 97
      ans += chr(new)
  print ans


def solve02():
  mystring = ''
  with open('prob_02', 'r') as myfile:
    for line in myfile:
      mystring += line
  mystring = mystring.translate(None, '{!@#$%^&*()}[]+_\n')
  print mystring


def solve03():
  import re
  mystring = ''
  with open('prob_03', 'r') as myfile:
    for line in myfile:
      newline = re.sub(r'.*[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z].*', r"\1", line)
      if line != newline:
        mystring += newline
  mystring = mystring.translate(None, '\n')
  print mystring


def solve04():
  import urllib2
  url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345' 
  html = urllib2.urlopen(url)
  mystring =  html.read()
  mystringlist = mystring.split()

  '''
  for i in range(200):
    newurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='  
    newurl += mystringlist.pop()
    html = urllib2.urlopen(newurl)
    mystring = html.read()
    print str(i) + ": " + mystring
    mystringlist = mystring.split()
  # print str(92118 / 2)
  '''

  '''
  mystringlist = ['33110']
  for i in range(200):
    newurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    newurl += mystringlist.pop()
    html = urllib2.urlopen(newurl)
    mystring = html.read()
    print str(i) + ": " + mystring
    mystringlist = mystring.split()
  '''

  print 'peak.html'


def solve05():
  pass


def solve06():
  pass


def solve07():
  pass


def solve08():
  pass


def solve09():
  pass


def solve10():
  pass


def solve11():
  pass


def solve12():
  pass


def solve13():
  pass


def solve14():
  pass


def solve15():
  pass


def solve16():
  pass


def solve17():
  pass


def solve18():
  pass


def solve19():
  pass


def solve20():
  pass


print "0---------------------------------"
solve00()

print
print "1---------------------------------"
solve01()

print
print "2---------------------------------"
solve02()

print
print "3---------------------------------"
solve03()

print
print "4---------------------------------"
solve04()

"""
print
print "5---------------------------------"
solve05()

print
print "6---------------------------------"
solve06()

print
print "7---------------------------------"
solve07()

print
print "8---------------------------------"
solve08()

print
print "9---------------------------------"
solve09()

print
print "10--------------------------------"
solve10()

print
print "11--------------------------------"
solve11()

print
print "12--------------------------------"
solve12()

print
print "13--------------------------------"
solve13()

print
print "14--------------------------------"
solve14()

print
print "15--------------------------------"
solve15()

print
print "16--------------------------------"
solve16()

print
print "17--------------------------------"
solve17()

print
print "18--------------------------------"
solve18()

print
print "19--------------------------------"
solve19()

print
print "20--------------------------------"
solve20()

"""
