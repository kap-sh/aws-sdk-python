"""Generated from Smithy shape ``com.amazonaws.lightsail#RecordState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

RecordState: TypeAlias = Literal[
    "Started",
    "Succeeded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Started",
        "Succeeded",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: RecordState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordState value: {data!r}")
    return cast(RecordState, data)
