from ..models import Measurement
from variables.models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    return measurement

def update_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    var = Variable.objects.get(pk=new_measurement["variable"])
    measurement.variable = var
    measurement.value = new_measurement["value"]
    measurement.unit = new_measurement["unit"]
    measurement.place = new_measurement["place"]
    measurement.save()
    return measurement

def create_measurement(measurement):
    var = Variable.objects.get(pk=measurement["variable"])
    measure = Measurement(variable =var, value=measurement["value"], unit=measurement["unit"], place=measurement["place"])
    measure.save()
    return measure

def delete_measurement(measurement_pk):
    measurement = get_measurement(measurement_pk)
    measurement.delete()
    return measurement
