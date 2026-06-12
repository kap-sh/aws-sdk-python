"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceCreationTime``."""

import datetime
from typing import TypeAlias

ResourceCreationTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCreationTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ResourceCreationTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
