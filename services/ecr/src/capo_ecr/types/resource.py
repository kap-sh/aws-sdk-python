"""Generated from Smithy shape ``com.amazonaws.ecr#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.resource_details
    import capo_ecr.types.resource_id
    import capo_ecr.types.tags
    import capo_ecr.types.type


class Resource(TypedDict, closed=True):
    details: NotRequired["capo_ecr.types.resource_details.ResourceDetails"]
    """<p>An object that contains details about the resource involved in a finding.</p>"""
    id: NotRequired["capo_ecr.types.resource_id.ResourceId"]
    """<p>The ID of the resource.</p>"""
    tags: NotRequired["capo_ecr.types.tags.Tags"]
    """<p>The tags attached to the resource.</p>"""
    type: NotRequired["capo_ecr.types.type.Type"]
    """<p>The type of resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resource) -> dict:
    out: dict = {}
    if "details" in value:
        import capo_ecr.types.resource_details

        out["details"] = capo_ecr.types.resource_details.serialize_aws_json_1_1(
            value["details"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "tags" in value:
        import capo_ecr.types.tags

        out["tags"] = capo_ecr.types.tags.serialize_aws_json_1_1(value["tags"])
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("details") is not None:
        import capo_ecr.types.resource_details

        out["details"] = capo_ecr.types.resource_details.deserialize_aws_json_1_1(
            data["details"]
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("tags") is not None:
        import capo_ecr.types.tags

        out["tags"] = capo_ecr.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out
