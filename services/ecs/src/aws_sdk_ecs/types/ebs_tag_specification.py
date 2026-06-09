"""Generated from Smithy shape ``com.amazonaws.ecs#EBSTagSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.ebs_resource_type
    import aws_sdk_ecs.types.propagate_tags
    import aws_sdk_ecs.types.tags


class EBSTagSpecification(TypedDict):
    resource_type: "aws_sdk_ecs.types.ebs_resource_type.EBSResourceType"
    """<p>The type of volume resource.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The tags applied to this Amazon EBS volume. <code>AmazonECSCreated</code> and <code>AmazonECSManaged</code> are reserved tags that can't be used.</p>"""
    propagate_tags: NotRequired["aws_sdk_ecs.types.propagate_tags.PropagateTags"]
    """<p>Determines whether to propagate the tags from the task definition to the Amazon EBS volume. Tags can only propagate to a <code>SERVICE</code> specified in <code>ServiceVolumeConfiguration</code>. If no value is specified, the tags aren't propagated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EBSTagSpecification) -> dict:
    out: dict = {}
    import aws_sdk_ecs.types.ebs_resource_type

    out["resourceType"] = aws_sdk_ecs.types.ebs_resource_type.serialize_aws_json_1_1(
        value["resource_type"]
    )
    if "tags" in value:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "propagate_tags" in value:
        import aws_sdk_ecs.types.propagate_tags

        out["propagateTags"] = aws_sdk_ecs.types.propagate_tags.serialize_aws_json_1_1(
            value["propagate_tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EBSTagSpecification:
    out: EBSTagSpecification = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import aws_sdk_ecs.types.ebs_resource_type

        out["resource_type"] = (
            aws_sdk_ecs.types.ebs_resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError("EBSTagSpecification.resource_type required")
    if "tags" in data:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if "propagateTags" in data:
        import aws_sdk_ecs.types.propagate_tags

        out["propagate_tags"] = (
            aws_sdk_ecs.types.propagate_tags.deserialize_aws_json_1_1(
                data["propagateTags"]
            )
        )
    return out
