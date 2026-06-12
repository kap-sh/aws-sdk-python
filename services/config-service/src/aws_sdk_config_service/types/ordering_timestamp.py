"""Generated from Smithy shape ``com.amazonaws.configservice#OrderingTimestamp``."""

import datetime
from typing import TypeAlias

OrderingTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrderingTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> OrderingTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
