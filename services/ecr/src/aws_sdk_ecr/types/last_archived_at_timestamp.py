"""Generated from Smithy shape ``com.amazonaws.ecr#LastArchivedAtTimestamp``."""

import datetime
from typing import TypeAlias

LastArchivedAtTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastArchivedAtTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastArchivedAtTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
