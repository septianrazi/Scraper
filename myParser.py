## MAIN FUNCTION 
# takes a web element and returns dictionary of stuff
def getDetailsFromWebElement(webelement):
    res_dict = {}
    res_dict["date"]            = getDate(webelement)
    res_dict["name"]            = getName(webelement)
    res_dict["text"]            = getTextContent(webelement)
    res_dict["comment_count"]   = getCommentCount(webelement)
    res_dict["like_count"]      = getLikes(webelement)
    res_dict["link"]            = getLink(webelement)
    return res_dict

## HELPER FUNCTIONS BELOW

def getDate(webelement):
    try: 
        date_webelement = webelement.find_element_by_xpath(".//div[@data-testid='story-subtitle']")
        date_text = date_webelement.find_element_by_xpath(".//abbr").get_attribute("title")
        return date_text
    except:
        return ""

def getTextContent(webelement):
    content_list = webelement.find_elements_by_xpath(".//div[@data-testid='post_message']")
    if len(content_list) == 0:
        return ""
    return content_list[0].text

def getName(webelement):
    name_list = webelement.find_elements_by_xpath(".//a[@class='profileLink']") 
    if len(name_list) == 0:
        return ""
    name = name_list[0].text 
    return name

def getLikes(webelement):
    likes_list = webelement.find_elements_by_xpath(".//span[@class='_81hb']")
    if len(likes_list) == 0:
        return 0
    likes = int(likes_list[0].text)
    return likes

def getCommentCount(webelement):
    comments_list = webelement.find_elements_by_xpath(".//a[@class='_3hg- _42ft']")
    if len(comments_list) == 0:
        return 0
    comments_text = comments_list[0].text
    comment_num = int(comments_text[0])
    return comment_num

def getLink(webelement):
    date_webelement_list = webelement.find_elements_by_xpath(".//a[@class='_5pcq']")
    if (len(date_webelement_list) == 0):
        return ""
    link_text = date_webelement_list[0].get_attribute("href")
    return link_text



