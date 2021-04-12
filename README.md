# Fundgrube-Finder
Durchsucht Fundgruben von Saturn / MediaMarkt nach bestimmten Produkten

## Nutzung

* In den Fundgruben von [Saturn](https://www.saturn.de/de/shop/fundgrube.html) oder [MediaMarkt](https://www.mediamarkt.de/de/shop/fundgrube.html) einen Shop suchen, auswählen und die ID aus der URL notieren (z. B. Köln City = 310)
* Shop unter `targets` einfügen
* Produkte, die gefunden werden sollen, zu `looking_for` hinzufügen. Suchwörter, die zusammen auftreten sollen, in einem String durch Leereichen trennen. Groß-/Kleinschreibung wird ignoriert (z. B. "Canon EOS 90D" findet die gleichen Ergebnisse wie "EOS CANON 90d")
