from flask import Flask
from flask import render_template
from data import db_session
from data.users import User
from data.jobs import Job
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init(f"db/mars_explorer.db")
db_sess = db_session.create_session()

def main():
    app.run()

    # db_session.global_init(f"db/mars_explorer.db")
    # job = Job()
    # job.team_leader = 1
    # job.job = 'Do something'
    # job.work_size = 20
    # job.collaborators = '2, 3'
    # job.is_finished = False
    # db_sess.add(job)
    # db_sess.commit()
    # db_sess = db_session.create_session()
    # surnames = ['Scott', 'Smith', 'Kim', 'Garcia']
    # names = ['Ridley', 'Liam', 'Sakura', 'Mohamed']
    # ages = [21, 22, 23, 24]
    # positions = ['captain', 'worker', 'worker', 'worker']
    # specialities = ['research engineer', 'engineer', 'engineer', 'engineer']
    # addresses = ['module_1', 'module_2', 'module_3', 'module_4']
    # emails = ['scott_chief@mars.org', 'smith_chief@mars.org', 'kim_chief@mars.org', 'garcia_chief@mars.org']
    # for i in range(4):
    #     user = User()
    #     user.surname = surnames[i]
    #     user.name = names[i]
    #     user.age = ages[i]
    #     user.position = positions[i]
    #     user.speciality = specialities[i]
    #     user.address = addresses[i]
    #     user.email = emails[i]
    #     db_sess.add(user)
    #     db_sess.commit()


@app.route("/")
def index():
    jobs = db_sess.query(Job)
    return render_template("index.html", jobs=jobs)


if __name__ == '__main__':
    main()