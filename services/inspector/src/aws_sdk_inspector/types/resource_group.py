"""Generated from Smithy shape ``com.amazonaws.inspector#ResourceGroup``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.resource_group_tags
    import aws_sdk_inspector.types.timestamp


class ResourceGroup(TypedDict):
    arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the resource group.</p>"""
    tags: "aws_sdk_inspector.types.resource_group_tags.ResourceGroupTags"
    """<p>The tags (key and value pairs) of the resource group. This data type property is used in the <a>CreateResourceGroup</a> action.</p>"""
    created_at: "aws_sdk_inspector.types.timestamp.Timestamp"
    """<p>The time at which resource group is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceGroup) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_inspector.types.resource_group_tags

    out["tags"] = aws_sdk_inspector.types.resource_group_tags.serialize_aws_json_1_1(
        value["tags"]
    )
    import aws_sdk_inspector.types.timestamp

    out["createdAt"] = aws_sdk_inspector.types.timestamp.serialize_aws_json_1_1(
        value["created_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceGroup:
    out: ResourceGroup = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ResourceGroup.arn required")
    if "tags" in data:
        import aws_sdk_inspector.types.resource_group_tags

        out["tags"] = (
            aws_sdk_inspector.types.resource_group_tags.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    else:
        raise DeserializationError("ResourceGroup.tags required")
    if "createdAt" in data:
        import aws_sdk_inspector.types.timestamp

        out["created_at"] = aws_sdk_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    else:
        raise DeserializationError("ResourceGroup.created_at required")
    return out
