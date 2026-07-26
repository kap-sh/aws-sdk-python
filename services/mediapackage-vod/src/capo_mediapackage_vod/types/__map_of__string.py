"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#__mapOf__string``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__string

__mapOf__string: TypeAlias = dict[
    "capo_mediapackage_vod.types.__string.__string",
    "capo_mediapackage_vod.types.__string.__string",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: __mapOf__string) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> __mapOf__string:
    out: __mapOf__string = {}
    for key, value in data.items():
        out[key] = value
    return out
