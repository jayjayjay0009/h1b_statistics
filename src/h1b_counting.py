import sys

def main():
    H1bInputCSVFilePath = sys.argv[1]
    Top10OccupationsTXTFilePath = sys.argv[2]
    Top10StatesTXTFilePath = sys.argv[3]
    
    h1bInputCSVFile = open(sys.argv[1],'r')
    
    top10OccupationsTXTFile = open(sys.argv[2],'w')
    top10OccupationsTXTFile.write('11223344')
    top10OccupationsTXTFile.close()

    Top10StatesTXTFilePath = open(sys.argv[3],'w')
    Top10StatesTXTFilePath.write('11223344')
    Top10StatesTXTFilePath.close()

main()
