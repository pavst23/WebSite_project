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
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_2.css')}"/>
                            <title>Пример формы</title>
                          </head>
                          <body>
                            
                            <div class="alert alert-success" role="alert">
                                <form class="login_form" method="post">
                                    <h1>Регистрация на мероприятие</h1>
                                    <h2>В этом сайте вы сможете зарегистрироваться на мероприятия, которые вам интересны</h2>
                                    <button type="submit" class="btn btn-primary">Пройти регистрацию</button>
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
    app.run(port=8080, host='127.0.0.2')