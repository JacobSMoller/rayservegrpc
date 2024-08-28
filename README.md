# rayservegrpc
tiny helloworld grpc service using ray serve


```bash
ray start --head
serve start --grpc-port 9000 --grpc-servicer-function example_pb2_grpc.add_ExampleServiceServicer_to_server
serve deploy model_grpc.deploy
python grpc_client.py
```
