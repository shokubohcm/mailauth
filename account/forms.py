from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model # ユーザーモデルを取得するため


# ユーザーモデル取得
User = get_user_model()


'''ログイン用フォーム'''
class LoginForm(AuthenticationForm):

    # bootstrap4対応
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる


'''サインアップ用フォーム'''
class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email','username', )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = '' # 全フィールドを入力必須

            # オートフォーカスとプレースホルダーの設定
            print(field.label)
            if field.label == 'Last Name':
                field.widget.attrs['autofocus'] = '' # 入力可能状態にする
                field.widget.attrs['placeholder'] = 'Tanaka'
            elif field.label == 'First Name':
                field.widget.attrs['placeholder'] = 'Taro'
            elif field.label == 'Mail Address':
                field.widget.attrs['placeholder'] = '***@gmail.com'

'''ユーザー情報更新用フォーム'''
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'username',)

    # bootstrap4対応
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = '' # 全フィールドを入力必須

'''パスワード変更フォーム'''
class MyPasswordChangeForm(PasswordChangeForm):

    # bootstrap4対応で、classを指定
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'