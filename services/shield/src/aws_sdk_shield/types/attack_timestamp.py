"""Generated from Smithy shape ``com.amazonaws.shield#AttackTimestamp``."""

import datetime
from typing import TypeAlias

AttackTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> AttackTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
