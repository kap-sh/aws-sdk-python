"""Generated from Smithy shape ``com.amazonaws.ecs#LocalStorageType``."""

from typing import Literal, TypeAlias, cast

LocalStorageType: TypeAlias = Literal[
    "hdd",
    "ssd",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocalStorageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LocalStorageType:
    return cast(LocalStorageType, data)
