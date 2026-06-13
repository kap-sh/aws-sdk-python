"""Generated from Smithy shape ``com.amazonaws.odb#DataSafeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DataSafeStatus: TypeAlias = Literal[
    "REGISTERING",
    "REGISTERED",
    "DEREGISTERING",
    "NOT_REGISTERED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGISTERING",
        "REGISTERED",
        "DEREGISTERING",
        "NOT_REGISTERED",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: DataSafeStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DataSafeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSafeStatus value: {data!r}")
    return cast(DataSafeStatus, data)
