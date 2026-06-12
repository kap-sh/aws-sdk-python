"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StorageMaximumSizeUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

StorageMaximumSizeUnit: TypeAlias = Literal[
    "MB",
    "GB",
    "TB",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MB",
        "GB",
        "TB",
    )
)


def serialize_aws_json_1_0(value: StorageMaximumSizeUnit) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StorageMaximumSizeUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageMaximumSizeUnit value: {data!r}")
    return cast(StorageMaximumSizeUnit, data)
