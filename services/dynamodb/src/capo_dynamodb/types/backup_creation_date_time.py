"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupCreationDateTime``."""

import datetime
from typing import TypeAlias

BackupCreationDateTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BackupCreationDateTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> BackupCreationDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
