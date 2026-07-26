"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#UserMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.string

UserMetadata: TypeAlias = dict[
    "capo_elastic_transcoder.types.string.String",
    "capo_elastic_transcoder.types.string.String",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UserMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> UserMetadata:
    out: UserMetadata = {}
    for key, value in data.items():
        out[key] = value
    return out
