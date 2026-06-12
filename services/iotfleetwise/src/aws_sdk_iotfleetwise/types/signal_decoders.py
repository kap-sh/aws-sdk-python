"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalDecoders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.signal_decoder

SignalDecoders: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.signal_decoder.SignalDecoder"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalDecoders) -> list:
    import aws_sdk_iotfleetwise.types.signal_decoder

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.signal_decoder.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SignalDecoders:
    import aws_sdk_iotfleetwise.types.signal_decoder

    out: SignalDecoders = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.signal_decoder.deserialize_aws_json_1_0(item)
        )
    return out
