"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GenericTimeStamp``."""

import datetime
from typing import TypeAlias

GenericTimeStamp: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GenericTimeStamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> GenericTimeStamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
