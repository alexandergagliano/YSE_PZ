from django.contrib import admin

# Register your models here.
from YSE_App.models import *

admin.site.register(TransientHostRank)
admin.site.register(TransientStatus)
admin.site.register(FollowupStatus)
admin.site.register(TaskStatus)
admin.site.register(AntaresClassification)
admin.site.register(InternalSurvey)
admin.site.register(ObservationGroup)
admin.site.register(SEDType)
admin.site.register(HostMorphology)
admin.site.register(Phase)
admin.site.register(TransientClass)
admin.site.register(Observatory)
admin.site.register(Telescope)
admin.site.register(Instrument)
admin.site.register(ToOResource)
admin.site.register(ClassicalResource)
admin.site.register(QueuedResource)
admin.site.register(ClassicalObservingDate)
admin.site.register(InstrumentConfig)
admin.site.register(ConfigElement)
admin.site.register(PhotometricBand)
admin.site.register(Host)
admin.site.register(Transient)
admin.site.register(TransientFollowup)
admin.site.register(HostFollowup)
admin.site.register(TransientObservationTask)
admin.site.register(HostObservationTask)
admin.site.register(TransientSpectrum)
admin.site.register(HostSpectrum)
admin.site.register(TransientPhotometry)
admin.site.register(HostPhotometry)
admin.site.register(InformationSource)
admin.site.register(TransientWebResource)
admin.site.register(HostWebResource)
admin.site.register(AlternateTransientNames)
admin.site.register(TransientSpecData)
admin.site.register(HostSpecData)
admin.site.register(TransientPhotData)
admin.site.register(HostPhotData)
admin.site.register(TransientImage)
admin.site.register(ClassicalNightType)
admin.site.register(HostImage)
admin.site.register(HostSED)
admin.site.register(Log)
