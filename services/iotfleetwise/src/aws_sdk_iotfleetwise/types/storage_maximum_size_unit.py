"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StorageMaximumSizeUnit``."""

from typing import Literal, TypeAlias, cast

StorageMaximumSizeUnit: TypeAlias = Literal[
    "MB",
    "GB",
    "TB",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StorageMaximumSizeUnit) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StorageMaximumSizeUnit:
    return cast(StorageMaximumSizeUnit, data)
