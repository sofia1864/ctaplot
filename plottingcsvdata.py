#paragraph: my plot is interactive so it showcases multiple patterns & relationships between the variables average amount of rides on sunday, 
#saturday, weekdays, total week, and total month, though I will only choose to mention one pattern in this graph as I feel it is the most significant piece of data 
#that can be gathered from the graph. this pattern is the pattern between the average amount of rides taken during the week in relation to the average amount of rides 
#taken on Sundays and Saturdays as it really shows how trains are people's main way of transportation to get around during the weekends and shows how we as a society 
#have come to lean upon advanced technology such as trains to transport us places in not only our work lives but social as well, and suggests that weekend rides will continue 
#to be the majority of rides throughout the week.

import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
from matplotlib import pyplot as plt
import numpy as np

bar_showing = True

with open('tester.csv', 'r') as f: #reading the file
    data = f.read()
    row1 = f.readline() 
    row1 = row1.split(',')

lines = data.split('\n')

lines.pop(0)
lines.pop(-1)
 
avgsunrides = []
avgsatrides = []
avgweekdayrides = []
stationname = []
avgsunrides = []
avgweekrides = []
monthtotal = []
times = []

#categorizing data
for thing in lines:
    if thing: #conditional to check if it is a thing lol
        parts = thing.split(',')
        times.append(parts[2])
        stationname.append(parts[1])
        avgweekdayrides.append(float(parts[3]))
        avgsatrides.append(float(parts[4]))
        avgsunrides.append(float(parts[5]))
        monthtotal.append(float(parts[6]))
        avgweekrides.append(float(parts[3])+float(parts[4])+float(parts[5]))

#dictionary to get lists instead of the name
rides = { "avgsunrides": avgsunrides, "avgsatrides": avgsatrides, "avgweekdayrides": avgweekdayrides, "stationname": stationname, "avgweekrides": avgweekrides, "monthtotal": monthtotal, "times": times} #finish make dictionary
    
def yxvalues(): #letting the user selecting their x & y 
    value = []
    options = ["avgweekdayrides", "avgsatrides", "avgsunrides", "monthtotal", "avgweekrides"] #use rides dictionary
    value.append(input(f"What is your y value? Options: {options} "))
    xvalue = []
    options.remove(value[0])
    xvalue = str(input(f"Choose three x values and type them how you normally would (like so: monthtotal, avgweekrides). Options: {options} "))
    xvalue = xvalue.split(', ') 
    for i in xvalue:
        value.append(i)
    return value 

value = yxvalues()
dictconverted = [ rides[value[0]], rides[value[1]], rides[value[2]], rides[value[3]] ] 

width = 0.4

def graph(dictconverted, value):
    zero = value[0]
    one = value[1]
    two = value[2]
    three = value[3]
    ax1.set_title(f"CTA Ridership L Station Entries: {zero} vs {one}, {two}, and {three} (rides)")
    ax1.set_ylabel(zero + "(rides)")
    ax1.set_xlabel(f"{one}, {two} and {three} {rides}")
    leg = ax1.legend(loc='upper left')
    fig.canvas.draw()

def bar(val): #making a bar graph!
    ax1.clear()
    global dictconverted
    rects1 = ax1.bar(times, dictconverted[1], width, color='Yellow', label="one") 
    rects2 = ax1.bar(times, dictconverted[2], width, color='Green', bottom=dictconverted[1], label="two") #BUG: got color to work but bars aren't stacking the way I want them to
    rects3 = ax1.bar(times, dictconverted[3], width, color='Blue', bottom=dictconverted[2], label="three")
    ax1.set_xticks(ax1.get_xticks(), rotation=90)
    plt.draw()
    global bar_showing
    bar_showing = True
    graph(dictconverted, value)

def scatter(val): #making a scatter graph!
    ax1.clear()
    global dictconverted
    zero = dictconverted[0]
    for j in range(2, len(dictconverted)):
       i = dictconverted[j] 
       ax1.scatter(i, zero, marker='o') 
       #slope, intercept = np.polyfit(i, zero, 1) #find the slope of trendline
       #print(f"the slope of the trendline of the relationship between {i} and {zero} is, while its intercept is {intercept}")
       #trendpoly = np.poly1d(slope, intercept) #BUG: ???
       #ax1.plot(i, trendpoly(i), ls = 'dashed', color = 'blue') #making trendline 
    ax1.set_xticks(ax1.get_xticks(), rotation=90)
    plt.draw()
    global bar_showing
    bar_showing = False
    graph(dictconverted, value)

def updatexy(val):
    global dictconverted
    values = yxvalues()
    dictconverted = [ rides[value[0]], rides[value[1]], rides[value[2]], rides[value[3]] ] 
    if bar_showing:
        bar(value)
    else:
        scatter(value)

fig, ax1 = plt.subplots()
plt.subplots_adjust(left = 0.3, bottom = 0.25)
ax2 = plt.axes([0.41, 0.01, 0.1, 0.075])
ax3 = plt.axes([0.61, 0.01, 0.1, 0.075])
ax4 = plt.axes([0.81, 0.01, 0.1, 0.075])

barbutton = widgets.Button(ax2, 'Bar graph')
barbutton.on_clicked(bar)
scatbutton = widgets.Button(ax3, 'Scatterplot')
scatbutton.on_clicked(scatter)
xybutton = widgets.Button(ax4, 'Change x & y values') 
xybutton.on_clicked(updatexy)

print("We will start you off with a bar graph using the values you've chosen but you can adjust the graph type and such to your liking using the widgets on the page")
bar(value)
plt.draw()
plt.show()
