"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalDecoderType``."""

from typing import Literal, TypeAlias, cast

SignalDecoderType: TypeAlias = Literal[
    "CAN_SIGNAL",
    "OBD_SIGNAL",
    "MESSAGE_SIGNAL",
    "CUSTOM_DECODING_SIGNAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalDecoderType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SignalDecoderType:
    return cast(SignalDecoderType, data)
