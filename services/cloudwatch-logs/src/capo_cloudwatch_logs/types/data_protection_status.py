"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DataProtectionStatus``."""

from typing import Literal, TypeAlias, cast

DataProtectionStatus: TypeAlias = Literal[
    "ACTIVATED",
    "DELETED",
    "ARCHIVED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProtectionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataProtectionStatus:
    return cast(DataProtectionStatus, data)
