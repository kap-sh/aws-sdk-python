"""Generated from Smithy shape ``com.amazonaws.batch#TagrisTagsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.tag_key
    import capo_batch.types.tag_value

TagrisTagsMap: TypeAlias = dict[
    "capo_batch.types.tag_key.TagKey", "capo_batch.types.tag_value.TagValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TagrisTagsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TagrisTagsMap:
    out: TagrisTagsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
