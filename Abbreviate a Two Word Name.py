# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

# test.assert_equals(abbrev_name("Sam Harris"), "S.H")
# test.assert_equals(abbrev_name("patrick feenan"), "P.F")
# test.assert_equals(abbrev_name("Evan C"), "E.C")
# test.assert_equals(abbrev_name("P Favuzzi"), "P.F")
# test.assert_equals(abbrev_name("David Mendieta"), "D.M")

def abbrev_name(name):
    for one_word in name:
      if one_word == " ":
         index = name.index(one_word)
         index +=1

    return f"{name[0]}{'.'}{name[index]}".upper()

print(abbrev_name("P Favuzzi"))