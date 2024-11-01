from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class EquipoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    costo = FloatField('Costo', validators=[DataRequired()])
    modelo = SelectField('Modelo', coerce=int)
    categoria = SelectField('Categoría', coerce=int)
    submit = SubmitField('Guardar')
class ModeloForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    fabricante_id = SelectField('Fabricante', coerce=int)
    submit = SubmitField('Guardar')
