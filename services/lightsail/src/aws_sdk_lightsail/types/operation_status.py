"""Generated from Smithy shape ``com.amazonaws.lightsail#OperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

OperationStatus: TypeAlias = Literal[
    "NotStarted",
    "Started",
    "Failed",
    "Completed",
    "Succeeded",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotStarted",
        "Started",
        "Failed",
        "Completed",
        "Succeeded",
    )
)


def serialize_aws_json_1_1(value: OperationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationStatus value: {data!r}")
    return cast(OperationStatus, data)
