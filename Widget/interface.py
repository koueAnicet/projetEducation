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
                    ],["""Le Président de la République est le
                                    Chef de l’Etat. Il incarne l’unité
                                    nationale...""",
                        """
                                        Le Premier ministre de Côte d'
                                        Ivoire est chargé de coordonner
                                        l'action du gouvernement de la... """,
                        """Le parlement est constitué d’une chambre 
                                        unique dite Assemblée Nationale dont les 
                                        membres....""",
                        """Le Président de la République est le
                                        Chef de l’Etat. Il incarne l’unité
                                        nationale...""",
                        """C’est la loi Nº 94-438 du 16 Août 19
                                        94 qui fixe la composition, l’organisa
                                        tion, les attributions et  ...""",
                        """Le Président de la République est le
                                        Chef de l’Etat. Il incarne l’unité
                                        nationale...""",
                        """Le parlement est constitué d’une
                                        chambre unique dite Assemblée
                                        Nationale dont les membres....""",
                        """La justice est rendue dans les 
                                        juridictions par un personnel varié.
                                        Les juridictions :...""",
                        """Haute juridiction financière chargée 
                                        du contrôle des finances publiques,
                                        la Cour des ...""",
                        """ARTICLE 115 La Médiation c’est 
                                        l’action d’intervenir entre deux ou 
                                        plusieurs personnes, ...""",
                        """C’est la loi n°60-403 du 10
                                        Décembre 1960, modifiée 
                                        par la loi ...""",
                        """Les missions et attributions du 
                                        CESEC sont déterminées ...""",
                        """Prévue par la Constitution du 1er 
                                        août 2000, en son article...""",
                        """CADRE JURIDIQUE Ordonnance 
                                        N°2013-660 du 20 septembre ...""",
                        """L’Inspecteur Général d’Etat : Dirige,
                                        anime et coordonne les activités ..."""
                ],
                ["","","","","","","","","","","","","","","",""]
            ]
        
        dict_infos={
            "titre": "PRESIDENCE",
            "nom": "S.E.M ALASSANE DRAMANE OUATTARA",
            "description_mini": """Le Président de la République est le
                                Chef de l’Etat. Il incarne l’unité
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
        
