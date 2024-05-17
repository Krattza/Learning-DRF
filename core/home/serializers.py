from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'age', 'father_name'] # To get specific fields.
        # exclude = ['father_name'] # excludes the given field and returns all other fields.
        # fields = '__all__' # To include all the fields in the model

    def validate(self, data):
        
        if data['age'] < 18:
            raise serializers.ValidationError({'error': 'Age must be over 18'})
            
        return data
    
    def validate_name(self, value):
        # value here is the value of the 'name' field
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError('Numbers not allowed in name')
        return value
    
    # def validate(self, data):
    #     name = list(data)
        
    #     for i in range(0, len(name)):
            
    #         if name[i] == "1":
    #             raise serializers.ValidationError({'error': 'Numbers not allowed in name'})
            
    


    
