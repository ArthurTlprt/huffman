##
#   Affiche les feuilles de l'arbre : la lettre et son code associé
def dispCode(node):
    if "right" not in node:
        print "letter: " + node["letter"] + " = " + node["bin"]
    else:
        dispCode(node["right"])
        dispCode(node["left"])

##
#   Code les lettres
def encode(node, code):
    node["bin"] = code
    if "left" in node:
        encode(node["left"], code + "0")
    if "right" in node:
        encode(node["right"], code + "1")
    return

##
#   Crée une liste d'objet trié en fonction du nombre d'occurence des lettres de noeuds fils
def setList(text, oc):
    for l in text:
        if {"letter": l, "count": text.count(l), "bin" : None} not in oc:
            oc.append({"letter": l, "count": text.count(l), "bin" : None})
    oc = sorted(oc, key=lambda k: k['count'])
    oc.reverse()

def main():
    text = raw_input()
    oc = []

    # Crée l'arbre, associe les neouds de poids les plus faibles ensemble
    while len(oc) != 1:
        m_node = {"bin" : None, "count" : None, "left": None, "right": None}
        m_node["left"] = oc.pop()
        m_node["right"] = oc.pop()
        m_node["count"] = m_node["left"]["count"] + m_node["right"]["count"]
        oc.append(m_node)
        oc = sorted(oc, key=lambda k: k['count'])
        oc.reverse()

    root = oc.pop()
    encode(root["left"], "0")
    encode(root["right"], "1")
    dispCode(root)


if __name__ == "__main__":
    main()
