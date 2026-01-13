from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],  # список валидаторов
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")

    def create(self, validated_data):
        # Используем create_user, чтобы пароль захешировался правильно
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        return user

    def validate_email(self, value):
        """
        Check that the email is valid.
        """
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Этот email уже используется")
        return value
