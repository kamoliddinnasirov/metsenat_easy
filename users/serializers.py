from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'role']
        extra_kwargs = {'password':{"write_only":True}} #uyga vazifa


        def create(self, validate_data):
            user = User(
                email = validate_data['email'],
                username = validate_data['username'],
                role = validate_data['role']
            )

            user.set_password(validate_data['password'])
            user.save()
            return user 