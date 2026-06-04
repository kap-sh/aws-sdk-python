"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportToTime``."""

import datetime
from typing import TypeAlias

ExportToTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportToTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> ExportToTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
