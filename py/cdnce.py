def GenerateFunc(jobNum, timeDeltaVal, timeDeltaName, waveName):
    s = f'waveVsWave(?x xval(leafValue( {waveName} "N" 1 )) + 0 ?y leafValue( {waveName} "N" 1 ))'
    for job in range(2, jobNum+1):
        s += f' + waveVsWave(?x xval(leafValue( {waveName} "N" {job} )) + {timeDeltaVal*(job-1)}{timeDeltaName} ?y leafValue( {waveName} "N" {job} ))'
    return s

if __name__ == "__main__":
    print(GenerateFunc(30, 8, 'm', 'ADC_OUT_POINTS'))