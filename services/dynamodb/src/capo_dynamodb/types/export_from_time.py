"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportFromTime``."""

import datetime
from typing import TypeAlias

ExportFromTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportFromTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> ExportFromTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
