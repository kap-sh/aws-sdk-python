"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StorageMinimumTimeToLiveUnit``."""

from typing import Literal, TypeAlias, cast

StorageMinimumTimeToLiveUnit: TypeAlias = Literal[
    "HOURS",
    "DAYS",
    "WEEKS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StorageMinimumTimeToLiveUnit) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StorageMinimumTimeToLiveUnit:
    return cast(StorageMinimumTimeToLiveUnit, data)
