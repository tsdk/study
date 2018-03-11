
import codecs,sys
sys.stdout = codecs.lookup('utf-8')[-1](sys.stdout)
s = unicode("乐山大佛", 'utf-8')
print s

mystr = unicode(u"9hello流口水的份",'utf8');
myint = 1234;
str = ''' %s jack, you are %d00''' % (mystr, myint)
print mystr, myint, str

