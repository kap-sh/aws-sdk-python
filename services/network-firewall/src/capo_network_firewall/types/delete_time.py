"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteTime``."""

import datetime
from typing import TypeAlias

DeleteTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> DeleteTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
