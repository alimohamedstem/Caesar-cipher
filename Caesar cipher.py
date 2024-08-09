import string

alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list(input('The text: \n').lower())

what_to_do = input(
    'encrypt or decrypt \n').lower()

shift_number = int(input('Theshift number from 1 to 25: \n'))

end_program = False

while not end_program:
    if what_to_do == 'encrypt':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
        print(''.join(map(str, sentence)))
        end_program = True
    elif what_to_do == 'decrypt':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) - shift_number
                sentence[i] = alphabets[new_letter]
        print(''.join(map(str, sentence)))
        end_program = True
    else:
        decide = input(
            'Error to retry press y or press n to end programm : \n').lower()
        if decide == 'y':
            sentence = list(input('enter your text: \n').lower())
            what_to_do = input(
                'encrypt or decrypt \n').lower()
            shift_number = int(input('The shift number from 1 to 25: \n'))
        else: 
            end_program = True