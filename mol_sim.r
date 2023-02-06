library(Rpi)
library(rcdk)

# DrugBank의 aspirin 구조 정보 sdf format으로 불러옴
asp_mol <- load.molecules('https://go.drugbank.com/structures/small_molecule_drugs/DB00945.sdf')[[1]]
# DrugBank의 aspirin의 target (Prostaglandin G/H synthase 1)을 공통적으로 target으로 하는 다른 molecule (ibuprofen) 구조 정보도 sdf format로 불러옴
ibu_mol <- load.molecules('https://go.drugbank.com/structures/small_molecule_drugs/DB01050.sdf')[[1]]


# Rcpi: 모든 compound를 drug로 지칭하므로, drug 정보를 가져올 때 extractDrug~ function 사용

# Aspirin, ibuprofen에 대해 ECFP 형태로 Fingerprint extraction 하되, bit가 1인 자리만 표시
# 대부분 0인 sparse한 fingerprint라면 이 방법이 더 효율적
ecfp_asp <- extractDrugExtended(asp_mol)  #depth: ECFP-n, size: Fingerprint 길이 
ecfp_ibu <- extractDrugExtended(ibu_mol)

# Aspirin ECFP 형태로 fingerprint extraction 하되, 모든 bit를 다 표시 (함수명: ~Complete)
ecfp_asp_c <- extractDrugExtendedComplete(asp_mol)
ecfp_ibu_c <- extractDrugExtendedComplete(ibu_mol)

# Calculate Drug Fingerprint Similarity - Tanimoto Correlation 계산
calcDrugFPSim(ecfp_asp, ecfp_ibu, 'compact', 'tanimoto') # (mol1, mol2, fingerprint version - compact OR complete, 계산할 것)
calcDrugFPSim(ecfp_asp, ecfp_ibu, 'complete', 'tanimoto')