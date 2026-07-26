"""Generated from Smithy shape ``com.amazonaws.pi#ISOTimestamp``."""

import datetime
from typing import TypeAlias

ISOTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ISOTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ISOTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
