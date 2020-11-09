from pdfminer.layout import LAParams
import pdfminer


def parse_obj(lt_objs):
    # loop over the object list
    fp =[]
    tx=[]
    for obj in lt_objs:

        # if it's a textbox, print text and location
        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            # print ("%6d, %6d, %s" % (obj.bbox[0], obj.bbox[1], obj.get_text().replace('\n', '_')))
            # length = obj.bbox[3]-obj.bbox[1]
            length = obj.width
            # print ( "Text size", length)
            fp.append(int(length))
            tx.append(obj.get_text())

    return fp, tx


def most_frequent(fontsize):
    counter = 0
    num = fontsize[0]

    for i in fontsize:
        curr_frequency = fontsize.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


def filter_text(final_text_unfiltered):
    final_text = []
    fontsize1 = []
    for x in final_text_unfiltered:
        if x[1] == " \n":
            pass
        else:
            final_text.append(x)
    for f in final_text:
        fontsize1.append(f[0])
    most_freq_fontsize = most_frequent(fontsize1)
    talking_text = []
    len(final_text)
    for i in range(len(final_text)):
        if final_text[i][0] == most_freq_fontsize:
            talking_text.append(final_text[i][1])
    return talking_text
