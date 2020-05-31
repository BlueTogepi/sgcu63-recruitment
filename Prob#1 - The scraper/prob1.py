from bs4 import BeautifulSoup
from requests import get

def getBaanContent(url):
    response = get(url)
    doc = BeautifulSoup(response.text, "html.parser")
    # assumption: all div tag that contain Baan's data must be a class of "baan-info-module--text-wrapper--uuYTz"
    baan = doc.find(class_="baan-info-module--text-wrapper--uuYTz")

    # assumption: all Baan div tag must have div as its children, and Baan name as the first content of div and Baan Slogan as the second
    try:
        name = "".join([str(e) for e in baan.div.contents[0].contents])
    except:
        name = None
    
    try:
        slogan = "".join([str(e) for e in baan.div.contents[1].contents])
    except:
        slogan = None
    
    return [name, slogan]

def baan2TableRow(name, slogan):
    return "<tr><td>" + name + "</td><td>" + slogan + "</td></tr>"

# assumption: all Baan urls will be as below
urls_list = [
    "https://rubnongkaomai.com/baan/abnormal",
    "https://rubnongkaomai.com/baan/agape",
    "https://rubnongkaomai.com/baan/buem",
    "https://rubnongkaomai.com/baan/dork",
    "https://rubnongkaomai.com/baan/duidui",
    "https://rubnongkaomai.com/baan/indiana",
    "https://rubnongkaomai.com/baan/judson",
    "https://rubnongkaomai.com/baan/khunnoo",
    "https://rubnongkaomai.com/baan/mheenoi",
    "https://rubnongkaomai.com/baan/pak-tak-agard",
    "https://rubnongkaomai.com/baan/panarak",
    "https://rubnongkaomai.com/baan/phee",
    "https://rubnongkaomai.com/baan/rhoy",
    "https://rubnongkaomai.com/baan/seiyw",
    "https://rubnongkaomai.com/baan/tem",
    "https://rubnongkaomai.com/baan/buchayun",
    "https://rubnongkaomai.com/baan/dung",
    "https://rubnongkaomai.com/baan/fyo",
    "https://rubnongkaomai.com/baan/kids",
    "https://rubnongkaomai.com/baan/koh",
    "https://rubnongkaomai.com/baan/laijai",
    "https://rubnongkaomai.com/baan/nhai",
    "https://rubnongkaomai.com/baan/preaw",
    "https://rubnongkaomai.com/baan/wang",
    "https://rubnongkaomai.com/baan/wanted",
    "https://rubnongkaomai.com/baan/work",
    "https://rubnongkaomai.com/baan/aaum",
    "https://rubnongkaomai.com/baan/jodeh-huesa",
    "https://rubnongkaomai.com/baan/koom",
    "https://rubnongkaomai.com/baan/por",
    "https://rubnongkaomai.com/baan/sod",
    "https://rubnongkaomai.com/baan/soeiteelheemouy",
    "https://rubnongkaomai.com/baan/indy",
    "https://rubnongkaomai.com/baan/jo+",
    "https://rubnongkaomai.com/baan/rang",
    "https://rubnongkaomai.com/baan/yim"
]

html_wrapper = """
<!DOCTYPE html>
<html>
    <head>
        <title>RubNongKaoMai Baans</title>
    </head>
    <body>
    <table style="margin-left: auto; margin-right: auto;" border="1" cellspacing="0" cellpadding="5">
        <tbody>
        <tr>
            <td><strong>ชื่อบ้าน</strong></td>
            <td><strong>สโลแกน</strong></td>
        </tr>
        %s
        </tbody>
    </table>
    </body>
</html>
"""

tableRows = list()
html_file = open("table.html",'w', encoding="utf-8")

for url in urls_list:
    print("Getting " + url + " ...")
    baan = getBaanContent(url)
    tableRows.append(baan2TableRow(baan[0], baan[1]))

html_whole = html_wrapper % "".join(tableRows)
html_file.write(html_whole)
html_file.close()