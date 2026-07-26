"""Generated from Smithy shape ``com.amazonaws.mpa#SessionMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.session_key
    import capo_mpa.types.session_value

SessionMetadata: TypeAlias = dict[
    "capo_mpa.types.session_key.SessionKey", "capo_mpa.types.session_value.SessionValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SessionMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SessionMetadata:
    out: SessionMetadata = {}
    for key, value in data.items():
        out[key] = value
    return out
