from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.models import inlineformset_factory, formset_factory

from recipe_app.models import Ingredient, Recipe, RecipeRating, UserProfile, MealType, MEASUREMENTUNIT_CHOICES


class MealTypeForm(forms.Form):
    mt_field = forms.ModelMultipleChoiceField(queryset=MealType.objects.all, widget=forms.CheckboxSelectMultiple)


class SearchRecipeForm(forms.TextInput):
    class Meta:
        model = Recipe
        fields = ['title', 'meal_type', 'ingredients',]


class RatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['recipe', 'rating', ]

"""

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', ]

"""

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'description', 'meal_type', 'directions', ]
        #if using multiple forms, I will remove some fields i.e.measurement, ingredients, title


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

"""
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
"""

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

IngredientFormSet = inlineformset_factory(
    Recipe, Ingredient, extra=5, can_delete=False, min_num=1,
    fields=('quantity', 'measurement_unit', 'ingredient_name')
    )
