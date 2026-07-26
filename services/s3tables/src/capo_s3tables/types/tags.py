"""Generated from Smithy shape ``com.amazonaws.s3tables#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.tag_key
    import capo_s3tables.types.tag_value

Tags: TypeAlias = dict[
    "capo_s3tables.types.tag_key.TagKey", "capo_s3tables.types.tag_value.TagValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        out[key] = value
    return out
