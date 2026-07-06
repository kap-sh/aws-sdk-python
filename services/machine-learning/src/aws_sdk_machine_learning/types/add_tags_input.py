"""Generated from Smithy shape ``com.amazonaws.machinelearning#AddTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.tag_list
    import aws_sdk_machine_learning.types.taggable_resource_type


class AddTagsInput(TypedDict, closed=True):
    tags: "aws_sdk_machine_learning.types.tag_list.TagList"
    """<p>The key-value pairs to use to create tags. If you specify a key without specifying a value, Amazon ML creates a tag with the specified key and a value of null.</p>"""
    resource_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>The ID of the ML object to tag. For example, <code>exampleModelId</code>.</p>"""
    resource_type: (
        "aws_sdk_machine_learning.types.taggable_resource_type.TaggableResourceType"
    )
    """<p>The type of the ML object to tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsInput) -> dict:
    out: dict = {}
    import aws_sdk_machine_learning.types.tag_list

    out["Tags"] = aws_sdk_machine_learning.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_machine_learning.types.taggable_resource_type

    out["ResourceType"] = (
        aws_sdk_machine_learning.types.taggable_resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsInput:
    out: AddTagsInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_machine_learning.types.tag_list

        out["tags"] = aws_sdk_machine_learning.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("AddTagsInput.tags required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("AddTagsInput.resource_id required")
    if "ResourceType" in data:
        import aws_sdk_machine_learning.types.taggable_resource_type

        out["resource_type"] = (
            aws_sdk_machine_learning.types.taggable_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError("AddTagsInput.resource_type required")
    return out
