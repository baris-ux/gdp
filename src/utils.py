def calculer_moyenne(liste_nombres):
  """
  Calcule la moyenne d'une liste de nombres.

  Args:
    liste_nombres: Une liste de nombres (entiers ou flottants).

  Returns:
    La moyenne des nombres dans la liste.
    Retourne None si la liste est vide.
    Lève une TypeError si un élément de la liste n'est pas un nombre.
  """
  if not liste_nombres:
    return None
  somme = 0
  for nombre in liste_nombres:
    if not isinstance(nombre, (int, float)):
      raise TypeError("La liste doit contenir uniquement des nombres.")
    somme += nombre
  return somme / len(liste_nombres)

def convertir_temperature(temperature, unite_source, unite_cible):
  """
  Convertit une température d'une unité à une autre (Celsius, Fahrenheit, Kelvin).

  Args:
    temperature: La température à convertir.
    unite_source: L'unité de température source ('C', 'F', 'K').
    unite_cible: L'unité de température cible ('C', 'F', 'K').

  Returns:
    La température convertie.
    Lève une ValueError si les unités ne sont pas valides.
  """
  if unite_source not in ('C', 'F', 'K') or unite_cible not in ('C', 'F', 'K'):
    raise ValueError("Unités de température non valides. Utilisez 'C', 'F' ou 'K'.")

  if unite_source == unite_cible:
    return temperature

  if unite_source == 'C':
    if unite_cible == 'F':
      return (temperature * 9/5) + 32
    elif unite_cible == 'K':
      return temperature + 273.15
  elif unite_source == 'F':
    if unite_cible == 'C':
      return (temperature - 32) * 5/9
    elif unite_cible == 'K':
      return (temperature - 32) * 5/9 + 273.15
  elif unite_source == 'K':
    if unite_cible == 'C':
      return temperature - 273.15
    elif unite_cible == 'F':
      return (temperature - 273.15) * 9/5 + 32

  return None # Ne devrait jamais arriver si la logique est correcte changement
