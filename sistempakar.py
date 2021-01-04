from experta import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("penyakit.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("Gejala penyakit/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Deskripsi penyakit/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Obat penyakit/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()
	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("Kemungkinan penyakit yang kamu miliki adalah %s\n" %(id_disease))

		plt.imshow(mpimg.imread("./img/" + id_disease + ".jpg"))
		plt.title(id_disease)
		plt.axis('off')
		plt.show()

		print("Sedikit deskripsi tentang penyakit yang diberikan :")
		print(disease_details+"\n")
		print("Pengobatan umum dan prosedur yang disarankan oleh dokter adalah :")
		print(treatments+"\n")

class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Halo! Saya adalah Do-bot, Saya akan mendiagnosa penyakit kulit yang anda alami!")
		print("Oleh karena itu anda harus menjawab beberapa gejala yang anda alami")
		print("Apakah anda merasakan beberapa gejala dibawah ini(yes/no):")
		print("")
		yield Fact(action="find_disease")

#Gejala
	@Rule(Fact(action='find_disease'), NOT(Fact(kulit_membengkak=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(kulit_membengkak=input("Apakah anda mengalami pembengkakan kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(benjolan_di_kulit=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(benjolan_di_kulit=input("Apakah anda mengalami benjolan di kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(mengeluarkan_nanah=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(mengeluarkan_nanah=input("Apakah kulit anda mengeluarkan nanah: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(demam=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(demam=input("Apakah anda demam: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(mata_merah=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(mata_merah=input("Apakah mata anda merah: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(kulit_kepala_berminyak=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(kulit_kepala_berminyak=input("Apakah kulit kepala anda berminyak: ")))
	 
	@Rule(Fact(action='find_disease'), NOT(Fact(rasa_gatal=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(rasa_gatal=input("Apakah anda merasakan gatal: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(luka_dari_bagian_mulut=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(luka_dari_bagian_mulut=input("Apakah ada luka dari bagian mulut: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(memiliki_gelembung_berisi_air=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(memiliki_gelembung_berisi_air=input("Apakah ada semacam gelembung berisi air: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(rasa_nyeri=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(rasa_nyeri=input("Apakah anda merasakan nyeri: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(kulit_melepuh=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(kulit_melepuh=input("Apakah kulit anda melepuh: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(memiliki_bercak_bercak_merah=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(memiliki_bercak_bercak_merah=input("Apakah timbul bercak bercak merah: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(iritasi_kulit=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(iritasi_kulit=input("Apakah terjadi iritasi kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(uban_muncul_sebelum_waktunya=W())), salience=1)
	def symptom_13(self):
		self.declare(Fact(uban_muncul_sebelum_waktunya=input("Apakah muncul uban sebelum waktunya: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(muncul_keringat_berlebihan=W())), salience=1)
	def symptom_14(self):
		self.declare(Fact(muncul_keringat_berlebihan=input("Apakah anda mengalami keringat yang berlebihan: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(menimbulkan_warna_kekuningan=W())), salience=1)
	def symptom_15(self):
		self.declare(Fact(menimbulkan_warna_kekuningan=input("Apakah ada timbul warna kekuningan pada kulit anda: ")))

	@Rule(Fact(action='find_disease'),Fact(kulit_membengkak="yes"),Fact(benjolan_di_kulit="yes"),
		  Fact(mengeluarkan_nanah="no"),Fact(demam="no"),Fact(mata_merah="no"),Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"),Fact(luka_dari_bagian_mulut="no"),Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"),Fact(kulit_melepuh="no"),Fact(memiliki_bercak_bercak_merah="no"),Fact(iritasi_kulit="no"),
		  Fact(uban_muncul_sebelum_waktunya="no"),Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_0(self):
		self.declare(Fact(disease="Jerawat"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="yes"),
		  Fact(mengeluarkan_nanah="yes"), Fact(demam="no"), Fact(mata_merah="no"), Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"), Fact(luka_dari_bagian_mulut="no"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="no"), Fact(memiliki_bercak_bercak_merah="no"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_1(self):
		self.declare(Fact(disease="Bisul"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="no"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="yes"), Fact(mata_merah="yes"),
		  Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"), Fact(luka_dari_bagian_mulut="yes"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="no"), Fact(memiliki_bercak_bercak_merah="no"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_2(self):
		self.declare(Fact(disease="Campak"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="no"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="no"), Fact(mata_merah="no"), Fact(kulit_kepala_berminyak="yes"),
		  Fact(rasa_gatal="yes"), Fact(luka_dari_bagian_mulut="no"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="no"), Fact(memiliki_bercak_bercak_merah="no"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_3(self):
		self.declare(Fact(disease="Ketombe"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="yes"), Fact(benjolan_di_kulit="no"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="no"), Fact(mata_merah="no"), Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"), Fact(luka_dari_bagian_mulut="yes"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="no"), Fact(memiliki_bercak_bercak_merah="no"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_4(self):
		self.declare(Fact(disease="Sariawan"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="no"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="no"), Fact(mata_merah="no"), Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"), Fact(luka_dari_bagian_mulut="no"), Fact(memiliki_gelembung_berisi_air="yes"),
		  Fact(rasa_nyeri="yes"), Fact(kulit_melepuh="no"), Fact(memiliki_bercak_bercak_merah="no"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_5(self):
		self.declare(Fact(disease="Herpes"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="no"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="no"), Fact(mata_merah="no"), Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="yes"), Fact(luka_dari_bagian_mulut="no"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="yes"), Fact(memiliki_bercak_bercak_merah="no"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_6(self):
		self.declare(Fact(disease="Kudis"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="no"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="yes"), Fact(mata_merah="no"), Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"), Fact(luka_dari_bagian_mulut="no"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="yes"), Fact(memiliki_bercak_bercak_merah="yes"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_7(self):
		self.declare(Fact(disease="Impetigo"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="no"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="yes"), Fact(mata_merah="yes"), Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"), Fact(luka_dari_bagian_mulut="no"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="no"), Fact(memiliki_bercak_bercak_merah="no"),
		  Fact(iritasi_kulit="yes"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_8(self):
		self.declare(Fact(disease="Lepra"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="yes"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="no"), Fact(mata_merah="no"), Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"), Fact(luka_dari_bagian_mulut="yes"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="no"), Fact(memiliki_bercak_bercak_merah="no"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_9(self):
		self.declare(Fact(disease="Keloid"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="yes"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="no"), Fact(mata_merah="no"), Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"), Fact(luka_dari_bagian_mulut="no"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="no"), Fact(memiliki_bercak_bercak_merah="yes"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_10(self):
		self.declare(Fact(disease="Hemangioma"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="no"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="no"), Fact(mata_merah="no"), Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"), Fact(luka_dari_bagian_mulut="no"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="no"), Fact(memiliki_bercak_bercak_merah="no"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="yes"), Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))
	def disease_11(self):
		self.declare(Fact(disease="Vitiligo"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="no"), Fact(benjolan_di_kulit="no"),
		  Fact(mengeluarkan_nanah="no"), Fact(demam="no"), Fact(mata_merah="no"), Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"), Fact(luka_dari_bagian_mulut="no"), Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"), Fact(kulit_melepuh="no"), Fact(memiliki_bercak_bercak_merah="no"),
		  Fact(iritasi_kulit="no"), Fact(uban_muncul_sebelum_waktunya="no"), Fact(muncul_keringat_berlebihan="yes"),
		  Fact(menimbulkan_warna_kekuningan="yes"))
	def disease_12(self):
		self.declare(Fact(disease="Hypohidrosis"))

	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)

	def disease(self, disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("Kemungkinan terbesar yang anda alami adalah %s\n" %(id_disease))

		plt.imshow(mpimg.imread("./img/" + id_disease + ".jpg"))
		plt.title(id_disease)
		plt.axis('off')
		plt.show()

		print("Berikut deskripsi singkat dari penyakit yang diberikan :")
		print(disease_details+"\n")
		print("Beberapa pengobatan yang disarankan :")
		print(treatments+"\n")

	@Rule(Fact(action='find_disease'),
		  Fact(kulit_membengkak=MATCH.kulit_membengkak),
		  Fact(benjolan_di_kulit=MATCH.benjolan_di_kulit),
		  Fact(mengeluarkan_nanah=MATCH.mengeluarkan_nanah),
		  Fact(demam=MATCH.demam),
		  Fact(mata_merah=MATCH.mata_merah),
		  Fact(kulit_kepala_berminyak=MATCH.kulit_kepala_berminyak),
		  Fact(rasa_gatal=MATCH.rasa_gatal),
		  Fact(luka_dari_bagian_mulut=MATCH.luka_dari_bagian_mulut),
		  Fact(memiliki_gelembung_berisi_air=MATCH.memiliki_gelembung_berisi_air),
		  Fact(rasa_nyeri=MATCH.rasa_nyeri),
		  Fact(kulit_melepuh=MATCH.kulit_melepuh),
		  Fact(memiliki_bercak_bercak_merah=MATCH.memiliki_bercak_bercak_merah),
		  Fact(iritasi_kulit=MATCH.iritasi_kulit),
		  Fact(uban_muncul_sebelum_waktunya=MATCH.uban_muncul_sebelum_waktunya),
		  Fact(muncul_keringat_berlebihan=MATCH.muncul_keringat_berlebihan),
		  Fact(menimbulkan_warna_kekuningan=MATCH.menimbulkan_warna_kekuningan),
		  NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,kulit_membengkak, benjolan_di_kulit, mengeluarkan_nanah, demam, mata_merah, kulit_kepala_berminyak,
					rasa_gatal, luka_dari_bagian_mulut,memiliki_gelembung_berisi_air ,rasa_nyeri ,kulit_melepuh ,memiliki_bercak_bercak_merah ,
					iritasi_kulit,uban_muncul_sebelum_waktunya,muncul_keringat_berlebihan,menimbulkan_warna_kekuningan):
		print("\nTidak menemukan penyakit yang sangat pas dengan gejala yang anda alami")
		lis = [kulit_membengkak, benjolan_di_kulit, mengeluarkan_nanah, demam, mata_merah, kulit_kepala_berminyak,
					rasa_gatal, luka_dari_bagian_mulut,memiliki_gelembung_berisi_air ,rasa_nyeri ,kulit_melepuh ,memiliki_bercak_bercak_merah ,
					iritasi_kulit,uban_muncul_sebelum_waktunya,muncul_keringat_berlebihan,menimbulkan_warna_kekuningan]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("Ingin mencoba diagnosa dengan gejala yang lain?")
		if input() == "no":
			exit()
		#print(engine.facts)