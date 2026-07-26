"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DeletedDateType``."""

import datetime
from typing import TypeAlias

DeletedDateType: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletedDateType) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> DeletedDateType:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
