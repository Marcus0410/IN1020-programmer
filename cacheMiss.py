def totaltAntallSykler(antallInstr, syklerPerInstr, minneaksess, cacheMissPros, syklerPerMiss, syklerPerHit):
    totalt = 0
    fraMinne = antallInstr * (minneaksess / 100)    #antall instruksjoner må aksesseres i minne

    totalt += (cacheMissPros / 100) * fraMinne * syklerPerMiss      #sykler fra cache-miss
    totalt += ((100 - cacheMissPros) / 100) * fraMinne * syklerPerHit #sykler fra cache hit

    totalt += (antallInstr - fraMinne) * syklerPerInstr             #vanlig instruksjoner

    print("Totalt antall sykler:", totalt)

antallInstr = int(input("Antall instruksjoner: "))
syklerPerInstr = int(input("Antall klokkesykler per instruksjon: "))
minneaksess = int(input("Hvor mange % minneaksessering: "))
cacheMissPros = int(input("Cache-miss prosent: "))
syklerPerMiss = int(input("Antall sykler per cache-miss: "))
syklerPerHit = int(input("Antall sykler per cachde-hit: "))

totaltAntallSykler(antallInstr, syklerPerInstr, minneaksess, cacheMissPros, syklerPerMiss, syklerPerHit)
