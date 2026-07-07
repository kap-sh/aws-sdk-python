"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteTagsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.taggable_resource_type


class DeleteTagsOutput(TypedDict, closed=True):
    resource_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>The ID of the ML object from which tags were deleted.</p>"""
    resource_type: NotRequired[
        "aws_sdk_machine_learning.types.taggable_resource_type.TaggableResourceType"
    ]
    """<p>The type of the ML object from which tags were deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagsOutput) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        import aws_sdk_machine_learning.types.taggable_resource_type

        out["ResourceType"] = (
            aws_sdk_machine_learning.types.taggable_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagsOutput:
    out: DeleteTagsOutput = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        import aws_sdk_machine_learning.types.taggable_resource_type

        out["resource_type"] = (
            aws_sdk_machine_learning.types.taggable_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    return out
