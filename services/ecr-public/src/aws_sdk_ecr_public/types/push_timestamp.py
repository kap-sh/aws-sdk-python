"""Generated from Smithy shape ``com.amazonaws.ecrpublic#PushTimestamp``."""

import datetime
from typing import TypeAlias

PushTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PushTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> PushTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
