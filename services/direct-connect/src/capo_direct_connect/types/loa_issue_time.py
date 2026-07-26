"""Generated from Smithy shape ``com.amazonaws.directconnect#LoaIssueTime``."""

import datetime
from typing import TypeAlias

LoaIssueTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoaIssueTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LoaIssueTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
