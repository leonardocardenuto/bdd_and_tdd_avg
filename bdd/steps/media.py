from behave import given, when, then

@given('eu possuo dois números : {num1:d} e {num2:d}')

def step_impl(context, num1, num2):
  context.num1 = num1
  context.num2 = num2

@when('eu somo e divido os números por 2')
def step_impl(context):
  context.resultado = (context.num1 + context.num2)/2

@then('o resultado será {resultado:d}')
def step_impl(context, resultado):
  assert context.resultado == resultado, f"Resultado incorreto. Resultado esperado: {resultado}. Resultado obtido: {context.resultado}"
