import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            '25:onMode = off',
            '25:oneChannel = 1 1 100 5 -5', # H -> b b~
            '25:onIfMatch = 5 -5',
            '35:oneChannel = 1 1 100 6 -6', # Y -> t t~
            '35:onMode = off',
            '35:onIfMatch = 6 -6',
            '24:mMin = 0.05', # the lower limit of the allowed mass range generated by the Breit-Wigner (in GeV)
            '24:onMode = off', # Turn off all W decays
            '24:onIfAny = 1 2 3 4 5', # W->qq decays 
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'processParameters')
    )
)

