"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalDecoderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

SignalDecoderType: TypeAlias = Literal[
    "CAN_SIGNAL",
    "OBD_SIGNAL",
    "MESSAGE_SIGNAL",
    "CUSTOM_DECODING_SIGNAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CAN_SIGNAL",
        "OBD_SIGNAL",
        "MESSAGE_SIGNAL",
        "CUSTOM_DECODING_SIGNAL",
    )
)


def serialize_aws_json_1_0(value: SignalDecoderType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SignalDecoderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SignalDecoderType value: {data!r}")
    return cast(SignalDecoderType, data)
