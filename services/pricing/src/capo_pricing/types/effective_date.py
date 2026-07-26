"""Generated from Smithy shape ``com.amazonaws.pricing#EffectiveDate``."""

import datetime
from typing import TypeAlias

EffectiveDate: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EffectiveDate) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> EffectiveDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
