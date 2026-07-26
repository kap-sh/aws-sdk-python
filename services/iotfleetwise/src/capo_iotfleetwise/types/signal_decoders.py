"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalDecoders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.signal_decoder

SignalDecoders: TypeAlias = list["capo_iotfleetwise.types.signal_decoder.SignalDecoder"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalDecoders) -> list:
    import capo_iotfleetwise.types.signal_decoder

    out: list = []
    for item in value:
        out.append(capo_iotfleetwise.types.signal_decoder.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SignalDecoders:
    import capo_iotfleetwise.types.signal_decoder

    out: SignalDecoders = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.signal_decoder.deserialize_aws_json_1_0(item)
        )
    return out
