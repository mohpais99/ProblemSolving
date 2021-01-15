class soal_nomor_4:
    def __init__(self, a, b, c ,d):
        self.TotalJarak = a
        self.MaxTank = b
        self.JarakSpbu = c
        self.Harga = d
        self.TankiAwal = 180
        self.kmPemberhentian = [100,200,360]
        self.price = 0
        self.programStart()

    def programStart(self):
        for jarak in range(0 , self.TotalJarak + 1):
            for i, km in enumerate(self.JarakSpbu):
                if km == jarak and km in self.kmPemberhentian:
                    sisaTanki = self.TankiAwal - km
                    jumlahLiter = self.MaxTank - sisaTanki
                    calculate = self.Harga[i] * jumlahLiter
                    self.TankiAwal += jumlahLiter
                    self.price += calculate
        print('jawaban no 4: Price =', self.price)
