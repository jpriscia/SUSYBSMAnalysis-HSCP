import sys, os
import FWCore.ParameterSet.Config as cms

isSignal = False
isBckg = True
isData = False
isSkimmedSample = False
GTAG = 'MCRUN2_74_V7::All'
OUTPUTFILE = 'HSCP.root'

#debug input files 
#this list is overwritten by CRAB
InputFileList = cms.untracked.vstring(
'/store/relval/CMSSW_7_4_0/RelValZMM_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7_GENSIM_7_1_15-v1/00000/0C579384-8EDD-E411-B509-0025905A611C.root',
'/store/relval/CMSSW_7_4_0/RelValZMM_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7_GENSIM_7_1_15-v1/00000/101AC681-88DD-E411-AF23-0025905A60B0.root',
'/store/relval/CMSSW_7_4_0/RelValZMM_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7_GENSIM_7_1_15-v1/00000/28FC8724-89DD-E411-BE77-002618943833.root',
'/store/relval/CMSSW_7_4_0/RelValZMM_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7_GENSIM_7_1_15-v1/00000/841142E3-8ADD-E411-88A7-002618943833.root',
'/store/relval/CMSSW_7_4_0/RelValZMM_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7_GENSIM_7_1_15-v1/00000/8C9E8C6F-8DDD-E411-8B03-0025905A48FC.root',
'/store/relval/CMSSW_7_4_0/RelValZMM_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7_GENSIM_7_1_15-v1/00000/BE96FFAA-87DD-E411-986A-0025905A48FC.root',
'/store/relval/CMSSW_7_4_0/RelValZMM_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7_GENSIM_7_1_15-v1/00000/C4388E70-90DD-E411-960A-002590593878.root',
'/store/relval/CMSSW_7_4_0/RelValZMM_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7_GENSIM_7_1_15-v1/00000/EC182626-86DD-E411-838F-0025905A60B0.root',
'/store/relval/CMSSW_7_4_0/RelValZMM_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7_GENSIM_7_1_15-v1/00000/F6CBEF71-90DD-E411-B734-0025905A60CE.root',
)

#main EDM tuple cfg that depends on the above parameters
execfile( os.path.expandvars('${CMSSW_BASE}/src/SUSYBSMAnalysis/HSCP/test/MakeEDMtuples/HSCParticleProducer_cfg.py') )
