import wx

class Frame1(wx.Frame):

    def __init__(self, superior):
        wx.Frame.__init__(self, parent=superior, title="FirstGUI", pos=(300, 100), size=(400, 400))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        #self.text1 = wx.TextCtrl(panel, size=(100, 200), style=wx.TE_MULTILINE|wx.TE_READONLY)
        #self.text2 = wx.TextCtrl(panel, size=(100, 200), style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.label1 = wx.StaticText(panel,pos=(10,10))
        self.label2 = wx.StaticText(panel,pos=(10,30), size=(160,-1), style=wx.ALIGN_CENTER)

        font = wx.Font(wx.FontInfo(10)).Scaled(6)

        self.label1.SetForegroundColour("blue")
        self.label1.SetFont(font)
        #self.label1.SetBackgroundColour("black")
        self.label2.SetForegroundColour("black")
        self.label2.SetFont(font)
        #self.label2.SetBackgroundColour("black")
        #sizer.Add(self.text1,0,wx.ALIGN_TOP | wx.EXPAND)
        #sizer.Add(self.text2,2,wx.ALIGN_TOP | wx.EXPAND)
        sizer.Add(self.label1, 0, wx.ALIGN_TOP | wx.EXPAND)
        sizer.Add(self.label2, 1, wx.ALIGN_TOP | wx.EXPAND)
        button1 = wx.Button(panel,label="点我")
        button2 = wx.Button(panel, label="点我2")
        sizer.Add(button1)
        sizer.Add(button2)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON, self.OnClick1, button1)
        self.Bind(wx.EVT_BUTTON, self.OnClick2, button2)
        statusbar = self.CreateStatusBar()
        menubar = wx.MenuBar()

        first = wx.Menu()
        second = wx.Menu()
        exit = wx.Menu()

        exit.Append(wx.ID_EXIT,"Exit","This is an exit point")
        first.Append(1,"new window","this is a new window")
        first.Append(2,"MessageDialog","click to show a MSG")
        second.Append(1, "open...", "this will open a new window")


        menubar.Append(first,"File")
        menubar.Append(second,"Edit")
        menubar.Append(exit, "Exit")


        self.SetMenuBar(menubar)

        #box=wx.MessageDialog(None,"this is MSG box","Title",wx.OK)
        #answer = box.ShowModal()
        #box.Destroy()
        msgbutton = first.FindItemById(2)
        exitbutton = exit.FindItemById(wx.ID_EXIT)

        self.Bind(wx.EVT_MENU, self.ClickShowMsg, msgbutton)
        self.Bind(wx.EVT_MENU,self.exit,exitbutton)


    global count1,count2

    count1 = 0
    count2 = 0

    def OnClick1(self,text):

        global count1
        count1 = count1 + 1
        count1str = str(count1)
        #self.text1.write(count1str + "\n")
        self.label1.SetLabel(count1str)

    def OnClick2(self,text):

        global count2
        count2 = count2 + 1
        count1str2 = str(count2)
        #self.text2.AppendText(count1str2 + "\n")
        self.label2.SetLabel(count1str2)

    def ClickShowMsg(self,e):
        box = wx.MessageDialog(self, "this is MSG box", "Title", wx.OK)
        box.ShowModal()
        box.Destroy()

    def exit(self,e):

        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()