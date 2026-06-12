"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InvalidSignalDecoders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.invalid_signal_decoder

InvalidSignalDecoders: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.invalid_signal_decoder.InvalidSignalDecoder"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidSignalDecoders) -> list:
    import aws_sdk_iotfleetwise.types.invalid_signal_decoder

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.invalid_signal_decoder.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InvalidSignalDecoders:
    import aws_sdk_iotfleetwise.types.invalid_signal_decoder

    out: InvalidSignalDecoders = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.invalid_signal_decoder.deserialize_aws_json_1_0(
                item
            )
        )
    return out
