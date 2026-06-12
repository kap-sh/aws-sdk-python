"""Generated from Smithy shape ``com.amazonaws.transfer#DateImported``."""

import datetime
from typing import TypeAlias

DateImported: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DateImported) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> DateImported:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
