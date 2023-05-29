# oy sistemi

sandik = 0

while True:
    akp = int(input('AKP % oy birimi: '))
    chp = int(input('CHP % oy birimi: '))

    akpmat = (akp + akp) / 1
    chpmat = (chp + chp) / 1
    sandikmat = sandik + 1

    if akpmat > 100:
        print('Geçersiz oy türü. Sayı % 100 geçiyor..')

    if chpmat > 100:
        print('Geçersiz oy türü. Sayı % 100 geçiyor..')

    if akp > chp:
        print('Önde giden: Recep Tayyip Erdoğan\nAKP: % {}\nCHP: % {}\nSandık: % {}'.format(akpmat, chpmat, sandikmat))
    elif chp > akp:
        print('Önde giden: Kemal Kılıçlaroğlu\nCHP: % {}\nAKP: % {}\nSandık: % {}'.format(chpmat, akpmat, sandikmat))

    if sandik == 100:
        print('Tüm sandıklar açıldı.')