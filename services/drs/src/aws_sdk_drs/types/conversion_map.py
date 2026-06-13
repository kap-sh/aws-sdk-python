"""Generated from Smithy shape ``com.amazonaws.drs#ConversionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.ebs_snapshot

ConversionMap: TypeAlias = dict[
    "aws_sdk_drs.types.ebs_snapshot.EbsSnapshot",
    "aws_sdk_drs.types.ebs_snapshot.EbsSnapshot",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConversionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ConversionMap:
    out: ConversionMap = {}
    for key, value in data.items():
        out[key] = value
    return out
