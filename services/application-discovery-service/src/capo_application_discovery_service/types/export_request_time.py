"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportRequestTime``."""

import datetime
from typing import TypeAlias

ExportRequestTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportRequestTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ExportRequestTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
