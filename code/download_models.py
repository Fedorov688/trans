import multiprocessing
from transformers import AutoTokenizer, AutoModelForMaskedLM, AutoModel
import requests


class Models:

    url = "https://huggingface.co/api/models"
    specs = []
    tasks = 0

    def __init__(self):
        response = requests.request("GET", self.url)
        self.specs = response.json()

    @staticmethod
    def _download_m(model_name):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        m = AutoModel.from_pretrained(model_name)

    def create_tasks(self, model_implication):
        pool = multiprocessing.Pool()
        for model in self.specs:
            if model_implication in model["modelId"]:
                print("Download " + model["modelId"] + "\n")
                # self.tasks.append(
                self.tasks += 1
                pool.apply_async(self._download_m,
                                 args=(
                                     model["modelId"],
                                       )
                                 )
        pool.close()
        pool.join()
        print(self.tasks)


if __name__ == '__main__':
    ms = Models()
    ms.create_tasks("Helsinki-NLP/")
