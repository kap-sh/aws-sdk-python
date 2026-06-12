"""Generated from Smithy shape ``com.amazonaws.lightsail#AlarmState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

AlarmState: TypeAlias = Literal[
    "OK",
    "ALARM",
    "INSUFFICIENT_DATA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OK",
        "ALARM",
        "INSUFFICIENT_DATA",
    )
)


def serialize_aws_json_1_1(value: AlarmState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AlarmState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlarmState value: {data!r}")
    return cast(AlarmState, data)
