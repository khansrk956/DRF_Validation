from rest_framework import serializers
from . models import Student

def start_with_r(value):
    if value[0].lower() !='r':
        raise serializers.ValidationError('Name should be start with R')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    sr_no = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    # Create
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # update
    def update(self, instance, validata_data):
        print(instance.name)
        instance.name = validata_data.get('name',instance)
        print(instance.name)
        instance.city = validata_data.get('city', instance)
        instance.save()
        return instance
    

    # Field Level Validation. When we validate single field.
    def validate_sr_no(self, value):
        if value >= 120:
            raise serializers.ValidationError('No More Serial Number Available.')
        return value
    
    # Object level Validation. When we validate more than one field.

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'sharukh' and ct.lower() != 'faridabad':
            raise serializers.ValidationError('City must be faridabad')
        return data
    



    

