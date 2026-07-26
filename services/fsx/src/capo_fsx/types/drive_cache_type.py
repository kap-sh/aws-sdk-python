"""Generated from Smithy shape ``com.amazonaws.fsx#DriveCacheType``."""

from typing import Literal, TypeAlias, cast

DriveCacheType: TypeAlias = Literal[
    "NONE",
    "READ",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DriveCacheType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DriveCacheType:
    return cast(DriveCacheType, data)
