from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import pandas
from django.contrib.staticfiles.templatetags.staticfiles import static


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    i = 0
    wholetable = [["Bob Doe", 1, 23, 383.08],
    ["Jason Nani", 0, 0, 263.68]]
    data = [[271, 235, 256, 263, 286, 224, 254, 267, 323, 238, 273, 244, 165, 439, 166, 801, 685, 641, 705, 549, 563, 414, 588, 500, 627, 605, 725, 708, 594, 664, 620, 712, 642, 545, 425, 570, 747, 737, 139, 139, 147, 209, 211, 245, 230, 197, 254, 229, 247, 213, 280, 236, 241, 253, 277, 248, 243, 257, 219],
    [236, 231, 270, 284, 257, 262, 243, 250, 288, 332, 275, 267, 283, 248, 274, 266, 237, 294, 295, 235, 247, 273, 246, 268, 274, 283, 264, 256, 252, 263, 304, 256, 284, 283, 272, 261, 241, 258, 328, 265, 291, 269, 255, 268, 239, 286, 254, 265, 270, 278, 247, 283, 298, 308, 239, 268, 274, 258, 266]]
    # wholetable = [["Delilah Guardipee",0,0,222.98368655088],
    # ["Nathanial al-Harron",2,0.280358666081359,253.86157404815],
    # ["Jay Mateos-Gonzalez",0,0,224.10900925916],
    # ["Tarah Padilla",0,0,223.97566048756],
    # ["Kyle el-Amara",0,0,224.21460433691],
    # ["Sean al-Fahmy",4,0.220027998554751,245.38362108716],
    # ["Chase al-Khalaf",4,0.177193652159059,243.19866273294],
    # ["Hassan Cotonuts",3,0.298977878396366,255.53133360871],
    # ["Santee Kramer",5,0.166064080492475,241.29063085178],
    # ["Sarah al-Allam",4,0.170553801855034,241.40187913010],
    # ["Raaji Blackmon",5,0.0458478721206196,229.81461051947],
    # ["Andrew Munoz Leyva",0,0,223.29663917618],
    # ["Abdul Khaliq el-Farid",0,0,224.18508041037],
    # ["Isley Willis",2,0.222535868012681,248.04978906645],
    # ["Patricia Inthavong",0,0,225.46035561418],
    # ["Brandon Ryen",0,0,224.68803095248],
    # ["Christian Ali",5,0.196175054375484,244.49324659033],
    # ["Mus'ab Raley",3,0.1895446995233,243.94280470252],
    # ["Sean Helfer",0,0,225.24375334120],
    # ["Brittini Yazzie",0,0,225.58321200113],
    # ["Charles Goldston",0,0,223.93258779336],
    # ["Jessica Martin",0,0,224.19907473059],
    # ["Andrew Almada",0,0,224.97026030206],
    # ["Megan el-Yamin",3,0.198875409853004,244.13143184061],
    # ["Khiry Tipton",0,0,223.33833801180],
    # ["Tyondre Shaw",2,0.120271254467041,237.88469151851],
    # ["Jareer al-Rasheed",6,0.448649395400626,270.44802710717],
    # ["Alexandra Norris",0,0,226.46558107802],
    # ["Brandy Robertson",4,0.277586459489388,253.19120555461],
    # ["Tynan Portillos",3,0.418623892344652,266.83387796449],
    # ["Aaron Won",6,0.262334828790687,251.76508381265],
    # ["Shayla Chase",4,0.127855883682975,238.62431123766],
    # ["Cante Fink",0,0,224.30666068435],
    # ["Lisa Romero",0,0,226.52261314262],
    # ["Dominique Rodriguez",5,0.298233554834096,253.80830650105],
    # ["Maysa Sharrar",3,0.180067631179209,243.20588008028],
    # ["Zhjade Karman",0,0,226.17021746641],
    # ["William Murison",5,0.168627924150403,242.57900941574],
    # ["James Shannon",2,0.0925264522829091,233.93750826866],
    # ["Meghan Ahmed",0,0,225.03167974092],
    # ["Rihaab al-Dada",0,0,223.45043490585],
    # ["Orawan Bickel",9,0.230970614299164,247.47097128916],
    # ["Alexsondro White",4,0.109445966682853,234.95508940325],
    # ["Phaylinh Clark",0,0,226.80207455819],
    # ["Hibbaan al-Awan",0,0,226.59417959546],
    # ["Savannah al-Baccus",3,0.409949781536844,265.76763639600],
    # ["Frank Garcia",3,0.210364857650877,246.43244386604],
    # ["Hana Wilson",0,0,223.3270012998],
    # ["T'Aunsanae Riley",2,0.0976892439648509,234.08163015001],
    # ["Arif Ortega",9,0.205892091500575,245.56819225679],
    # ["Zuhair Landry",2,0.349289380421304,259.48849457634],
    # ["Nickolas Ho",4,0.173188020471938,244.78716911046],
    # ["Barry Marcos-Domingo",0,0,226.32940104266],
    # ["Lance Greene",0,0,224.19682571298],
    # ["Nicholas Lester",3,0.078000232208378,232.94231279772],
    # ["Dakota Her",8,0.24039675099712,249.79556587991],
    # ["Katrina Hallenbeck",0,0,225.3764706744],
    # ["Abdinasir Plumb",6,0.0731185770903659,231.42462428961],
    # ["Amy al-Niazi",6,0.191086670083291,243.51360684025],
    # ["Yameia Viner",0,0,225.22587806977],
    # ["Jesse Foreman",10,0.136265712046292,237.8788098262],
    # ["Azeema Hansen",4,0.292047241705447,253.66291518886],
    # ["Amari Go",0,0,224.99138539264],
    # ["Tahjneke Garcia Trevizo",0,0,224.37958590439],
    # ["Winthana Moscoso",0,0,223.44115607091],
    # ["Velhia Williams",6,0.389341243609192,264.01876221984],
    # ["Rachelle Borgen",7,0.136301528975146,239.06641551241],
    # ["Sarah Rusli",4,0.196589935747871,243.88640558967],
    # ["Angelica Anaya",0,0,225.25949036149],
    # ["Jasmine Elizalde III",4,0.180501464418122,243.28636099887],
    # ["Fernanda Coyote",0,0,225.23669414374],
    # ["Connor Rohde",2,0.238758426430615,248.33981731189],
    # ["Raaid Lor",5,0.238563101568964,249.96373478527],
    # ["Liam Moreno",0,0,225.8966900556],
    # ["Amber al-Waheed",0,0,224.94070539941],
    # ["Kristy Herrera",0,0,224.4615295418],
    # ["Jihaad Zimmerle",0,0,224.03152133737],
    # ["Savanna Mangino",0,0,226.27221445514],
    # ["Mumtaaza Garcia-Perez",0,0,225.52066460895],
    # ["Jaylyn Clark",0,0,224.37608904518],
    # ["Karah Coombes",6,0.140307239512822,238.37442960291],
    # ["Chhun Manglona",4,0.251895926287639,250.18028904082],
    # ["Haley Morrow",4,0.167333730321508,241.38245973329],
    # ["Kevin Jackson",0,0,225.05824999256],
    # ["Tasneem Andrus",0,0,226.92101426716],
    # ["Andrew Mouanoutoua",4,0.268693874693911,251.57496038080],
    # ["Elizabeth Crowder",0,0,226.37467187563],
    # ["Eric Little",0,0,224.90612913065],
    # ["Majdi Vea",0,0,224.83762494099],
    # ["Mahmood Longwolf",0,0,223.54628891844],
    # ["Tahani Hennessy",0,0,224.37656914745],
    # ["Mikal Zhen",0,0,226.13375354187],
    # ["Adeeba Madril",0,0,223.57967857840],
    # ["Ghaazi Rausch",3,0.0481611063916552,230.63799192102],
    # ["Maria el-Kaiser",8,0.229587386497619,247.24336374182],
    # ["Shea el-Fahmy",3,0.0161670942904723,226.70207401862],
    # ["Aqeel Lobato",0,0,224.66452351406],
    # ["Isaac Garcia",6,0.187845837490405,244.25063605044],
    # ["Mubarak Turner",0,0,224.96367341768],
    # ["Maya Williams",0,0,225.04736009211]]
    # with open("C:/Users/leong/downloads/sachack/webapp/cheers/fandata.csv", mode='r') as csv_file:
    #         df = pandas.read_csv(csv_file, delimiter = ",")
    #         add = []
    #         i+=1
    #         for row in df:
    #             add.append(row)
    #         wholetable.append(add)
    # context = {'latest_question_list': latest_question_list}

    context = {'table' : wholetable, 'data': data}
    # context = {'table': [[s, "cats", "are dumb"], ["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"], ["chocolate", "cats", "are dumb"]],
    #             'chicken': ["meow"]}
    return render(request, 'cheers/index.html', context)

def main(request):
    context = {'bands': ["1","2","3","4","5","6","7","8","5654","6","5478","647","545r","436","547","5476","54","754","yrf","hf","hre","tre","tre","yre","ytr","y64","754","543","7657","535","2","5437","56u","y","r","htru","t4y","436","246","426","42"]}
    return render(request, 'cheers/main.html', context)
