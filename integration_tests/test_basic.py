import os
from unittest import TestCase

from influxdb_influxql_client.client.influxdb_influxql_client import InfluxQLClient


class TestTrack(TestCase):

    def test_basic(self):
        ic = InfluxQLClient(os.getenv("URL"), "telegraf")
        ic.query_api().query(
            """
            SELECT mean(\"usage_guest\") FROM \"cpu\" WHERE time >= now() - 1h and 
            time <= now() GROUP BY time(2s) fill(null)
            """
        )
