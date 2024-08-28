import grpc
from example_pb2 import ExampleRequest
from example_pb2_grpc import ExampleServiceStub


channel = grpc.insecure_channel("localhost:9000")
stub = ExampleServiceStub(channel)
request = ExampleRequest(word="Hello world")

response, call = stub.Example.with_call(request=request)
print(f"status code: {call.code()}")  # grpc.StatusCode.OK
print(f"greeting: {response.translation}")  # "bar"
