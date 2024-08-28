import ray
import requests
from ray import serve
from transformers import pipeline
from google.protobuf.json_format import ParseDict
from example_pb2 import ExampleRequest, ExampleResponse


@serve.deployment(
    num_replicas=2,
    ray_actor_options={"num_cpus": 0.2, "num_gpus": 0},
    route_prefix="/hello_world",
)
class Translator:
    def __init__(self):
        self.model = pipeline("translation_en_to_fr", model="t5-small")

    async def Examplefoo(self, example_request: ExampleRequest) -> ExampleResponse:

        english_text = example_request.word  # Await the request to get the JSON data
        translated_text = self.model(english_text)[0]["translation_text"]
        return ExampleResponse(translation=translated_text)


deploy = Translator.bind()
