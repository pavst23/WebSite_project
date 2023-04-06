from flask import Flask, request, url_for
import json

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации на мероприятие</h1>
                            <div class="alert alert-danger" role="alert">
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="name" class="form-control" id="name" placeholder="Введите ФИО" name="name">
                                    <input type="age" class="form-control" id="age" placeholder="Введите дату рождения" name="age">
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <input type="event" class="form-control" id="age" placeholder="Введите название интересуемого мероприятия" name="event">
                                    <div class="form-group">
                                        <label for="classSelect">Укажите удобное для вас время</label>
                                        <select class="form-control" id="classSelect" name="time">
                                          <option>0:00</option>
                                          <option>0:30</option>
                                          <option>1:00</option>
                                          <option>1:30</option>
                                          <option>2:00</option>
                                          <option>2:30</option>
                                          <option>3:00</option>
                                          <option>3:30</option>
                                          <option>4:00</option>
                                          <option>4:30</option>
                                          <option>5:30</option>
                                          <option>6:30</option>
                                          <option>7:00</option>
                                          <option>7:30</option>
                                          <option>8:30</option>
                                          <option>9:00</option>
                                          <option>9:30</option>
                                          <option>10:00</option>
                                          <option>10:30</option>
                                          <option>11:00</option>
                                          <option>11:30</option>
                                          <option>12:00</option>
                                          <option>12:30</option>
                                          <option>13:00</option>
                                          <option>13:30</option>
                                          <option>14:00</option>
                                          <option>14:30</option>
                                          <option>15:00</option>
                                          <option>15:30</option>
                                          <option>16:00</option>
                                          <option>16:30</option>
                                          <option>17:00</option>
                                          <option>17:30</option>
                                          <option>18:00</option>
                                          <option>18:30</option>
                                          <option>19:30</option>
                                          <option>20:00</option>
                                          <option>20:30</option>
                                          <option>21:00</option>
                                          <option>21:30</option>
                                          <option>22:00</option>
                                          <option>22:30</option>
                                          <option>23:00</option>
                                          <option>23:30</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите попасть на это мероприятие</label>
                                        <textarea class="form-control" id="about" rows="3" name="about2"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите вашу фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js" 
                            integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" 
                            crossorigin="anonymous"></script>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        result = {
                     request.form['name']: [request.form['email'], request.form['age'], request.form['sex'],
                                            request.form['time'], request.form['about'], request.form['about2'],
                                            request.form['file']]
        }
        json.dump(result, open('res.json', 'w'))
        # print(request.form['email'])
        # print(request.form['name'])
        # print(request.form['age'])
        # print(request.form['sex'])
        # print(request.form['time'])
        # print(request.form['about'])
        # print(request.form['about2'])
        # print(request.form['file'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')