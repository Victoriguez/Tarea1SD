import grpc
import Tarea1SD.sala_pb2 as sala_pb2
import Tarea1SD.sala_pb2_grpc as sala_pb2_grpc
import redis

class SalaService(sala_pb2_grpc.SalaServiceServicer):
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    def ObtenerSala(self, request, context):
        # Aquí implementa la lógica para obtener la sala asociada al curso
        curso = request.curso
        sala = self.redis_client.get(curso)
        if sala:
            return sala_pb2.RespuestaSala(sala=sala.decode('utf-8'))
        else:
            return sala_pb2.RespuestaSala(sala="Sala no encontrada")

def run_server():
    server = grpc.server(grpc.ThreadPoolExecutor(max_workers=10))
    sala_pb2_grpc.add_SalaServiceServicer_to_server(SalaService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
