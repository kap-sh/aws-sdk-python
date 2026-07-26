"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationTimestamp``."""

import datetime
from typing import TypeAlias

IntegrationTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> IntegrationTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
