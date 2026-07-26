"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantTokenAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.string

ParticipantTokenAttributes: TypeAlias = dict[
    "capo_ivs_realtime.types.string.String", "capo_ivs_realtime.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ParticipantTokenAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ParticipantTokenAttributes:
    out: ParticipantTokenAttributes = {}
    for key, value in data.items():
        out[key] = value
    return out
