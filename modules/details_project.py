from tkinter import *
from tkinter import ttk
from objects.app import app

class ProjectDetailsModule(object):
    def __init__(self, detailsPanel):
        self.container = ttk.Labelframe(detailsPanel, text="Project details")
        self.container.pack(side = LEFT, fill=Y)

        self.subjectCount = ttk.Label(self.container, text=None)
        self.subjectCount.pack(expand=False)

        # VO2 details
        self.VO2max = ttk.Label(self.container, text=None)
        self.VO2max.pack(expand=False)
        self.VO2min = ttk.Label(self.container, text=None)
        self.VO2min.pack(expand=False)
        self.VO2avg = ttk.Label(self.container, text=None)
        self.VO2avg.pack(expand=False)

        # QaO2 details
        self.QaO2max = ttk.Label(self.container, text=None)
        self.QaO2max.pack(expand=False)
        self.QaO2min = ttk.Label(self.container, text=None)
        self.QaO2min.pack(expand=False)
        self.QaO2avg = ttk.Label(self.container, text=None)
        self.QaO2avg.pack(expand=False)

        # DO2 details
        self.DO2max = ttk.Label(self.container, text=None)
        self.DO2max.pack(expand=False)
        self.DO2min = ttk.Label(self.container, text=None)
        self.DO2min.pack(expand=False)
        self.DO2avg = ttk.Label(self.container, text=None)
        self.DO2avg.pack(expand=False)

        self.calculateButton = ttk.Button(self.container, text="Calculate", command=lambda: app.getMaxMinAvg(plotProject=True))

    def refreshDetails(self):
        # Show buttons
        try:
            self.calculateButton.pack_info()
        except:
            self.calculateButton.pack(side=BOTTOM)
        
        activeProject = app.getActiveProject()
        self.subjectCount.config(text=f'Subjects: {len(activeProject.subjects)}')
        # VO2
        self.VO2max.config(text=f'VO\u2082\u2098\u2090\u2093 peak: {"{0:.1f}".format(float(activeProject.VO2max))}')
        self.VO2min.config(text=f'VO\u2082\u2098\u2090\u2093 min: {"{0:.1f}".format(float(activeProject.VO2min))}')
        self.VO2avg.config(text=f'VO\u2082\u2098\u2090\u2093 avg: {"{0:.1f}".format(float(activeProject.VO2avg))}')
        # QaO2
        self.QaO2max.config(text=f'QaO\u2082 peak: {"{0:.1f}".format(float(activeProject.QaO2max))}')
        self.QaO2min.config(text=f'QaO\u2082 min: {"{0:.1f}".format(float(activeProject.QaO2min))}')
        self.QaO2avg.config(text=f'QaO\u2082 avg: {"{0:.1f}".format(float(activeProject.QaO2avg))}')
        # DO2
        self.DO2max.config(text=f'DO\u2082 peak: {"{0:.1f}".format(float(activeProject.DO2max))}')
        self.DO2min.config(text=f'DO\u2082 min: {"{0:.1f}".format(float(activeProject.DO2min))}')
        self.DO2avg.config(text=f'DO\u2082 avg: {"{0:.1f}".format(float(activeProject.DO2avg))}')