"""Generated from Smithy shape ``com.amazonaws.ecr#Resource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.resource_details
    import aws_sdk_ecr.types.resource_id
    import aws_sdk_ecr.types.tags
    import aws_sdk_ecr.types.type


class Resource(TypedDict):
    details: NotRequired["aws_sdk_ecr.types.resource_details.ResourceDetails"]
    """<p>An object that contains details about the resource involved in a finding.</p>"""
    id: NotRequired["aws_sdk_ecr.types.resource_id.ResourceId"]
    """<p>The ID of the resource.</p>"""
    tags: NotRequired["aws_sdk_ecr.types.tags.Tags"]
    """<p>The tags attached to the resource.</p>"""
    type: NotRequired["aws_sdk_ecr.types.type.Type"]
    """<p>The type of resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resource) -> dict:
    out: dict = {}
    if "details" in value:
        import aws_sdk_ecr.types.resource_details

        out["details"] = aws_sdk_ecr.types.resource_details.serialize_aws_json_1_1(
            value["details"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "tags" in value:
        import aws_sdk_ecr.types.tags

        out["tags"] = aws_sdk_ecr.types.tags.serialize_aws_json_1_1(value["tags"])
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "details" in data:
        import aws_sdk_ecr.types.resource_details

        out["details"] = aws_sdk_ecr.types.resource_details.deserialize_aws_json_1_1(
            data["details"]
        )
    if "id" in data:
        out["id"] = data["id"]
    if "tags" in data:
        import aws_sdk_ecr.types.tags

        out["tags"] = aws_sdk_ecr.types.tags.deserialize_aws_json_1_1(data["tags"])
    if "type" in data:
        out["type"] = data["type"]
    return out
