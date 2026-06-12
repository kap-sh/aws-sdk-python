"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

FlywheelStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: FlywheelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlywheelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlywheelStatus value: {data!r}")
    return cast(FlywheelStatus, data)
