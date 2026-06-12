"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncLastModifiedTime``."""

import datetime
from typing import TypeAlias

ResourceDataSyncLastModifiedTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncLastModifiedTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ResourceDataSyncLastModifiedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
