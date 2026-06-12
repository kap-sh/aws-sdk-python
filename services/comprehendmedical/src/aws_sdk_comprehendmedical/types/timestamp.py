"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#Timestamp``."""

import datetime
from typing import TypeAlias

Timestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Timestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> Timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
