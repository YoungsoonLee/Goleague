echo ">> test"
python3 manage.py test

echo ">> insert init four data"
curl http://127.0.0.1:8000/todos/ --header "Content-Type: application/json" -d '{"text":"test100", "due_date": "2018-09-09 00:00:00"}' -X POST | python3 -m "json.tool"
curl http://127.0.0.1:8000/todos/ --header "Content-Type: application/json" -d '{"text":"test200", "due_date": "2018-09-10 00:00:00"}' -X POST | python3 -m "json.tool"
curl http://127.0.0.1:8000/todos/ --header "Content-Type: application/json" -d '{"text":"test300", "due_date": "2018-09-10 00:00:00", "done_state": "True"}' -X POST | python3 -m "json.tool"
curl http://127.0.0.1:8000/todos/ --header "Content-Type: application/json" -d '{"text":"test400", "due_date": "2018-10-10 00:00:00"}' -X POST | python3 -m "json.tool"

echo ">> query all todos"
curl http://127.0.0.1:8000/todos/ | python3 -m "json.tool"


echo ">> patah a todos with id 1"
curl http://127.0.0.1:8000/todos/1/ --header "Content-Type: application/json" -d '{"text":"test111", "due_date": "2018-10-10 00:00:00", "done_state": "True"}' -X PATCH | python3 -m "json.tool"

echo ">> delete a todos with id 1"
curl http://127.0.0.1:8000/todos/1/ - X DELETE | python3 -m "json.tool"


echo ">> filter a todos with done_state=True"
curl http://127.0.0.1:8000/search?done_state=True | python3 -m "json.tool"


echo ">> filter a todos with du_date=2018-09-09 00:00:00"
curl http://127.0.0.1:8000/search?due_date="2018-09-09T00:00:00Z" | python3 -m "json.tool"

echo ">> filter a todos with done_state=False and du_date=2018-09-10 00:00:00"
curl http://127.0.0.1:8000/search?done_state=False&due_date="2018-09-10T00:00:00Z" | python3 -m "json.tool"

