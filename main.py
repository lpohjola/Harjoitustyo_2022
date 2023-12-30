sanalista = []
luetut_alkiot = []
verbit = []
sanat = open('taajuussanasto.csv', 'r')

for row in sanat:
    row = row.strip()
    parts = row.split(';')
    sanalista.append(parts[3])

for alkio in sanalista:
    if "verbi" in alkio:
        verbit.append(alkio)

for alkio in list(verbit):
    if "adverbi" in alkio:
        verbit.remove(alkio)

for alkio in list(verbit):
    if alkio not in luetut_alkiot:
        luetut_alkiot.append(alkio)
    else:
        continue
    sana = alkio
    taivutus = input(f'Taivuta verbiä "{sana}" muotoon m.1.p.')


sanat.close()
