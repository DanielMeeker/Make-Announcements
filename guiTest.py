from Tkinter import *
import time, re, os

class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
	
	def create_widgets(self):
		self.nameLabel = Label(self, text = "Enter your name:")
		self.nameLabel.grid(row = 0, column = 0, sticky = W)

		self.nameEntry = Entry(self)
		self.nameEntry.grid(row = 0, column = 1, sticky = W)
		self.nameEntry.focus_set()

		self.dateInputLabel = Label(self, text = "Enter the date you want your announcement read:")
		self.dateInputLabel.grid(row = 1, column = 0, sticky = W)

		self.dateInputEntry = Entry(self)
		self.dateInputEntry.grid(row =1, column = 1, sticky = W)

		self.announcementLabel = Label(self, text = "Enter your announcement:")
		self.announcementLabel.grid(row = 2, column = 0, sticky = W)

		#self.announcementEntry = StringVar()
		self.announcementEntry = Text(self, width = 64, height = 10)
		#self.announcementEntry = Entry(self)
		self.announcementEntry.grid(row = 3, column = 0, columnspan = 2, sticky = W)

		self.amOrPmLabel = Label(self, text = "Is the announcement read in the Morning, Afternoon, or Both?")
		self.amOrPmLabel.grid(row = 4, column = 0, columnspan =2, sticky = W)

		self.amOrPmEntry = StringVar()

                

		Radiobutton(self, text = "AM", variable = self.amOrPmEntry, value = "AM").grid(row = 5, column = 0, sticky = W) #, command = self.output
		Radiobutton(self, text = "PM", variable = self.amOrPmEntry, value = "PM").grid(row = 5, column = 1, sticky = W)
		Radiobutton(self, text = "BOTH", variable = self.amOrPmEntry, value = "Both").grid(row = 6, column = 0, sticky = W)




		self.submit_button = Button(self, text = "Submit", command = self.output)
		self.submit_button.grid(row = 7, column = 0, sticky = W)

		self.text = Text(self, width = 64, height = 5, wrap = WORD)
		self.text.grid(row = 8, column = 0, columnspan =2, sticky = W)

	def output(self):
		contentName = self.nameEntry.get()
		contentDate = self.dateInputEntry.get()
		contentAnnouncement = self.announcementEntry.get("1.0", "end-1c")
		contentAmOrPm = self.amOrPmEntry.get()


		self.text.delete(0.0, END)
		self.text.insert(0.0, "Name: "+ contentName + "\nDate: " + contentDate + "\nAnnouncement: " + contentAnnouncement + "\nTime" + contentAmOrPm)

		now = (time.strftime("%m_%d_%Y"))
		nowTime = (time.strftime("%m/%d/%Y %H:%M:%S"))

		lengthTeach = 20 - len(contentName)
		lengthAm = 10 - len(contentAmOrPm)
		lengthAll = 20 + lengthAm + len(contentAmOrPm)

		space1 = " " * lengthTeach
		space2 = " " * lengthAm
		space3 = " " * lengthAll

		contentAnnouncement = re.sub("(.{64})", "\\1\n%s" % space3, contentAnnouncement, 0, re.DOTALL)

		contentDate = re.sub('/', '_', contentDate)
		announce = open("./announcements2/announcement" + contentDate + ".txt", 'a')
		if (os.path.getsize("./announcements2/announcement" + contentDate + ".txt") == 0):
			announce.write("Teacher" + " " * 13 + "AM/PM" + " " * 5 + "Announcement\n\n")

		announce.write(contentName + space1 + contentAmOrPm + space2 + contentAnnouncement + "\n")
		announce.write("Time Added: " + nowTime + "\n\n")

		announce.close()

		sys.exit(0)




root = Tk()
root.title("Announcements")
root.geometry("500x550")
app = Application(root)

root.mainloop()

"""root = Tk()

root.title("Announcements")
root.geometry("800x700")

app = Frame(root)
announcement = Label(app, text = "Announcement")
teacher = Label(app, text = "Name")
dateRead = Label(app, text = "Desired Date")
amOrPm = Label(app, text = "Morning/Afternoon")

submit = Button(app, text ="submit")

app.grid()
announcement.grid()
teacher.grid()
dateRead.grid()
amOrPm.grid()
submit.grid()

root.mainloop()

"""
