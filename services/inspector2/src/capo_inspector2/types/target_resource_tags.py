"""Generated from Smithy shape ``com.amazonaws.inspector2#TargetResourceTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.tag_value_list
    import capo_inspector2.types.target_resource_tags_key

TargetResourceTags: TypeAlias = dict[
    "capo_inspector2.types.target_resource_tags_key.TargetResourceTagsKey",
    "capo_inspector2.types.tag_value_list.TagValueList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TargetResourceTags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_inspector2.types.tag_value_list

        out[key] = capo_inspector2.types.tag_value_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TargetResourceTags:
    out: TargetResourceTags = {}
    for key, value in data.items():
        import capo_inspector2.types.tag_value_list

        out[key] = capo_inspector2.types.tag_value_list.deserialize_json(value)
    return out
