"""Generated from Smithy shape ``com.amazonaws.fsx#DriveCacheType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

DriveCacheType: TypeAlias = Literal[
    "NONE",
    "READ",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "READ",
    )
)


def serialize_aws_json_1_1(value: DriveCacheType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DriveCacheType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DriveCacheType value: {data!r}")
    return cast(DriveCacheType, data)
