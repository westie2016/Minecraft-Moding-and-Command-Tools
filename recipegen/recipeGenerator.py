

def testfor(stuff, value):
    re = False
    i = 0
    while i < len(stuff):
        if stuff[i] == value:
            re = True
        i += 1
    return re


def getKeys(string1, string2, string3):
    string = string1 + string2 + string3
    keys = []
    i = 0
    while i < len(string):
        if (string[i] != ' ') and (testfor(keys, string[i]) != True):
            keys.append(string[i])
        i += 1
    return keys


def defineKeyItem(key):
    id = input("Please enter the item id for key " + key + ":")
    return [key, id]


def defineKeys(keys):
    i = 0
    definedKeys = []
    while i < len(keys):
        definedKeys.append(defineKeyItem(keys[i]))
        i += 1
    return definedKeys

def compileRecipe(Isshaped, group):
  r1 = input("Please enter row 1: ")
  r2 = input("Please enter row 2: ")
  r3 = input("Please enter row 3: ")
  if Isshaped:
      recipe = '{ "type": "minecraft:crafting_shaped", "pattern": [ "'+r1+'", "'+r2+'", "'+r3+'" ],'
      i = 0
      recipe = recipe + ' "key": { '
      itemk = defineKeys(getKeys(r1, r2, r3))
      while i < len(itemk):
          if not i < len(itemk) - 1:
            recipe = recipe + '"' + itemk[i][0] + '": { "item": "' + itemk[i][1] + '" } }, '
          else:
            recipe = recipe + '"' + itemk[i][0] + '": { "item": "' + itemk[i][1] + '" }, '
          i += 1
      recipe = recipe + '"result": {'
      rid = input("Please enter result item id: ")
      rd = input("Please enter result data: ")
      rc = input("Please enter result count: ")
      recipe = recipe + '"item": "'+rid+'", "data": '+rd+', "count": '+rc+"} }"
  return recipe


r = compileRecipe(True, None)
name = input("please enter the name of your recipe file: ")
file = open(name + '.json', 'w')
file.write(r)
file.close()
