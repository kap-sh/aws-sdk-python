"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ResourceTagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.tag_key
    import capo_imagebuilder.types.tag_value

ResourceTagMap: TypeAlias = dict[
    "capo_imagebuilder.types.tag_key.TagKey",
    "capo_imagebuilder.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResourceTagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ResourceTagMap:
    out: ResourceTagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
