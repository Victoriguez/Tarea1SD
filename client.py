import grpc
import Tarea1SD.sala_pb2 as sala_pb2
import Tarea1SD.sala_pb2_grpc as sala_pb2_grpc

def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = sala_pb2_grpc.SalaServiceStub(channel)
    response = stub.ObtenerSala(sala_pb2.SolicitudSala(curso="Curso XYZ"))
    print("Sala:", response.sala)

if __name__ == '__main__':
    run_client()
