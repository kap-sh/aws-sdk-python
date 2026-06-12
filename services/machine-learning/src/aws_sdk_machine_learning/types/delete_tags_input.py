"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteTagsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.tag_key_list
    import aws_sdk_machine_learning.types.taggable_resource_type


class DeleteTagsInput(TypedDict):
    tag_keys: "aws_sdk_machine_learning.types.tag_key_list.TagKeyList"
    """<p>One or more tags to delete.</p>"""
    resource_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>The ID of the tagged ML object. For example, <code>exampleModelId</code>.</p>"""
    resource_type: (
        "aws_sdk_machine_learning.types.taggable_resource_type.TaggableResourceType"
    )
    """<p>The type of the tagged ML object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagsInput) -> dict:
    out: dict = {}
    import aws_sdk_machine_learning.types.tag_key_list

    out["TagKeys"] = aws_sdk_machine_learning.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_machine_learning.types.taggable_resource_type

    out["ResourceType"] = (
        aws_sdk_machine_learning.types.taggable_resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagsInput:
    out: DeleteTagsInput = {}  # type: ignore[typeddict-item]
    if "TagKeys" in data:
        import aws_sdk_machine_learning.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_machine_learning.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("DeleteTagsInput.tag_keys required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("DeleteTagsInput.resource_id required")
    if "ResourceType" in data:
        import aws_sdk_machine_learning.types.taggable_resource_type

        out["resource_type"] = (
            aws_sdk_machine_learning.types.taggable_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError("DeleteTagsInput.resource_type required")
    return out
