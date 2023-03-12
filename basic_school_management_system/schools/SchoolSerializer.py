from rest_framework import serializers
from .models import *

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = school
        # fields = ['name','email','city','pin_code','password']
        exclude = ['id']
        # fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = sutudent
        # fields = ['name','user_name','password','grade','school']
        fields = '__all__'

    def validate(self, data):
        
        if data['grade'] not in range(1,13):
            raise serializers.ValidationError({"eror":"Grage should be betwwen 1-12"})
        
        return data 