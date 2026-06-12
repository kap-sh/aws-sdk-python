"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

SignalValueType: TypeAlias = Literal[
    "INTEGER",
    "FLOATING_POINT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTEGER",
        "FLOATING_POINT",
    )
)


def serialize_aws_json_1_0(value: SignalValueType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SignalValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SignalValueType value: {data!r}")
    return cast(SignalValueType, data)
