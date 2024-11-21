def GenerateFunc(jobNum, timeDeltaVal, timeDeltaName, waveName, DEL, STOP):
    s = f'waveVsWave(?x xval(leafValue( clipX({waveName} {DEL} {STOP} ) "N" 1 )) + 0 ?y leafValue( {waveName} "N" 1 ))'
    for job in range(2, jobNum+1):
        s += f' + waveVsWave(?x xval(leafValue( {waveName} "N" {job} )) + {timeDeltaVal*(job-1)}{timeDeltaName} ?y leafValue( {waveName} "N" {job} ))'
    return s

def Gen2(jobNum, waveName, startJob, endJob, deltaTime, deltaTimeMeas):
    s = f'waveVsWave(?x xval(clip(leafValue( {waveName} "N" 1 ) {startJob} {endJob} ?interpolate nil)) + 0 ?y clip(leafValue( {waveName} "N" 1 ) {startJob} {endJob} ?interpolate nil))'
    for job in range(2, jobNum+1):
        s += f' + waveVsWave(?x xval(clip(leafValue( {waveName} "N" {job} ) {startJob} {endJob} ?interpolate nil)) + {deltaTime*(job-1)}{deltaTimeMeas} ?y clip(leafValue( {waveName} "N" {job} ) {startJob} {endJob} ?interpolate nil))'
    return s
    
if __name__ == "__main__":
    # print(GenerateFunc(64, 5.12, 'm', 'VT("/sin")', 0.00021, 0.00532))
    print(Gen2(64, 'SAMPLE', 0.00021001, 0.00532001, 5.12, 'm'))
