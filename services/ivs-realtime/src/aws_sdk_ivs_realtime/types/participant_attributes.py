"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.string

ParticipantAttributes: TypeAlias = dict[
    "aws_sdk_ivs_realtime.types.string.String",
    "aws_sdk_ivs_realtime.types.string.String",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ParticipantAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ParticipantAttributes:
    out: ParticipantAttributes = {}
    for key, value in data.items():
        out[key] = value
    return out
