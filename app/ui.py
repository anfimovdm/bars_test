from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext
import datetime


class UserAddEditWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddEditWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label='password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label='last login',
            name='last login',
            anchor='100%',
            format='d.m.Y')

        self.field__su_status = ext.ExtCheckBox(
            label='active',
            name='active',
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label='username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__name = ext.ExtStringField(
            label='first name',
            name='name',
            anchor='100%')

        self.field__surname = ext.ExtStringField(
            label='last name',
            name='surname',
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label='email address',
            name='email',
            anchor='100%')

        self.field__date = ext.ExtDateField(
            label='date joined',
            name='date',
            anchor='100%',
            format='d.m.Y')

        self.field__staff_status = ext.ExtCheckBox(
            label='active',
            name='active',
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label='active',
            name='active',
            checked=True,
            anchor='100%')

        self.field__date = ext.ExtDateField(
            label='date joined',
            name='date',
            format='d.m.Y',
            value=datetime.date.today(),
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__su_status,
            self.field__username,
            self.field__name,
            self.field__surname,
            self.field__email,
            self.field__staff_status,
            self.field__active,
            self.field__date,
        ))

    def set_params(self, params):
        """
        Установка параметров окна
        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddEditWindow, self).set_params(params)
        self.height = 'auto'
