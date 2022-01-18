def compare(file1, file2):
    #open file 1 and store the list of lines in the variable lines1
    with open(file1, 'r', encoding="utf-8") as f1:
        lines1 = f1.readlines()
    #open file 2 and store the list of lines in the variable lines2
    with open(file2, 'r', encoding="utf-8") as f2:
        lines2 = f2.readlines()

    #instantiate variables that will count the number of words for each page and the total of words present on both pages
    tot1 = 0
    tot2 = 0
    A = 0

    #checks if the two files have the same number of lines
    if len(lines1) != len(lines2):
        print("the two files have a different number of lines")
        return
    else:
        for num in range(len(lines1)):
            #split each line into a list of words and add it to the wordcount for the file
            words1 = lines1[num].split();
            tot1 += len(words1)
            words2 = lines2[num].split();
            tot2 += len(words2)
            #if the two lines have the same number of words
            if len(words1) == len(words2):
                #zip takes pairs of tuples corresponding to the same index in each list
                for ann1, ann2 in zip(words1, words2):
                    #if annotators agree, add 1 to the count of agreed words
                    if ann1 == ann2:
                        A += 1
                    #else indicate the disagreement
                    else:
                        print("Disagreement on line "+str(num+1)+": Annotator 1 wrote: "+ann1+" Annotator 2 wrote: " + ann2)
            else:
                #indicate the disagreement
                print("different wordcount on line "+str(num+1))
                print("Annotator 1 wrote : "+lines1[num])
                print("Annotator 2 wrote : "+lines2[num])
                #the following part allows for finding if some words in the line are agreed, even though they are not aligned (in the case where one annotator added a space between words for example)
                for word in words1:
                    for word2 in words2:
                        if word == word2:
                            A += 1
                            break
        #calculate the agreement over the page
        perc_agreement = A/((tot1 + tot2)/2)
        print("The annotators agreed at "+ str(perc_agreement))
        return

if __name__ == "__main__":
    #two .txt files to compare as input
    compare("Co3.txt", "Fra3 (1).txt")
