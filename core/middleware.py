
class DatabaseHandler:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
    
    def __call__(self, request):
        from django.db import connections
        connections.databases['default']['NAME']=request.headers['Database']
        from django.db.utils import OperationalError
        db_conn = connections['default']
        try:
            c = db_conn.cursor()
        except OperationalError:
            connected = False
        else:
            connected = True
        response = self.get_response(request)
        return response
    