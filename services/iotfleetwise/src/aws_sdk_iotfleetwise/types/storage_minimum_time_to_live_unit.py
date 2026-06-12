"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StorageMinimumTimeToLiveUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

StorageMinimumTimeToLiveUnit: TypeAlias = Literal[
    "HOURS",
    "DAYS",
    "WEEKS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOURS",
        "DAYS",
        "WEEKS",
    )
)


def serialize_aws_json_1_0(value: StorageMinimumTimeToLiveUnit) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StorageMinimumTimeToLiveUnit:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StorageMinimumTimeToLiveUnit value: {data!r}"
        )
    return cast(StorageMinimumTimeToLiveUnit, data)
