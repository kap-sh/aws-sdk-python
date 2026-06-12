"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

SetupStatus: TypeAlias = Literal[
    "succeeded",
    "failed",
    "inProgress",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "succeeded",
        "failed",
        "inProgress",
    )
)


def serialize_aws_json_1_1(value: SetupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SetupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SetupStatus value: {data!r}")
    return cast(SetupStatus, data)
