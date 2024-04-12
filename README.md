# Anki-Cards-App
 A flash card system based on the [Anki Flash Card system](https://en.wikipedia.org/wiki/Anki_(software)) Anki (暗記) simply meaning "memorize", to which is what flashcards help you do for most, if not all subjects.

 ![Sample Demo](https://github.com/rinriukato/Anki-Cards-App/blob/main/sample.gif)


## Features and Usage
The current word bank holds around 1,000+ of the most commonly Kanji and Vocabulary found in Japanese the basic principle is that the user will go through the word bank, and if the user clicks on the "Checkmark" button, it will remove that word from the word bank and create a word bank based on all the words the user has not gone through or have marked incorrectly.

To flip the card and display English, use the space bar as hinted by the text at the bottom of the application.

This updated wordbank will be saved as 'words-to-learn.csv' in the data folder of this project. However, if you wish to restart you can simply delete 'words-to-learn'.csv for the program to default to the default database.

## Notes
It is possible to change the flash card pack if you edit the contents of 'jp-en'.csv. Simply follow the format provided of:

 {[Japanese] : Word} and {[English]: Word}

