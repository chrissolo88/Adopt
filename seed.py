from models import Pet, Specie, db
from app import app


db.drop_all()
db.create_all()

p1 = Pet(name="Rudolph",specie_id=1,age=88,photo_url="https://render.fineartamerica.com/images/rendered/search/print/8/6/break/images/artworkimages/medium/1/rudolph-carrie-ann-grippo-pike.jpg",notes="Seasonal Adoption Only",available=True)
p2 = Pet(name="Hershey",specie_id=2,age=16,photo_url="https://californiapuppiesforsale.com/wp-content/themes/mega-theme2/images/poodle8.jpg",notes="Elderly Chocolate mini-poodle",available=True)
p3 = Pet(name="Hercules",specie_id=3,age=2,photo_url="https://s36537.pcdn.co/wp-content/uploads/2018/03/Calico-cat.jpg.optimal.jpg",notes="Calico cat very friendly",available=True)
p4 = Pet(name="Hamtaro",specie_id=4,age=1,photo_url="https://www.westchathamvet.com/wp-content/uploads/2022/03/guinea-pigs.jpg",notes="Previous child owner wanted hamster",available=True)
p5 = Pet(name="Fabio",specie_id=5,age=4,photo_url="https://www.ntu.ac.uk/__data/assets/image/0035/884573/Otis-Havana.jpg",notes="Lazy Rabbit loves sunbathing",available=True)

s1 = Specie(specie="Reindeer")
s2 = Specie(specie="Dog")
s3 = Specie(specie="Cat")
s4 = Specie(specie="Guinea Pig")
s5 = Specie(specie="Rabbit")
s6 = Specie(specie="Horse")
s7 = Specie(specie="Ferret")


db.session.add_all([s1,s2,s3,s4,s5])

db.session.commit()

db.session.add_all([p1,p2,p3,p4,p5])

db.session.commit()
