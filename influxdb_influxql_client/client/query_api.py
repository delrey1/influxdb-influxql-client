import requests

from influxdb_influxql_client.client.models.Results import ResultsModel


class QueryApi:
    def __init__(self, influxdb_client):
        self._influxdb_client = influxdb_client

    def _query(self, query: str):
        response: requests.Response = self._influxdb_client.sh.get("query", params={
            'q': query,
            'db': self._influxdb_client.database
        })

        assert response.status_code == 200, "Unexpected Response code from Influx Client: {}".format(
            response.status_code)
        return response

    def query(self, query: str) -> ResultsModel:
        response = self._query(query)

        results = ResultsModel(**response.json())

        return results

    def query_raw(self, query: str):
        return self._query(query).content
