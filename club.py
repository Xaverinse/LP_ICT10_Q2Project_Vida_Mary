from pyscript import document

clubs = {
    "heartslabyul": "<h3>Heartslabyul Dorm</h3><p>Order and rules.</p>",
    "savanaclaw": "<h3>Savanaclaw Dorm</h3><p>Strength and pride.</p>",
    "octavinelle": "<h3>Octavinelle Dorm</h3><p>Business and cunning.</p>",
    "scarabia": "<h3>Scarabia Dorm</h3><p>Ambition and hospitality.</p>",
    "pomefiore": "<h3>Pomefiore Dorm</h3><p>Beauty and elegance.</p>",
    "ignihyde": "<h3>Ignihyde Dorm</h3><p>Technology and isolation.</p>",
    "diasomnia": "<h3>Diasomnia Dorm</h3><p>Magic and nobility.</p>",
    "ramshackle": "<h3>Ramshackle Dorm</h3><p>Ghosts and chaos.</p>",
}

def show(club):
    div = document.getElementById("Clubs")
    div.innerHTML = clubs[club]

def hear(): show("heartslabyul")
def sava(): show("savanaclaw")
def octa(): show("octavinelle")
def scar(): show("scarabia")
def pome(): show("pomefiore")
def igni(): show("ignihyde")
def dias(): show("diasomnia")
def rams(): show("ramshackle")
