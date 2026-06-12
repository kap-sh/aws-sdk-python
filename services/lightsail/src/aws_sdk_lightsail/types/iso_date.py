"""Generated from Smithy shape ``com.amazonaws.lightsail#IsoDate``."""

import datetime
from typing import TypeAlias

IsoDate: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsoDate) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> IsoDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
