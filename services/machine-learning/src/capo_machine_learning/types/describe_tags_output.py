"""Generated from Smithy shape ``com.amazonaws.machinelearning#DescribeTagsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.tag_list
    import capo_machine_learning.types.taggable_resource_type


class DescribeTagsOutput(TypedDict, closed=True):
    resource_id: NotRequired["capo_machine_learning.types.entity_id.EntityId"]
    """<p>The ID of the tagged ML object.</p>"""
    resource_type: NotRequired[
        "capo_machine_learning.types.taggable_resource_type.TaggableResourceType"
    ]
    """<p>The type of the tagged ML object.</p>"""
    tags: NotRequired["capo_machine_learning.types.tag_list.TagList"]
    """<p>A list of tags associated with the ML object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsOutput) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        import capo_machine_learning.types.taggable_resource_type

        out["ResourceType"] = (
            capo_machine_learning.types.taggable_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "tags" in value:
        import capo_machine_learning.types.tag_list

        out["Tags"] = capo_machine_learning.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsOutput:
    out: DescribeTagsOutput = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        import capo_machine_learning.types.taggable_resource_type

        out["resource_type"] = (
            capo_machine_learning.types.taggable_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "Tags" in data:
        import capo_machine_learning.types.tag_list

        out["tags"] = capo_machine_learning.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
