import csv
import os
import threading
from time import sleep
from datetime import datetime
from plyer import notification
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


# ^^^^^^^^^^^^^^^^^^^^The function for search values^^^^^^^^^^^^^^^^^^^^
def tellsDay():
    dt = datetime.now()
    day = dt.weekday()
    
    Monday = ["Muhammad Ali", "Mike Tyson", "Sugar Ray Robinson", "Joe Louis", "Rocky Marciano", "Jack Dempsey", "Joe Frazier", "George Foreman", "Lennox Lewis", "Evander Holyfield", "Floyd Mayweather Jr.", "Manny Pacquiao", "Oscar De La Hoya", 
              "Roy Jones Jr.", "Bernard Hopkins", "Marvin Hagler", "Thomas Hearns", "Roberto Duran", "Julio Cesar Chavez Sr.", "Pernell Whitaker", "Aaron Pryor", "Wilfred Benitez", "Salvador Sanchez", "Alexis Arguello", "Eusebio Pedroza", "Azumah Nelson",
              "Kostya Tszyu", "Arturo Gatti", "Miguel Cotto", "Juan Manuel Marquez", "Marco Antonio Barrera", "Erik Morales", "Ricardo Lopez", "Michael Carbajal", "Felix Trinidad","Vasyl Lomachenko","Gennady Golovkin","Terence Crawford","Canelo Alvarez",
              "Anthony Joshua","Deontay Wilder","Tyson Fury","Andy Ruiz Jr.","Manny Pacquiao","Errol Spence Jr.","Keith Thurman","Shawn Porter","Danny Garcia","Mikey Garcia","Vergil Ortiz Jr.","Teofimo Lopez","Ryan Garcia"]



    Tuesday = ["Hero Cycles", "Atlas Cycles", "Avon Cycles", "Firefox Bikes", "Bianchi", "Cannondale", "Giant Bicycles", "GT Bicycles", "Haro Bikes", "Kona Bikes", "Merida Bikes", "Pinarello", "Raleigh Bicycles", "Santa Cruz Bicycles", "Schwinn Bicycles",
               "Scott Sports", "Specialized Bicycle Components", "Trek Bicycle Corporation", "Yeti Cycles", "Cervelo","BMC","Colnago","De Rosa","Felt","Fuji","Look","Orbea","Salsa Cycles","Soma Fabrications","Surly Bikes","Wilier Triestina",
               "Canyon Bicycles","Cinelli","Diamondback Bicycles","Electra Bicycle Company","Foes Racing","Ibis Cycles","Jamis Bicycles","Litespeed Bicycle Company","Moots Cycles","Niner Bikes","Pivot Cycles","Rocky Mountain Bicycles","Salsa Cycles"]



    Wednesday = ["Cryptocurrency", "NFTs", "Climate change", "Artificial intelligence", "Virtual reality", "Augmented reality", "Electric vehicles", "Self-driving cars", "Cybersecurity", "Quantum computing", "Space exploration", "Renewable energy", 
                 "Mental health awareness", "Social media marketing", "Influencer marketing", "E-commerce", "Online education", "Remote work", "Health and wellness", "Sustainable fashion", "Plant-based diets and veganism", "Mindfulness and meditation",
                 "Personal finance and investing", "Gaming and esports", "Streaming services like Netflix and Amazon Prime Video","Artificial general intelligence","Internet of Things (IoT)","Big data and analytics","Blockchain technology","Cloud computing",
                 "5G technology","Robotics and automation","Biotechnology and gene editing","Nanotechnology","Wearable technology","Smart homes and home automation","Digital privacy and security","Data science and machine learning","Digital transformation",
                 "Industry 4.0 and smart factories","Circular economy and sustainability","Smart cities and urban planning","Autonomous drones and vehicles","Quantum cryptography and communication","Edge computing and fog computing",
                 "Human-computer interaction (HCI)","Natural language processing (NLP)","Computer vision and image recognition","Cyber-physical systems (CPS)","Digital twins and simulation modeling"]



    Thursday = ['Acanthurus coeruleus', 'Acanthurus leucosternon', 'Acanthurus lineatus', 'Acanthurus nigricans', 'Acanthurus olivaceus', 'Acanthurus pyroferus', 'Amphiprion bicinctus', 'Amphiprion chrysopterus', 'Amphiprion clarkii', 
                'Amphiprion ocellaris', 'Amphiprion percula', 'Anampses caeruleopunctatus', 'Anampses femininus', 'Anampses meleagrides', 'Anampses twistii', 'Apolemichthys griffisi', 'Apolemichthys xanthurus', 'Balistapus undulatus', 
                'Canthigaster valentini', 'Centropyge bicolor', 'Centropyge eibli', 'Centropyge ferrugatus', 'Centropyge flavicauda', 'Centropyge heraldi', 'Centropyge loriculus', 'Centropyge multicolor', 'Chaetodon auriga', 'Chaetodon baronessa', 
                'Chaetodon capistratus', 'Chaetodon citrinellus', 'Chaetodon collare', 'Chaetodon falcula', 'Chaetodon kleinii', 'Chaetodon lunula', 'Chaetodon miliaris', 'Chaetodon ocellatus', 'Chaetodon ornatissimus', 'Chaetodon pelewensis', 
                'Chaetodon quadrimaculatus', 'Chaetodon rafflesi', 'Chaetodon semilarvatus','Chelmon rostratus','Chromis cyanea','Chrysiptera cyanea','Chrysiptera parasema','Cirrhilabrus exquisitus','Cirrhilabrus jordani','Cirrhilabrus lubbocki',
                'Cirrhilabrus roseafascia','Cirrhilabrus solorensis','Ctenochaetus striatus','Dascyllus aruanus','Dascyllus melanurus','Dascyllus reticulatus','Ecsenius bicolor','Ecsenius midas']



    Friday = ["African Butterflyfish","African Glass Catfish","African Lungfish","African Tiger Fish",    "Arowana","Bala Shark","Banjo Catfish","Barbs","Bettas","Black Ghost Knifefish", "Blue Gourami","Blue-Eyed Pleco","Bolivian Ram Cichlid",
              "Bristlenose Pleco","Butterfly Pleco","Cardinal Tetra","Celestial Pearl Danio (Galaxy Rasbora)","Cherry Barb","Cherry Shrimp","Chinese Algae Eater","Clown Loach","Congo Tetra","Corydoras Catfish (Cory Cats)","Discus Fish","Dwarf Gourami",
              "Electric Eel (South American)","Electric Yellow Cichlid (Labidochromis caeruleus)","Endler's Livebearer (Endler's Guppy)","Featherfin Squeaker (Synodontis eupterus)","Firemouth Cichlid (Thorichthys meeki)","Flowerhorn Cichlid (Luo Han fish)"
              ,"Freshwater Angelfish (Pterophyllum scalare)","Freshwater Barracuda (Acestrorhynchus falcatus)","Freshwater Dolphin Fish (Mormyrus longirostris)","Freshwater Flounder (Archirus lineatus)","Freshwater Garfish (Atractosteus tropicus)",
              "Freshwater Hatchetfish (Carnegiella strigata)","Freshwater Lionfish (Pterois antennata)","Freshwater Moray Eel (Gymnothorax tile)","Freshwater Pipefish (Microphis brachyurus)","Freshwater Pufferfish (Tetraodon fluviatilis)",
              "Giant Danio (Devario aequipinnatus)","Glass Catfish (Kryptopterus bicirrhis)","Glowlight Tetra (Hemigrammus erythrozonus)","Gold Barb","Gold Nugget Pleco (Baryancistrus sp.)","Golden Wonder Killifish (Aplocheilus lineatus)",
              "Gouramis","Green Terror Cichlid (Andinoacara rivulatus)","Hillstream Loach (Beaufortia kweichowensis)","Kissing Gourami (Helostoma temminckii)","Kribensis Cichlid (Pelvicachromis pulcher)","Lemon Tetra (Hyphessobrycon pulchripinnis)","Loaches","Mollies"]



    Saturday = ["Vitamin C", "Vitamin D", "Calcium", "Iron", "Magnesium", "Zinc", "Folate", "Vitamin B12", "Vitamin B6", "Vitamin E", "Vitamin A", "Vitamin K", "Thiamin (B1)", "Riboflavin (B2)", "Niacin (B3)", "Pantothenic acid (B5)", "Biotin (B7)",
                "Choline", "Chromium", "Copper", "Iodine", "Manganese", "Molybdenum", "Selenium", "Phosphorus", "Potassium", "Sodium", "Chloride", "Fluoride", "Omega-3 fatty acids (EPA and DHA)", "Probiotics and prebiotics", "Collagen peptides", 
                "Creatine monohydrate", "Whey protein powder", "Casein protein powder", "Pea protein powder", "Hemp protein powder", "Rice protein powder", "Soy protein powder", "Multivitamins for men or women over 50 years old","Probiotics",
                "Turmeric","Ginger","Garlic","Cinnamon","Ashwagandha","Milk thistle","Berberine","CoQ10","Fish oil","Magnesium glycinate","Melatonin"]



    Sunday = ["Kawasaki Ninja 400","KTM Duke 390","Yamaha YZF-R3","Kawasaki Ninja 650","Yamaha MT-03","KTM RC 390","Honda CBR500R","Yamaha MT-07","Kawasaki Z650","Suzuki SV650","Triumph Street Triple R","KTM 390 Adventure","Yamaha XSR700"
              ,"Kawasaki Z900","Honda CB500F","Suzuki V-Strom 650","Triumph Tiger 800","Yamaha Tracer 900","Kawasaki Ninja 1000SX","Honda CBR650R","BMW F 750 GS","Suzuki SV650X","Triumph Bonneville T120","KTM 690 SMC R","Ducati Monster 821"
              ,"Yamaha MT-09","Kawasaki Z900RS","Honda CB650R","Suzuki V-Strom 1050","Triumph Tiger 900","KTM 790 Duke","Ducati Scrambler 800","Yamaha Tracer 700","Kawasaki Versys 1000","BMW F 850 GS","Suzuki GSX-S750","Triumph Bonneville Speedmaster"
              ,"Honda CBR1000RR","Yamaha MT-10","KTM 890 Duke R","Ducati Monster 939","Kawasaki Z1000","BMW S 1000 XR","Suzuki GSX-S1000","Triumph Tiger 1200","Ducati Multistrada 950","Yamaha Tracer 900 GT","KTM 1290 Super Duke R","Honda CB1000R",
              "Kawasaki Ninja H2 SX","BMW R 1250 GS","Ducati Panigale V2","Suzuki GSX-S1000F","Yamaha MT-10 SP","Triumph Rocket 3","KTM 1290 Super Adventure","Royal Enfield Himalayan"]



    match day:
        case 0:
            return Monday
        case 1:
            return Tuesday
        case 2:
            return Wednesday
        case 3:
            return Thursday
        case 4:
            return Friday
        case 5:
            return Saturday
        case 6:
            return Sunday
        
TheWordsList = tellsDay()

# Checks if a web element exists or not in the driver webpage

def check_exists_by_linktext(xpath, driver):
    try:
        driver.find_element(By.LINK_TEXT, xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_CSSselector(cssseletor, driver):
    try:
        driver.find_element(By.CSS_SELECTOR, cssseletor)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_ID(id, driver):
    try:
        driver.find_element(By.ID, id)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_ClassName(clsaa, driver):
    try:
        driver.find_element(By.CLASS_NAME, clsaa)
    except NoSuchElementException:
        return False
    return True


def TurnsOnMobileView(driver, choose):
    driver.get("chrome-extension://djflhoibgkdhkhhcedjiklpkjnoahfmg/popup.html")
    sleep(1.5)
    if (choose == 1):
        driver.find_element(By.ID, "ua_row_2").click()
        sleep(1.5)
        driver.find_element(By.ID, "ua_row_c_11").click()
        sleep(3)
        url = "https://www.bing.com/search?q=kaisen"
        driver.get(url)
    if (choose == 2):
        driver.find_element(By.ID, "ua_row_0").click()
        sleep(1.5)
        driver.find_element(By.ID, "ua_row_c_1").click()
        sleep(3)
        url = "https://www.bing.com/search?q=jujutsu"
        driver.get(url)

def enter_sign_in_page(driver):
    try:
        # driver.find_element(By.ID, "id_s").click()
        driver.get("https://bing.com")
        sleep(5)
        i = 0
        while(i<4):
            if(check_exists_by_linktext("Sign in", driver) == True):
                driver.find_element(By.LINK_TEXT, "Sign in").click()
                break
            else:
                sleep(2)
                i = i+1           
    except Exception as e:
        print(e)
        enter_sign_in_page(driver)

def This_Signs_the_ids(driver, TheUser, HisPassword, IDNo):
    try:
        # The sign-in phase
        enter_sign_in_page(driver)
        
        sleep(5)
        while(driver.title != "Sign in to Bing"):
            enter_sign_in_page(driver)            

        if (check_exists_by_ID("i0116", driver) == True):
            element = driver.find_element(By.ID, "i0116")
            element.clear()
            element.send_keys(TheUser)
            driver.find_element(By.ID, "idSIButton9").click()
    
            if (check_exists_by_ID("usernameError", driver) == True):
                element = driver.find_element(By.ID, "i0116")
                element.clear()
                element.send_keys(TheUser)
                driver.find_element(By.ID, "idSIButton9").click()
        sleep(2)
        if(check_exists_by_ID("i0118", driver) == True):
            password = driver.find_element(By.NAME, "passwd")
            password.clear()
            password.send_keys(HisPassword)
            driver.find_element(By.ID, "idSIButton9").click()
            if(check_exists_by_ID("passwordError", driver) == True):
                password = driver.find_element(By.NAME, "passwd")
                password.clear()
                password.send_keys(HisPassword)
                driver.find_element(By.ID, "idSIButton9").click()
        sleep(2)
        if(check_exists_by_ID("idSIButton9", driver) == True):
            driver.find_element(By.ID, "idSIButton9").click()
        return True
    except StaleElementReferenceException :
        # print(sexcs)
        print("\n\nStaleElementReferenceException in the fuction This_Signs_The_ids\n\n")
        This_Signs_the_ids(driver, TheUser, HisPassword, IDNo)
    except NoSuchElementException:
        # print(nexcs)
        print("\n\nNoSuchElementException in the fuction This_Signs_The_ids\n\n")
        This_Signs_the_ids(driver, TheUser, HisPassword, IDNo)
    except Exception as excs :
        print(excs)
        print("\n\nSome exception in the fuction This_Signs_The_ids\n\n")
        return False
    #^^^^^^^^^^^ Here we have signed into the rewards website

def notifierofIds(user, idno, num):
    if (num == 1):
        notifTitle = "ID "+str(idno)+" has started."
        notifMessage = "The id "+user+". Kindly check the signup button."
    elif(num == 2):
        notifTitle = "ID "+str(idno)+" has ended."
        notifMessage = user+" --> Completed."
    elif(num == 3):
        notifTitle = "ID "+str(idno)+" Program Crashed"
        notifMessage = user+" --> The Program Crashed, Running it once again."
    elif(num == 4):
        notifTitle = "Check the terminal "
        notifMessage = "Waiting for input to turn on mobile mode"
    
    notification.notify(
        title = notifTitle,
        message = notifMessage,
        app_icon = None,
        app_name = "The Python Program",
        timeout = 10,
        toast = False
    )

dt = datetime.now()
ate = dt.date()
TheMainFile = open("DailyReports.txt", "a")
TheMainFile.write(str(ate)+"\n\n")
TheMainFile.close()

TheFileList = []


# Opens a new window and closes all other windows except the main one
def closes_all_except_one(driver):
    sleep(2)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("chrome://settings/")
    # driver.get("https://www.google.com")
    for tab in driver.window_handles:
        if(tab == driver.window_handles[0]):
            continue
        else:
            driver.switch_to.window(tab)
            sleep(1)
            driver.close()
    driver.switch_to.window(driver.window_handles[0])

def checks_for_true_values(a, b, valueslist):
    for value in range(a,b):
        if valueslist[value] == True:
            # False means to run it once again
            return False
    return True

with open('pwds002.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    count = 0
    useremailids = []
    passwordsofids = []
    runCountry = []
    for row in reader:
        count = count+1
        useremailids.append(row['The emails'])
        passwordsofids.append(row['The email passwords'])
        runCountry.append(row['Country'])


ToDoOrNotToDo = []

def idCluster(RangeStarts, RangeEnds, winSize):
        for ides in range(RangeStarts, RangeEnds):
            try:
                if(ToDoOrNotToDo[ides] == False):
                    continue
                
                # Initialising driver for chrome
                options = webdriver.ChromeOptions()
                options.add_experimental_option("detach", True)
                options.add_extension("vpn.crx")
                options.add_extension("ABS.crx")
                options.add_extension("mobileviewer.crx")

                driver = webdriver.Chrome(options=options)

                match winSize:
                        case 0:
                            options.add_argument("window-size=654,1087")
                            driver.set_window_position(-7, 0, windowHandle='current')
                        case 1:
                            options.add_argument("window-size=654,1087")
                            driver.set_window_position(633, 0, windowHandle='current')
                        case 2:
                            options.add_argument("window-size=654,1087")
                            driver.set_window_position(1273, 0, windowHandle='current')
                        case 3:
                            driver.maximize_window()
                        case 4:
                            driver.set_window_rect(-7, 0, 974, 1087)
                        case 5:
                            driver.set_window_rect(953, 0, 974, 1087)                        

                # Open a new window
                closes_all_except_one(driver)

                # # This one is for the french VPN
                if (runCountry[ides] == "france"):
                    driver.get("chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/html/foreground.html")
                    sleep(5)
                    # driver.refresh()
                    if (check_exists_by_ClassName("footer-decline-text", driver) == True):
                        driver.find_element(By.CLASS_NAME, "footer-decline-text").click()
                    while(True):
                        if(check_exists_by_ClassName("next", driver) == True):
                            continuebtn = driver.find_element(By.CLASS_NAME, "next")
                            continuebtn.click()
                            break
                        else:
                            sleep(1)
                    while(True):
                        if(check_exists_by_ClassName("next", driver) == True):
                            startbtn = driver.find_element(By.CLASS_NAME, "next")
                            startbtn.click()
                            break
                        else:
                            sleep(1)
                    while(True):
                        if(check_exists_by_CSSselector("div.current-region-upper-block",driver) == True):
                            driver.find_element(By.CSS_SELECTOR, "div.current-region-upper-block").click()
                            break
                        else:
                            sleep(2)
                    while(True):
                        if(check_exists_by_CSSselector("div.region-name-and-area",driver) == True):
                            driver.find_element(By.CSS_SELECTOR, "div.region-name-and-area").click()        
                            break
                        else:
                            sleep(2)
                    while(True):
                        if(check_exists_by_CSSselector("span.button-clicker",driver) == True):
                            driver.find_element(By.CSS_SELECTOR, "span.button-clicker").click()
                            break
                        else:
                            sleep(2)

                if (runCountry[ides] == "usa"):
                    driver.get("chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/html/foreground.html")
                    sleep(5)
                    # driver.refresh()
                    if (check_exists_by_ClassName("footer-decline-text", driver) == True):
                        driver.find_element(By.CLASS_NAME, "footer-decline-text").click()
                    while(True):
                        if(check_exists_by_ClassName("next", driver) == True):
                            continuebtn = driver.find_element(By.CLASS_NAME, "next")
                            continuebtn.click()
                            break
                        else:
                            sleep(1)
                    while(True):
                        if(check_exists_by_ClassName("next", driver) == True):
                            startbtn = driver.find_element(By.CLASS_NAME, "next")
                            startbtn.click()
                            break
                        else:
                            sleep(1)
                    while (True):
                        if(check_exists_by_CSSselector("div.current-region-upper-block",driver) == True):
                            driver.find_element(By.CSS_SELECTOR, "div.current-region-upper-block").click()
                            break
                        else:
                            sleep(1.5)
                    while (True):
                        if(check_exists_by_CSSselector("#region-list > div:nth-child(7) > div.region-folder-header > div > div.region-name-wrapper",driver) == True):
                            driver.find_element(By.CSS_SELECTOR, "#region-list > div:nth-child(7) > div.region-folder-header > div > div.region-name-wrapper").click()
                            break
                        else: 
                            sleep(1.5)
                    while (True):
                        if(check_exists_by_CSSselector("#region-list > div:nth-child(7) > div.rah-static.rah-static--height-specific > div > div:nth-child(1) > div.region-name-fav-wrapper > div > span:nth-child(2)", driver) == True):
                            driver.find_element(By.CSS_SELECTOR, "#region-list > div:nth-child(7) > div.rah-static.rah-static--height-specific > div > div:nth-child(1) > div.region-name-fav-wrapper > div > span:nth-child(2)").click()
                            break
                        else:
                            sleep(1.2)
                    while (True):
                        if(check_exists_by_CSSselector("span.button-clicker", driver) == True):
                            driver.find_element(By.CSS_SELECTOR, "span.button-clicker").click()
                            break
                        else:
                            sleep(1)

                sleep(4)
                
                for tab in driver.window_handles:
                    if(tab == driver.window_handles[0]):
                        continue
                    else:
                        driver.switch_to.window(tab)
                        sleep(1)
                        driver.close()
                driver.switch_to.window(driver.window_handles[0])
                #^^^^^^^^^^^ Here we have signed into the rewards website

                if (This_Signs_the_ids(driver, useremailids[ides], passwordsofids[ides], ides) == True):

                    fname = "toDelete0"+str(winSize)+".txt"
                    if fname not in TheFileList:
                        TheFileList.append(fname)

                    TheTemporryFile = open(fname, "a")
                    theSent = "\t\t\t"+str(ides+1)+" > Id "+useremailids[ides]+" -- signin successfull."
                    TheTemporryFile.write(theSent+"\n\n")
                    TheTemporryFile.close()

                    notifierofIds(useremailids[ides], ides, 1)
                    # sleep(5)
                    # ^^^^^^^^^^^^^^^^^^^^The searching starts from here^^^^^^^^^^^^^^^^^^^^
                    # ^^^^^^^^^^^^^^^^^^^^The searching starts from here^^^^^^^^^^^^^^^^^^^^
                    # ^^^^^^^^^^^^^^^^^^^^The searching starts from here^^^^^^^^^^^^^^^^^^^^

                    url1 = "https://www.bing.com/search?q="+TheWordsList[0]
                    driver.get(url1)

                    for k in range(1, 30):
                        search_query = TheWordsList[k]
                        search_box = driver.find_element(By.NAME, "q")
                        sleep(0.7)
                        search_box.clear()
                        search_box.send_keys(search_query)
                        search_box.submit()

                    # notifierofIds(useremailids[ides], ides, 4)
                    # jk = str(input("Enter any number : "))
                    TurnsOnMobileView(driver, 1)
                    for kl in range(30, 50):
                        search_query = TheWordsList[kl]
                        search_box = driver.find_element(By.NAME, "q")
                        sleep(0.7)
                        search_box.clear()
                        search_box.send_keys(search_query)
                        search_box.submit()
                    TurnsOnMobileView(driver, 2)               

                    theSent = "\t\t\t\tId "+useremailids[ides]+" -- Ended successfully."
                    TheTemporryFile = open(fname, "a")
                    TheTemporryFile.write(theSent+"\n\n")
                    notifierofIds(useremailids[ides], ides, 2)
                    ToDoOrNotToDo[ides] = False
                    driver.quit()
                else:
                    driver.quit()
            except Exception as excs:
                driver.quit()
                print("\n\n\n\n\n\n\n\n",excs, "\n\n\n\n\n\n\n")
                continue


choice = int(input("Enter 1 to run all the ids or 2 to run specific ids : "))

if (choice == 1):
    for ides in range(0, len(useremailids)):
        ToDoOrNotToDo.append(True)
elif (choice == 2):
    print("Enter 1 to run the id, 0 to not run the id : ")
    for ides in range(0, len(useremailids)):
        STRNGGG = str(ides+1)+")For ID => "+useremailids[ides]+"  : "
        toRun = int(input(STRNGGG))
        if(toRun == 1):
            ToDoOrNotToDo.append(True)
            # True means the id needs to be run
        else:
            ToDoOrNotToDo.append(False)
            # False means all the id have been run properly
# elif (choice == 3):
    # checksbalance()
thread001 = threading.Thread(target=idCluster, args=[0,int(len(useremailids)/2),4])
thread002 = threading.Thread(target=idCluster, args=[int(len(useremailids)/2),int(len(useremailids)),5])

thread001.start()
thread002.start()

thread001.join()
thread002.join()


TheMainFile = open("DailyReports.txt", "a")
for fi in TheFileList:
    thred001 = open(fi, "r")
    linesInThred001 = thred001.readlines()
    thred001.close()
    TheMainFile.writelines(linesInThred001)
    TheMainFile.write("\n\n")
    
TheMainFile.write("Today's tasks are complete.\n\n")
TheMainFile.close()

for files in TheFileList:
    if os.path.exists(files):
      os.remove(files)
    else:
      print("The file does not exist")
      
      