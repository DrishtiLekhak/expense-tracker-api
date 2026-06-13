from rest_framework import serializers

from .models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]
    
    def validate(self, data):
        user = self.context['request'].user
        if Category.objects.filter(user=user, name=data['name']).exists():
            raise serializers.ValidationError("Category already exists for this user.")
        return data


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "title", "amount","currency", "category", "date", "notes"]
