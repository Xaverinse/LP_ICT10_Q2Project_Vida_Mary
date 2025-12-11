from pyscript import document

clubs = {
    "heartslabyul": "<h3>Heartslabyul</h3><p>A dorm based on the Queen of Hearts' spirit of strictness.</p> <p>Housewarden: Riddle Rosehearts</p><p> Twisted from Alice in Wonderland</p>",
    "savanaclaw": "<h3>Savanaclaw Dorm</h3><p>A dorm based on the King of Beasts' spirit of persistence.</p><p>Housewarden: Leona Kingscholar</p><p> Twisted from The Lion King</p>",
    "octavinelle": "<h3>Octavinelle Dorm</h3><p>A dorm based on the Sea Witch's spirit of benevolence.</p><p>Housewarden: Azul Ashengrotto</p><p> Twisted from The Little Mermaid</p>",
    "scarabia": "<h3>Scarabia Dorm</h3><p>A dorm based on the Sorcerer of the Sands' spirit of mindfulness.</p><p>Housewarden: Kalim Al-Asim</p><p> Twisted from Aladdin</p>",
    "pomefiore": "<h3>Pomefiore Dorm</h3><p>A dorm based on the Fairest Queen's spirit of tenacity.</p><p>Housewarden: Vil Schoenheit</p><p> Twisted from Snow White</p>",
    "ignihyde": "<h3>Ignihyde Dorm</h3><p>A dorm based on the King of the Underworld's spirit of diligence.</p> <p>Housewarden: Idia Shroud</p><p> Twisted from Hercules</p>",
    "diasomnia": "<h3>Diasomnia Dorm</h3><p>A dorm based on the Thorn Fairy's spirit of nobility.</p> <p>Housewarden: Malleus Draconia</p><p> Twisted from Sleeping Beauty</p>",
    "ramshackle": "<h3>Ramshackle Dorm</h3><p>Dorm was once abandoned and haunted by ghosts until Yuu and Grim move in.</p> <p>Housewarden: Yuu (the Protagonist)</p><p> From Twisted Wonderland</p>",
}

def show(club):
    div = document.getElementById("Clubs")
    if not div:
        return
    html = clubs.get(club, "<p>HOW DID YOU GET HERE???</p>")
    div.innerHTML = html

def hear(e=None): show("heartslabyul")
def sava(e=None): show("savanaclaw")
def octa(e=None): show("octavinelle")
def scar(e=None): show("scarabia")
def pome(e=None): show("pomefiore")
def igni(e=None): show("ignihyde")
def dias(e=None): show("diasomnia")
def rams(e=None): show("ramshackle")



