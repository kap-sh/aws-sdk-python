"""Generated from Smithy shape ``com.amazonaws.fsx#CreationTime``."""

import datetime
from typing import TypeAlias

"""<p>The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.</p>"""
CreationTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreationTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> CreationTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
