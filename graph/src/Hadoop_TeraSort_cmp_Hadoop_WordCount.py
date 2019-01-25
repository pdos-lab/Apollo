import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


benchmark1 = "Benchmark: Hadoop TeraSort"
benchmark2 = "Benchmark: Hadoop WordCount"
# WordCount 18G18U CPU_overall
t1 = "18G18U"  
benchmark1_a1 = "1547716515000,99.3168154972,0.366637543205,0.133328138014,0.179054757443,0.00416406412659 1547716520000,95.2634816817,3.85731054864,0.192165615881,0.687042153824,0.0 1547716525000,66.2952703177,28.7727687553,4.64259156717,0.276762198963,0.0126071608674 1547716530000,87.041688155,10.321068193,2.23637102605,0.396689225649,0.00418340026774 1547716535000,88.35790821,6.90358072912,3.9601176769,0.714328132619,0.0640652513484 1547716540000,84.6033491345,10.6275529897,3.34214591243,1.4155998527,0.0113521106457 1547716545000,84.4032307665,11.9981958902,2.10199436375,1.40928958928,0.0872893902745 1547716550000,77.2747854736,16.2141638201,1.84485701143,4.59067750142,0.0755161934339 1547716555000,97.2851300344,0.554448554388,1.32256962591,0.837851785278,0.0 1547716560000,99.8188951942,0.106167252682,0.0312250202957,0.0437125327832,0.0"
benchmark1_b1 = "1547716515000,40933652,5404940,2956628 1547716520000,40695060,5406168,3193992 1547716525000,38733584,5570448,4991188 1547716530000,38798668,5571924,4924628 1547716535000,38170852,5573072,5551296 1547716540000,37598820,5573380,6123020 1547716545000,38623428,5793296,4878496 1547716550000,39241892,6049772,4003556 1547716555000,39824504,6049436,3421280 1547716560000,26508840,4045356,2309284"
benchmark2_a1 = "1547716695000,98.2932643813,1.57728629171,0.196074353045,-0.0666250260254,0.0 1547716700000,92.8094981909,6.15722750133,0.928779075658,0.100310781562,0.00418445058164 1547716705000,76.5809570954,20.3374983972,2.80263797111,0.270544982721,0.00836155357665 1547716710000,75.1451175997,17.7352744762,4.38407549387,2.72594837805,0.00958405213724 1547716715000,70.3003361716,23.6759805178,5.10856236527,0.90163931405,0.0134816312774 1547716720000,84.1676076961,9.14825853484,2.22131854749,4.45186713673,0.0109480848695 1547716725000,90.1877328368,4.66626369989,4.46574484828,0.676081505585,0.00417710944027 1547716730000,94.3512040976,2.12150528214,2.47725491951,1.05003570078,0.0 1547716735000,89.4100798797,3.24438442579,4.65807863861,2.67570548412,0.0117515717727 1547716740000,83.4041952614,9.35347665118,6.84094849853,0.274917369507,0.126462219412 1547716745000,80.51499409,14.7610223282,4.56386851056,0.147289625529,0.0128254456842 1547716750000,86.5153920606,10.3982641445,3.04041556667,0.0416541760346,0.00427405222892 1547716755000,92.7804044323,6.57358476586,0.537693217465,0.104138903991,0.00417868037274 1547716760000,95.6340538816,3.57317220413,0.554995883664,0.221090495752,0.0166875348382"
benchmark2_b1 = "1547716695000,37795632,7938168,3561420 1547716700000,37245240,7939820,4110160 1547716705000,36198876,7940096,5156248 1547716710000,36788944,7940508,4565768 1547716715000,35815964,7942020,5537236 1547716720000,34999016,7942944,6353260 1547716725000,34356376,7943208,6995636 1547716730000,34509516,7943128,6842576 1547716735000,34250460,7943180,7101580 1547716740000,34464852,7943224,6887144 1547716745000,34350852,7943052,7001316 1547716750000,35707044,7943044,5645132 1547716755000,36019616,7942752,5332852 1547716760000,37583144,7941336,3770740"
# WordCount 24G24U CPU_overall
t2 = "24G24U"
benchmark1_a2 = "1547800075000,99.8584317013,0.0874417060927,0.0499625284937,0.0,0.00416406412659 1547800080000,97.8787206715,0.0749791856646,1.47950374709,0.566796395771,0.0 1547800085000,99.3045263743,0.083283884421,0.599697028698,0.0124927126277,0.0 1547800090000,96.1877587826,2.43754491658,1.05391780393,0.320778496909,0.0 1547800095000,82.9818860996,15.852797846,1.11499208495,0.0461295145194,0.00419445493058 1547800100000,81.1972709854,17.0519007028,1.32022140353,0.405530108086,0.0250768001569 1547800105000,71.4845614574,20.3941742589,7.7348532642,0.298214362019,0.0881966575428 1547800110000,86.4657914476,2.12447485182,10.0344388776,1.36695470387,0.00834011910297 1547800115000,89.8609394581,0.345421953353,8.73902339544,1.05039738548,0.00421780758362 1547800120000,84.0691342724,4.24994524981,11.6635450655,0.0173754123235,0.0 1547800125000,91.7782295317,0.201300483064,7.78494104312,0.231536926148,0.00399201596806 1547800130000,87.322495411,4.37623003686,8.15440314235,0.138505659168,0.00836575061697 1547800135000,82.0747517921,10.6779603016,6.86435810498,0.382929801253,0.0 1547800140000,78.1942603034,16.7789385304,4.89979986602,0.122732721159,0.00426857899005 1547800145000,73.0834529922,13.7905688169,12.6813189118,0.229019603029,0.215639676059 1547800150000,68.9456463569,15.4465139574,15.0389609066,0.568878779106,0.0 1547800155000,94.3388782775,3.39067453996,2.11405784875,0.152160825196,0.00422850860502 1547800160000,91.9847985541,4.43261963669,3.02263736371,0.551587074122,0.00835737138386"
benchmark1_b2 = "1547800075000,36601108,9552064,3142048 1547800080000,37218516,8945804,3130900 1547800085000,37317612,8843204,3134404 1547800090000,37129520,8843732,3321968 1547800095000,35966376,8845072,4483772 1547800100000,36663328,9169552,3462340 1547800105000,34909476,9474564,4911180 1547800110000,36284796,9367808,3642616 1547800115000,36255612,9367812,3671796 1547800120000,36151428,9367820,3775972 1547800125000,36140864,9367824,3786532 1547800130000,36070980,9407492,3816748 1547800135000,36035928,9407492,3851800 1547800140000,35984448,9407504,3903268 1547800145000,35821004,9446604,4027612 1547800150000,36002372,9446452,3846396 1547800155000,35943256,9486900,3865064 1547800160000,36139484,9536192,3619544"
benchmark2_a2 = "1547731215000,97.3169393279,1.77448441082,0.262951039257,0.645625221979,0.0 1547731220000,93.7924265328,3.16568788834,0.769263767368,2.27262181151,0.0 1547731225000,70.6182565104,27.7741939293,1.54058572754,0.054369374237,0.0125944584383 1547731230000,76.6809053617,22.9506409864,0.33084675752,0.0166583439986,0.0209485503603 1547731235000,88.9396777157,10.7681779655,0.212841930608,0.075137803765,0.00416458437448 1547731240000,80.0027377429,15.0345629215,4.9332163019,0.0294830336701,0.0 1547731245000,90.6351178592,6.49878108733,2.54397033615,0.301107596559,0.0210231207344"
benchmark2_b2 = "1547731215000,35898028,9824028,3573164 1547731220000,35773020,9824368,3697832 1547731225000,33029456,9826516,6439248 1547731230000,32929836,9826536,6538848 1547731235000,35767404,9825308,3702508 1547731240000,34619632,9827188,4848400 1547731245000,35762776,9827388,3705056"
# WordCount 30G30U CPU_overall
t3 = "30G30U"
benchmark1_a3 = "1547796040000,98.9455206603,0.104179189709,0.921122541761,0.0250093785169,0.00416822975282 1547796045000,95.9400856189,1.555988353,1.99086530769,0.513060720447,0.0 1547796050000,96.1800554069,1.90164989338,1.80573836377,0.112556335977,0.0 1547796055000,95.0549800045,0.978143065639,3.89179679758,0.0750801322929,0.0 1547796060000,87.7044088327,7.19417010169,5.08881598091,0.0126050847318,0.0 1547796065000,83.2061851825,3.93699045899,11.5434728969,1.30913951652,0.00421194507624 1547796070000,79.1780289086,7.90779678035,12.6394506861,0.262203279377,0.0125203455615 1547796075000,68.7623962552,19.746503353,9.85817684815,1.61605347704,0.0168700666955 1547796080000,75.4520091731,3.14858414532,20.1344496171,1.25178225352,0.0131748109817 1547796085000,72.5928876104,3.85486194751,23.127527262,0.419930465004,0.00479271507309 1547796090000,74.0920891844,7.6497246129,17.9918550866,0.261723882771,0.00460723335637 1547796095000,79.5961783666,1.31373796288,17.8161652489,1.19221907527,0.0816993464052 1547796100000,78.8159524245,3.7618137676,16.053040176,1.36502070587,0.00417292605575 1547796105000,76.8373771929,13.6379256608,9.11815053533,0.302966468899,0.103580142095 1547796110000,90.4788303525,6.00328216056,2.89592107825,0.588471453463,0.0334949552192"
benchmark1_b3 = "1547796040000,32940804,12382800,3971616 1547796045000,33207704,12007080,4080436 1547796050000,33110996,12007104,4177120 1547796055000,33087296,12007108,4200816 1547796060000,32419104,12008500,4867616 1547796065000,32271416,12008980,5014824 1547796070000,32600920,12170760,4523540 1547796075000,31107608,12173020,6014592 1547796080000,30540140,12173056,6582024 1547796085000,30518960,12173084,6603176 1547796090000,30243696,12214928,6836596 1547796095000,30145292,12237176,6912752 1547796100000,29654480,12260540,7380200 1547796105000,30038012,12755352,6501856 1547796110000,32381072,12674572,4239576"
benchmark2_a3 = "1547796245000,97.9215078126,1.82395761704,0.246186628155,0.00834794223224,0.0 1547796250000,93.5860742178,5.4405832606,0.752191348989,0.221151172628,0.0 1547796255000,70.7930421935,27.7059356439,0.992858703297,0.4872149089,0.0209485503603 1547796260000,78.9496836565,20.6538634485,0.212953331628,0.175144297437,0.00835526590634 1547796265000,85.2193015144,13.5590345441,0.895247342712,0.322230571768,0.00418602704173 1547796270000,84.0647738257,14.125924977,1.34000532501,0.456638858313,0.0126570139117"
benchmark2_b3 = "1547796245000,31753040,13427044,4115136 1547796250000,31294424,13428616,4572180 1547796255000,28882388,13429540,6983292 1547796260000,28871292,13429576,6994352 1547796265000,30989768,13429592,4875860 1547796270000,31635088,13429828,4230304"
# WordCount 36G36U CPU_overall
t4 = "36G36U"
benchmark1_a4 = "1547773885000,98.3982146203,0.325705106721,1.2718784158,0.0,0.00420185722089 1547773890000,95.6883774932,4.07793589945,0.217013136894,0.0166734704154,0.0 1547773895000,72.9105227316,20.1091446747,5.93229247388,1.03962686051,0.00841325929665 1547773900000,66.0897007804,26.7253439365,7.03060798932,0.13324372605,0.0211035678036 1547773905000,82.115434367,5.00974346145,12.12727545,0.747546721509,0.0 1547773910000,84.3170321265,3.70159149665,11.9478287274,0.0293820241882,0.00416562526035 1547773915000,76.9191189008,11.5841360246,11.4163574091,0.0627373474479,0.0176503181148 1547773920000,88.8377058262,2.98794371175,7.8874506288,0.261383119799,0.0255167134473 1547773925000,81.2826603419,15.4716591943,2.6818635308,0.450363610654,0.113453322421"
benchmark1_b4 = "1547773885000,36875028,8593324,3826868 1547773890000,36617232,8593856,4084132 1547773895000,34676932,8756900,5861388 1547773900000,34987884,8759092,5548244 1547773905000,34540804,8759708,5994708 1547773910000,33931064,8759956,6604200 1547773915000,33895248,8800380,6599592 1547773920000,33719096,8905992,6670132 1547773925000,35942192,9235380,4117648"
benchmark2_a4 = "1547774070000,98.9591139978,0.0749437921559,0.104088600217,0.861853609793,0.0 1547774075000,94.9053274133,4.50778201637,0.536693356675,0.050197213622,0.0 1547774080000,81.8866030372,16.9413124114,1.12626149625,0.0416354504877,0.00418760469012 1547774085000,72.5862397486,25.7978300485,0.708049025211,0.882736596325,0.0251445813427 1547774090000,81.9551144056,17.6438784083,0.292413682438,0.108593503668,0.0 1547774095000,83.7571497269,13.6192789645,2.31748040546,0.297723043913,0.00836785915487 1547774100000,87.7047320028,8.01184269696,3.98448748143,0.286295593782,0.0126422250316"
benchmark2_b4 = "1547774070000,35465244,9948624,3881352 1547774075000,35202760,9949408,4143052 1547774080000,34067872,9950948,5276400 1547774085000,32367380,9951916,6975924 1547774090000,35189128,9951204,4154888 1547774095000,34497972,9952404,4844844 1547774100000,35193040,9951816,4150364"
# WordCount 42G42U CPU_overall
t5 = "42G42U" 
benchmark1_a5 = "1547775955000,99.120650766,0.587678293385,0.254197997389,0.0374729432074,0.0 1547775960000,95.6201429697,3.8586131671,0.467016597705,0.0542272654721,0.0 1547775965000,66.6185924429,30.9191715265,2.07584129122,0.352777756212,0.0336169831176 1547775970000,85.0127872934,11.1824043784,3.37791654289,0.405960066171,0.0209317191969 1547775975000,76.7385051112,17.5109279831,5.51532820739,0.134494707305,0.10074399098 1547775980000,90.9414204536,2.30837209981,6.61626441414,0.041757823946,0.0921852084643 1547775985000,90.0404853696,4.69541238136,5.14153449482,0.109828900754,0.0127388535032"
benchmark1_b5 = "1547775955000,37300500,8938076,3056644 1547775960000,37386480,8623800,3284940 1547775965000,35915220,8950164,4429836 1547775970000,36023160,9020580,4251480 1547775975000,36151632,9148084,3995504 1547775980000,35886336,9269512,4139372 1547775985000,36546200,9265476,3483544"
benchmark2_a5 = "1547776095000,97.9304011698,1.81931446459,0.241958317555,0.0083260480413,0.0 1547776100000,94.5300687736,3.46492535899,1.74081938687,0.255796514921,0.00838996560114 1547776105000,72.632903836,22.608609331,4.0372145939,0.716888004801,0.00438423429348 1547776110000,81.6620569517,0.624593107847,16.0638518889,1.64949805155,0.0 1547776115000,71.8127731398,3.08337163277,24.4062390955,0.686859974046,0.0107561579004 1547776120000,75.26465813,7.67300425853,16.8576147831,0.20472282831,0.0 1547776125000,71.2639867274,14.2451789674,14.3409450856,0.140372207925,0.00951701165834 1547776130000,64.9422244693,16.7797109337,18.1432548522,0.11750198002,0.0173077647901 1547776135000,63.9465832961,16.3922294766,19.6051348254,0.0415352832536,0.0145171185803 1547776140000,68.3298054974,25.7976223046,5.53820783658,0.31649605087,0.0178683105512 1547776145000,64.2880230102,23.5285245738,12.1124926987,0.0709597173073,0.0 1547776150000,81.8442339138,15.3492864356,2.4457692195,0.339112486171,0.021597944942"
benchmark2_b5 = "1547776095000,35799592,9978432,3517196 1547776100000,35524876,9979376,3790968 1547776105000,33757904,9980520,5556796 1547776110000,33598632,9980532,5716056 1547776115000,33525936,9980536,5788748 1547776120000,33404556,9980540,5910124 1547776125000,33393196,9980468,5921556 1547776130000,32235164,9982892,7077164 1547776135000,32214044,9982948,7098228 1547776140000,32278308,9982624,7034288 1547776145000,31789244,9983244,7522732 1547776150000,35181880,9981792,4131548"
# WordCount 48G48U CPU_overall
t6 = "48G48U" 
benchmark1_a6 = "1547780100000,98.2986319063,1.23479253329,0.241781580956,0.224793979487,0.0 1547780105000,92.5290808447,4.96748837628,2.32826112125,0.171002470212,0.00416718756511 1547780110000,73.454878292,16.7330302772,8.20380172252,1.59986179981,0.00842790851965 1547780115000,77.2226695355,15.2900785352,6.77665096094,0.693545816113,0.0170551522527 1547780120000,71.9654253984,23.7874096553,3.96755304148,0.169646984507,0.109964920315 1547780125000,83.7927957414,11.4789793641,4.47087988834,0.202706087426,0.0546389187885"
benchmark1_b6 = "1547780100000,32766544,12165072,4363604 1547780105000,32985720,11537500,4772000 1547780110000,31437084,11537944,6320192 1547780115000,31264128,11807828,6223264 1547780120000,31070488,12148324,6076408 1547780125000,32619844,12177452,4497924"
benchmark2_a6 = "1547780215000,98.3561917498,1.43524278235,0.175186238072,0.0333792297743,0.0 1547780220000,93.2566519754,6.05410351177,0.639242826812,0.0500016859778,0.0 1547780225000,70.1038326881,27.8154312765,1.01793839149,1.04184909355,0.0209485503603 1547780230000,79.8379491217,19.6314236952,0.154579341489,0.367690480924,0.00835736074548 1547780235000,81.3304359838,14.1384835949,0.927816819731,3.59908125108,0.00418235048097 1547780240000,84.3171001967,14.368095458,1.16761368781,0.134610236571,0.0125804209362"
benchmark2_b6 = "1547780215000,32021448,12891576,4382196 1547780220000,31462488,12891624,4941108 1547780225000,29107876,12893200,7294144 1547780230000,29098248,12893212,7303760 1547780235000,31234900,12893584,5166736 1547780240000,31863936,12894456,4536828"

plt.figure(1)
plt.suptitle(benchmark1, color="blue")
benchmark1_t = []
for i in range(1,7):
    a = locals()['benchmark1_a'+str(i)].split(" ")
    x = []
    y_a = []
    l = 0   
    for n in a:   
        l = l + 1        
        m = n.split(",")          
        x.append(5*int(l))
        y_a.append(float('%.2f' % (float(m[2])+float(m[3]))))
    benchmark1_t.append(x[-1])
    b = locals()['benchmark1_b'+str(i)].split(" ")
    x = []
    y_b = []
    l = 0  
    for n in b:   
        l = l + 1        
        m = n.split(",")          
        x.append(5*int(l))
        y_b.append(float('%.2f' % (float(m[2])+float(m[3]))) / float('%.2f' % (float(m[1]) + float(m[2]) + float(m[3]))) * 100)
    locals()['ax'+str(i)] = plt.subplot(2,3,i)
    locals()['ax'+str(i)].set_title(locals()['t'+str(i)])
    x_axix, y_axix = (x, y_a)
    plt.plot(x_axix, y_axix, linewidth = '2', color='black', marker='x', label='CPU')
    x_axix, y_axix = (x, y_b)
    plt.plot(x_axix, y_axix, linewidth = '2', color='red', marker='o', label='RAM')
    
    ax = plt.gca()
    ax.set_ylim(0,100)
    if (i>3):
        plt.xlabel('time(sec)', fontsize=12)
    if (i==1 or i==4):
        plt.ylabel('resource usage(%)', fontsize=12)
    plt.legend()
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
plt.subplots_adjust(wspace=0.3, hspace=0.3)
# plt.show()
print(benchmark1_t)

benchmark2_t = []
plt.figure(2)
plt.suptitle(benchmark2, color="blue")
for i in range(1,7):
    a = locals()['benchmark2_a'+str(i)].split(" ")
    x = []
    y_a = []
    l = 0   
    for n in a:   
        l = l + 1        
        m = n.split(",")          
        x.append(5*int(l))
        y_a.append(float('%.2f' % (float(m[2])+float(m[3]))))
    benchmark2_t.append(x[-1])
    b = locals()['benchmark2_b'+str(i)].split(" ")
    x = []
    y_b = []
    l = 0  
    for n in b:   
        l = l + 1        
        m = n.split(",")          
        x.append(5*int(l))
        y_b.append(float('%.2f' % (float(m[2])+float(m[3]))) / float('%.2f' % (float(m[1]) + float(m[2]) + float(m[3]))) * 100)
    locals()['ax'+str(i)] = plt.subplot(2,3,i)
    locals()['ax'+str(i)].set_title(locals()['t'+str(i)])
    x_axix, y_axix = (x, y_a)
    plt.plot(x_axix, y_axix, linewidth = '2', color='black', marker='x', label='CPU')
    x_axix, y_axix = (x, y_b)
    plt.plot(x_axix, y_axix, linewidth = '2', color='red', marker='o', label='RAM')
    
    ax = plt.gca()
    ax.set_ylim(0,100)
    if (i>3):
        plt.xlabel('time(sec)', fontsize=12)
    if (i==1 or i==4):
        plt.ylabel('resource usage(%)', fontsize=12)
    plt.legend()
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
plt.subplots_adjust(wspace=0.3, hspace=0.3)
print(benchmark2_t)

plt.figure(3,figsize=(12, 6))
plt.suptitle("Configuration-performance curve", color="green")
x = []
for i in range(1,7):
    x.append(locals()['t'+str(i)])
ax1 = plt.subplot(1,2,1)
ax1.set_title(benchmark1)
y_a = benchmark1_t
x_axix, y_axix = (x, y_a)
plt.plot(x_axix, y_axix, linewidth = '2', color='black', marker='x')
ax = plt.gca()
ax.set_ylim(0,100)
plt.xlabel('configuration', fontsize=12)
plt.ylabel('job running time (sec)', fontsize=12)
plt.legend()
ax1 = plt.subplot(1,2,2)
ax1.set_title(benchmark2)
y_b = benchmark2_t
x_axix, y_axix = (x, y_b)
plt.plot(x_axix, y_axix, linewidth = '2', color='black', marker='x')
ax = plt.gca()
ax.set_ylim(0,100)
plt.xlabel('configuration', fontsize=12)
plt.ylabel('job running time (sec)', fontsize=12)
plt.legend()

plt.show()