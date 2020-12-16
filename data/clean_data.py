import  csv

with open('./game_new.csv','w',encoding='utf-8',newline="") as w_f:
    writer=csv.writer(w_f)
    with open('./game.csv',encoding='utf-8') as f:
        reader=csv.reader(f)
        header=next(reader)
        writer.writerow(header)
        for line in reader:
            line[2]=line[2].split(",")[-1]
            print(line)
            writer.writerow(line)
