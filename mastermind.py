print '<head>'
print '<style type="text/css">'
print 'body { font-family: arial; margin-left: 200px; margin-top: 60px; padding: 50px; background: linear-gradient(to top right, yellow, green);}'
print 'h1 { font-weight: 200; font-size: 80px }'
print 'span { color: #dc0459; font-size: 100px }'
print '.input { border:none; padding: 10px; border-radius: 5px; font-size: 90%}'
print 'button { background: #beff4d }'
print '#guess { background: #d1ff80 }'
print '</style>'
print '</head>'

import cgi
import random
from random import randint
import ast
form = cgi.FieldStorage()

if "answer" in form:
    master = form.getvalue("answer");
    master = ast.literal_eval(master);
else:
    master = ""
    a = randint(0, 9)
    b = randint(0, 9)
    c = randint(0, 9)
    d = randint(0, 9)
    master = [a,b,c,d]

if "guess" in form:
    code = form.getvalue("guess");
else:
    code = ""

if "count" in form:
    count = int(form.getvalue("count")) + 1
else:
    count = 0

print '<h1>Mastermind<span>.</span></h1>'
print '<p>Can you guess the four-digit number?</p>'
print '<form method="post">'
print '<input type="text" name="guess" value="'+ code +'" class="input">'
print '<input type="hidden" name="answer" value="'+ str(master) +'">'
print '<input type="hidden" name="count" value="'+ str(count) +'">'
print '<input type="submit" value="Guess!" id="guess" class="input">'
print '<button type="submit" name="cheat" class="input" value=0>Show Answer!</button>'
print '</form>'

if "guess" in form:
    code = form.getvalue("guess");
    white = 0
    red = 0
    i = 0
    while i <= 3:
        if int(code[i]) == master[i]:
            red += 1;
            i += 1;
        else:
            if int(code[i]) in master:
                white += 1;
                i += 1;
            else:
                i += 1;
    if white == 0 and red == 0:
        print "No number matches."
    else:
        if red == 4:
            print "You won! You used " + str(count) + " guesses. <a href=''>Play again!</a>"
        else:
            print str(white) + " digit(s) matched in a different spot and " + str(red) + " digit(s) matched in the correct spot."
else:
    print "4 digits required."

if "cheat" in form:
    print "<br><br>"+"Answer: " + str(master) + " <a href=''>Play again!</a>";
