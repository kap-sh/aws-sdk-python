"""Generated from Smithy shape ``com.amazonaws.inspector#ResourceGroupTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.resource_group_tag

ResourceGroupTags: TypeAlias = list[
    "capo_inspector.types.resource_group_tag.ResourceGroupTag"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceGroupTags) -> list:
    import capo_inspector.types.resource_group_tag

    out: list = []
    for item in value:
        out.append(capo_inspector.types.resource_group_tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceGroupTags:
    import capo_inspector.types.resource_group_tag

    out: ResourceGroupTags = []
    for item in data:
        out.append(
            capo_inspector.types.resource_group_tag.deserialize_aws_json_1_1(item)
        )
    return out
