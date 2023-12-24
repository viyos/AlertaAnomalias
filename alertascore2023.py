import smtplib
import email.message

lista = []
arq = open(r'bironeurototal%.txt','r')
for linha in arq:
	linha = linha.rstrip()
	linha = linha.split(';')
	lista.append(linha)
a = len(lista)
dt = lista[a-1][0]
b = int(lista[a - 1][1])
c = int(lista[a - 1][2])
d = (b/c)*100 #Missing Idade Segurado
d = round(d,2)
e = int(lista[a - 1][3])
f = int(lista[a - 1][4])
g = (e/f)*100 #Missing Score RF
g = round(g,2)
h = int(lista[a - 1][5])
i1 = int(lista[a - 1][6])
j = (h/i1)*100 #Missing Score Sinistro
j = round(j,2)
k = int(lista[a - 1][7])
l = int(lista[a - 1][8])
m = (k/l)*100 #Missing Pto Serasa
m = round(m,2)
n = int(lista[a - 1][9])
o = int(lista[a - 1][10])
p = (n/o)*100 #Missing Score Serasa
p = round(p,2)
q = int(lista[a - 1][11])
r = int(lista[a - 1][12])
s = (q/r)*100 #Missing Score Auto Glass
s = round(s,2)
t = int(lista[a - 1][11])
u = int(lista[a - 1][12])
v = (t/u)*100 #Missing Classe Social
v = round(v,2)

lista1 = []
arq1 = open(r'biropessoatotal%.txt','r')
for linha1 in arq1:
	linha1 = linha1.rstrip()
	linha1 = linha1.split(';')
	lista1.append(linha1)
aa = len(lista1)
bb = int(lista1[aa - 1][1])
cc = int(lista1[aa - 1][2])
dd = (bb/cc)*100 #Erro Tempo de Relacionamento 
dd = round(dd,2)
ee = int(lista1[aa - 1][3])
ff = int(lista1[aa - 1][4])
gg = (ee/ff)*100 #Erro Sinistros Motor
gg = round(gg,2)
hh = int(lista1[aa - 1][5])
ii = int(lista1[aa - 1][6])
jj = (hh/ii)*100 #Erro Flag Colisão
jj = round(jj,2)
tt = int(lista1[aa - 1][5])
uu = int(lista1[aa - 1][6])
vv = (tt/uu)*100 #Erro RNS CPF Total
vv = round(vv,2)

lista2 = []
arq2 = open(r'biroginitotal%.txt','r')
for linha2 in arq2:
	linha2 = linha2.rstrip()
	linha2 = linha2.split(';')
	lista2.append(linha2)

aaa = len(lista2)
bbb = int(lista2[aaa - 1][1])
ccc = int(lista2[aaa - 1][2])
ddd = (bbb/ccc)*100 #Erro Tempo de Relacionamento 
ddd = round(ddd,2)


dd = str(dd)
gg = str(gg)
jj = str(jj)
d = str(d)
g = str(g)
j = str(j)
m = str(m)
p = str(p)
s = str(s)
v = str(v)
vv = str(vv)
ddd = str(ddd)

corpo = 'Prezados, no dia ' + dt + ' tivemos a porcentagem de erros em relação aos Biros internos:<br>' + dd + '% Tempo de Relacionamento<br>' + gg + '%' + ' Quantidade de Sinistros no Motor<br>'  + jj + '%' +  ' Flag Colisão<br>' + vv + '%' +  ' RNS CPF Total<br>' + ddd + '%' +  ' IDHM 2010<br>' + 'Em relação ao Biro Neurotech possuimos os percentuais de cotações com missings:<br>' + d + '%' + ' Idade do Segurado<br>' + g + '%' + ' Score Roubo e Furto<br>' + j +'%' + ' Score Sinistro<br>' + m + '%' + ' Pontuação Serasa<br>' + p + '%' + ' Pontuação Score Serasa<br>' + s + '%' + ' Pontuação Score Auto Glass<br>' + v + '%' + ' Pontuação Classe Social'

listaemail = ['abc.def@hotmail.com','ghi.jkl@hotmail.com']

dd = float(dd)
gg = float(gg)
jj = float(jj)
d = float(d)
g = float(g)
j = float(j)
m = float(m)
p = float(p)
s = float(s)
v = float(v)
vv = float(vv)
ddd = float(ddd)

for i in range(len(listaemail)):
	if dd > 0.1 or gg > 0.1 or jj > 0.1 or d > 0.05 or g > 0.05 or j > 0.05 or m > 0.05 or p > 0.05 or s > 0.05 or v > 0.05 or ddd > 0.02:
		corpo_email = corpo
		msg = email.message.Message()		
		msg['Subject'] = "AVISO DE ERROS"
		msg['From'] = 'abcdef@gmail.com'   
		msg['To'] = listaemail[i]
		password = '123456' 
		msg.add_header('Content-Type', 'text/html')
		msg.set_payload(corpo_email)
		s = None
		while s is None:
			try:
				s = smtplib.SMTP('smtp.gmail.com: 587')
			except:
				pass		
		s.starttls()
	    # Login Credentials for sending the mail
		s.login(msg['From'], password)
		s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
		print('Email enviado')
	else:
		print('Sem erros')