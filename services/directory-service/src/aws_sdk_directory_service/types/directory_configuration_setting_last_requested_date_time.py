"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryConfigurationSettingLastRequestedDateTime``."""

import datetime
from typing import TypeAlias

DirectoryConfigurationSettingLastRequestedDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DirectoryConfigurationSettingLastRequestedDateTime,
) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(
    data: float,
) -> DirectoryConfigurationSettingLastRequestedDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
