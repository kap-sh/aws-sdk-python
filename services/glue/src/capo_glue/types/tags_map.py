"""Generated from Smithy shape ``com.amazonaws.glue#TagsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.tag_key
    import capo_glue.types.tag_value

TagsMap: TypeAlias = dict[
    "capo_glue.types.tag_key.TagKey", "capo_glue.types.tag_value.TagValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TagsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> TagsMap:
    out: TagsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
