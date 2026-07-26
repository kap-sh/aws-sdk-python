"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryConfigurationSettingLastUpdatedDateTime``."""

import datetime
from typing import TypeAlias

DirectoryConfigurationSettingLastUpdatedDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DirectoryConfigurationSettingLastUpdatedDateTime,
) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(
    data: float,
) -> DirectoryConfigurationSettingLastUpdatedDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
