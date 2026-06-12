"""Generated from Smithy shape ``com.amazonaws.machinelearning#EpochTime``."""

import datetime
from typing import TypeAlias

"""<p>A timestamp represented in epoch time.</p>"""
EpochTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EpochTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> EpochTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
