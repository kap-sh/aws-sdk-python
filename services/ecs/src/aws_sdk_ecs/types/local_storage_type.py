"""Generated from Smithy shape ``com.amazonaws.ecs#LocalStorageType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

LocalStorageType: TypeAlias = Literal[
    "hdd",
    "ssd",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "hdd",
        "ssd",
    )
)


def serialize_aws_json_1_1(value: LocalStorageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LocalStorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LocalStorageType value: {data!r}")
    return cast(LocalStorageType, data)
