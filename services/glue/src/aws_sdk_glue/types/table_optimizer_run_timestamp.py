"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizerRunTimestamp``."""

import datetime
from typing import TypeAlias

TableOptimizerRunTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableOptimizerRunTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> TableOptimizerRunTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
