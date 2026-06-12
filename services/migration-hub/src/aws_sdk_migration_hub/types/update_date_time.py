"""Generated from Smithy shape ``com.amazonaws.migrationhub#UpdateDateTime``."""

import datetime
from typing import TypeAlias

UpdateDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDateTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> UpdateDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
