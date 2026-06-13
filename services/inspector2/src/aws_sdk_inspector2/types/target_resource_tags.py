"""Generated from Smithy shape ``com.amazonaws.inspector2#TargetResourceTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.tag_value_list
    import aws_sdk_inspector2.types.target_resource_tags_key

TargetResourceTags: TypeAlias = dict[
    "aws_sdk_inspector2.types.target_resource_tags_key.TargetResourceTagsKey",
    "aws_sdk_inspector2.types.tag_value_list.TagValueList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TargetResourceTags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_inspector2.types.tag_value_list

        out[key] = aws_sdk_inspector2.types.tag_value_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TargetResourceTags:
    out: TargetResourceTags = {}
    for key, value in data.items():
        import aws_sdk_inspector2.types.tag_value_list

        out[key] = aws_sdk_inspector2.types.tag_value_list.deserialize_json(value)
    return out
