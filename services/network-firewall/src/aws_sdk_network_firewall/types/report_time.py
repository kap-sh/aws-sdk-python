"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ReportTime``."""

import datetime
from typing import TypeAlias

ReportTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReportTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> ReportTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
