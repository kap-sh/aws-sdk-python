"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TriggerMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

TriggerMode: TypeAlias = Literal[
    "ALWAYS",
    "RISING_EDGE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALWAYS",
        "RISING_EDGE",
    )
)


def serialize_aws_json_1_0(value: TriggerMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TriggerMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggerMode value: {data!r}")
    return cast(TriggerMode, data)
