import json,random

def execute_l(prt):
            try:
                global memory
                prt = prt.strip()
                prt_l = prt.lower()
                if prt_l.startswith("vrandom "):
                    sisa = prt_l[8:].strip()
                    if "=" in sisa:
        # Format: vrandom nama = 1 10
                        bagian = sisa.split("=", 1)
                        var_name = bagian[0].strip()
                        angka = bagian[1].strip().split()
                        if len(angka) == 2:
                            min_val = int(angka[0])
                            max_val = int(angka[1])
                            hasil = random.randint(min_val, max_val)
                            memory[var_name] = str(hasil)
                            print(f"[#] {var_name} = {hasil} (random)")
                        else:
        # Format: vrandom 1 10 (cuma print)
                           angka = sisa.split()
                           if len(angka) == 2:
                               min_val = int(angka[0])
                               max_val = int(angka[1])
                               hasil = random.randint(min_val, max_val)
                               print(f"Random: {hasil}")

                
                
                
                if prt.lower().startswith("random "):
                    dty = prt[7:].split()
                    if len(dty) == 2:
                         dy1 = int(dty[0])
                         dy2 = int(dty[1])
                         jdom = random.randint(dy1,dy2)
                         print(jdom)
    # 2. PRINT: vprint *teks* (bisa pake !variabel)
                if prt.startswith("vprint") and prt_l.endswith("*"):
                    text = prt.replace("vprint", "").strip().strip("*")
        
        # Ganti !nama dengan isi variabel
                    for name, number in memory.items():
                        text = text.replace(f"({name})", number)
                    print(text)
                if "=" in prt and not prt_l.startswith("vprint"):
                    hf = prt.split("=", 1)
                    name = hf[0].strip()
                    expr = hf[1].strip()

    # Coba hitung ekspresi matematika
                    try:
        # Ganti (nama_var) dengan nilainya dulu
                        for var_name, var_value in memory.items():
                            expr = expr.replace(f"({var_name})", var_value)
        
                        result = eval(expr)
                        value = str(result)
                    except:
        # Kalau gagal, simpan sebagai string biasa
                        value = expr
                    memory[name] = value

            except Exception as eer:
                print("error",eer)


import sys
if len(sys.argv) > 1:
    # Mode file: baca dari file
    with open(sys.argv[1], 'r') as f:
        for line in f:
            dst = line.strip()
            if dst:
                # Proses setiap baris seperti input interaktif
                dst_lower = dst.lower()
                # ... (copy logika proses perintah dari dalam while True)
    sys.exit(0)


print("hello in vx programming multifunction vx")
memory = {}
while True:
    try:
        dst = input(">>> ")
        dst_lower = dst.lower().strip()
        
        # IF-ELSE STATEMENT (ONE-LINER + MULTI-LINE)
        # WHILE LOOP: while 5 vprint *hi*  (loop selama kondisi = angka bukan 0)
# RANDOM: vrandom x = 1 10
        if dst_lower.startswith("vrandom "):
            sisa = dst[8:].strip()
            if "=" in sisa:
        # Format: vrandom nama = 1 10
                bagian = sisa.split("=", 1)
                var_name = bagian[0].strip()
                angka = bagian[1].strip().split()
                if len(angka) == 2:
                    min_val = int(angka[0])
                    max_val = int(angka[1])
                    hasil = random.randint(min_val, max_val)
                    memory[var_name] = str(hasil)
                    print(f"[#] {var_name} = {hasil} (random)")
                else:
        # Format: vrandom 1 10 (cuma print)
                   angka = sisa.split()
                   if len(angka) == 2:
                       min_val = int(angka[0])
                       max_val = int(angka[1])
                       hasil = random.randint(min_val, max_val)
                       print(f"Random: {hasil}")


        if dst.lower().startswith("random "):
          dty = dst[7:].split()
          if len(dty) == 2:
              dy1 = int(dty[0])
              dy2 = int(dty[1])
              jdom = random.randint(dy1,dy2)
              print(jdom)
            #ast = int(dft)
                
        if dst.lower() == "license":
            print("""!/usr/bin/env python3
 VX Programming Language
 License: VX License v1.0

 You may use, copy, modify, and distribute this software
 under the following conditions:
 - Do not remove or alter the variable system (memory, var, execute_l)
 - Do not rename the language (keep "VX")
 - Do not claim authorship
 - Attribution to "VX Language" must remain

The author remains anonymous.""")

        if dst_lower.startswith("while "):
            bagian = dst[6:].strip().split(" ", 1)
            if len(bagian) == 2:
                cond = bagian[0]
                ytta = bagian[1]
        
        # Evaluasi kondisi
                loop_active = True
                while loop_active:
            # Cek kondisi setiap kali mau loop
                    if cond.isdigit():
                        if int(cond) == 0:
                            break
                    if cond in memory:
                        if not memory[cond]:
                            break
                    else:
                            break
            
                    execute_l(ytta)
                continue
            # HATI-HATI: Kalau gak ada perubahan kondisi, bakal loop forever!
            # Lo bisa tambahin maksimal loop atau pake tombol Ctrl+C buat berhenti
    
        if dst.lower() in ["quit","exit","q"]:
            break
        
        if not dst:
            continue
               # FOR LOOP MUDAH: for 5 vprint(hi)

        if dst_lower.startswith("vfor "):
            bagian = dst[5:].strip().split(" ", 2)
            if len(bagian) >= 2:
                try:
            # Cek apakah bagian[0] BUKAN angka (berarti itu nama variabel)
                    if not bagian[0].isdigit():
                # Format: for x 5 vprint *(x)*
                        var_name = bagian[0]
                        jumlah = int(bagian[1])
                        prt = bagian[2] if len(bagian) > 2 else ""
                        for val in range(1, jumlah + 1):
                    # Simpan nilai sementara ke variabel, lalu eksekusi
                            memory[var_name] = str(val)
                            execute_l(prt)
                # Hapus variabel temporary (opsional)
                # del memory[var_name]
                    else:
                # Format: for 5 vprint *hi* (tanpa variabel)
                        jumlah = int(bagian[0])
                        prt = bagian[1]
                
                        for _ in range(jumlah):
                            execute_l(prt)
                except ValueError:
                    print("error value")
            else:
                print("error format for")
            
        """
        if "=" in dst_lower and not dst.startswith("vprint"):
            
            hf = dst_lower.split("=", 1)
            
            name = hf[0].strip()
            number = hf[1].strip()
            memory[name] = number
            print(f"[#] {name} = {number}")
            """
        if "=" in dst and not dst_lower.startswith("vprint"):
            hf = dst.split("=", 1)
            name = hf[0].strip()
            expr = hf[1].strip()

    # Coba hitung ekspresi matematika
            try:
        # Ganti (nama_var) dengan nilainya dulu
                for var_name, var_value in memory.items():
                    expr = expr.replace(f"({var_name})", var_value)
        
                result = eval(expr)
                value = str(result)
            except:
        # Kalau gagal, simpan sebagai string biasa
                value = expr
            memory[name] = value
            
        if dst.startswith("vprint") and dst_lower.endswith("*"):
            text = dst_lower.replace("vprint", "").strip().strip("*")
            
    # 2. PRINT: vprint *teks* (bisa pake !variabel)
        if dst.startswith("vprint") and dst_lower.endswith("*"):

            text = dst_lower.replace("vprint", "").strip().strip("*")
        
        # Ganti !nama dengan isi variabel
            for name, number in memory.items():
                text = text.replace(f"({name})", number)
            print(text)

    # 3. PANGGIL variabel (cuma ketik nama)
        if dst_lower in memory:
            print(memory[dst_lower])
            

        if dst.lower() == "vlist":
            if memory:
                for k,n in memory.items():
                    print(f"variabel",str(f"\033[92m{k}\033[0m"))
            else:
                print("0")
            
        if dst_lower.startswith("vdel"):
            nit = dst[4:].strip()
            if nit in memory:
                del memory[nit]
                print(f"delete variabel {nit}")
            else:
                print(f"not found variabel {nit} ")
        if dst.lower() == "vjson":
            rty = input("name file to save: ")
            with open(f"{rty}.json","w") as fil:
                json.dump(memory,fil,indent=2)
            print(f"save file {rty}.json")
        

    except Exception as error:
        print("error",error)
    except KeyboardInterrupt:
          print(dst)
