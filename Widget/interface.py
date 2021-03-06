from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from Widget.accueilProjEdu import Ui_MainWindow
import sqlite3

class Ui_MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.bnb.clicked.connect(self.personality)
    #SETCURRENTWIDGET()POUR AFFICHER UN WIDGET

    def personality(self):

        con=sqlite3.connect("data.db")

        c=con.cursor()
        listes=[
                    ["PRESIDENCE",
                        "PRIMATURE",
                        "L'ASSEMBLEE NATIONALE",
                        "LE SENAT",
                        "LE CONSEIL CONSTITUTIONNEL",
                        "COURS DE CASSATION",
                        "CONSEIL D'ETAT ",
                        "LA COUR SUPREME",
                        "LA COURS DES COMPTES",
                        "MEDIATEUR DE LA REPUBLIQUE",
                        "LA GRANDE CHANCELERIE DE L'ORDRE NATIONAL" ,
                        "LE CONSEIL ECONOMIQUE SOCIAL ENVIRONNEMENTAL ET CULTUREL",
                        "COMMISSION ELECTORALE INDEPENTANTE",
                        "HAUTE AUTORITE DE LA BONNE GOUVERNANCE",
                        "L'INSPECTION GENERALE DE L'ETAT",
                        "CHAMBRE DES ROIS ET DES CHEFS TRADITIONNELS"
                    ],["S.E.M ALASSANE DRAMANE OUATTARA",
                        'AMADOU SOUMAHORO',
                        'JEANNOT AHOUSSOU-KOUADIO',
                        'MAMADOU KONE',
                        'CAMARA NANAB CHANTAL',
                        'PATRICE YAO KOUAKOU',
                        'RENE FRANCOIS APHING KOUASSI',
                        "KANVALY DIOMANDE",
                        "ADAMA TOUNGARA",
                        'HENRIETTE ROSE DAGRI DIABATE',
                        'Dr AKA AOUELE',
                        'IBRAHIM COULIBALY/KUIBERT',
                        "N'GOLO FATOGOMA COULIBALY",
                        "AHOUA N'DOLI THEOPHILE",
                        "DESIRE AMON PAUL TANOE"
                    ],["""Le Pr??sident de la R??publique est le
                                    Chef de l???Etat. Il incarne l???unit??
                                    nationale...""",
                        """
                                        Le Premier ministre de C??te d'
                                        Ivoire est charg?? de coordonner
                                        l'action du gouvernement de la... """,
                        """Le parlement est constitu?? d???une chambre 
                                        unique dite Assembl??e Nationale dont les 
                                        membres....""",
                        """Le Pr??sident de la R??publique est le
                                        Chef de l???Etat. Il incarne l???unit??
                                        nationale...""",
                        """C???est la loi N?? 94-438 du 16 Ao??t 19
                                        94 qui fixe la composition, l???organisa
                                        tion, les attributions et  ...""",
                        """Le Pr??sident de la R??publique est le
                                        Chef de l???Etat. Il incarne l???unit??
                                        nationale...""",
                        """Le parlement est constitu?? d???une
                                        chambre unique dite Assembl??e
                                        Nationale dont les membres....""",
                        """La justice est rendue dans les 
                                        juridictions par un personnel vari??.
                                        Les juridictions :...""",
                        """Haute juridiction financi??re charg??e 
                                        du contr??le des finances publiques,
                                        la Cour des ...""",
                        """ARTICLE 115 La M??diation c???est 
                                        l???action d???intervenir entre deux ou 
                                        plusieurs personnes, ...""",
                        """C???est la loi n??60-403 du 10
                                        D??cembre 1960, modifi??e 
                                        par la loi ...""",
                        """Les missions et attributions du 
                                        CESEC sont d??termin??es ...""",
                        """Pr??vue par la Constitution du 1er 
                                        ao??t 2000, en son article...""",
                        """CADRE JURIDIQUE Ordonnance 
                                        N??2013-660 du 20 septembre ...""",
                        """L???Inspecteur G??n??ral d???Etat : Dirige,
                                        anime et coordonne les activit??s ..."""
                ],
                ["","","","","","","","","","","","","","","",""]
            ]
        
        dict_infos={
            "titre": "PRESIDENCE",
            "nom": "S.E.M ALASSANE DRAMANE OUATTARA",
            "description_mini": """Le Pr??sident de la R??publique est le
                                Chef de l???Etat. Il incarne l???unit??
                                nationale...""",
            "description": ""
        }

        command='''CREATE TABLE IF NOT EXISTS user(
            titre text,
            nom text,
            description_mini text, 
            description text
        )'''

        c.execute(command)
        command1="INSERT INTO user VALUES(:titre,:nom, :description_mini, :description)"

        c.execute(command1,dict_infos)
        
