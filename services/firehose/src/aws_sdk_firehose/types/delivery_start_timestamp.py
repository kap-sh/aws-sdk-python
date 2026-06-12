"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStartTimestamp``."""

import datetime
from typing import TypeAlias

DeliveryStartTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryStartTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> DeliveryStartTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
