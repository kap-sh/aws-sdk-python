"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalNodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

SignalNodeType: TypeAlias = Literal[
    "SENSOR",
    "ACTUATOR",
    "ATTRIBUTE",
    "BRANCH",
    "CUSTOM_STRUCT",
    "CUSTOM_PROPERTY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SENSOR",
        "ACTUATOR",
        "ATTRIBUTE",
        "BRANCH",
        "CUSTOM_STRUCT",
        "CUSTOM_PROPERTY",
    )
)


def serialize_aws_json_1_0(value: SignalNodeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SignalNodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SignalNodeType value: {data!r}")
    return cast(SignalNodeType, data)
