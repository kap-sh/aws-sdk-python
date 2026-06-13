"""Generated from Smithy shape ``com.amazonaws.inspector2#Resource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.non_empty_string
    import aws_sdk_inspector2.types.resource_details
    import aws_sdk_inspector2.types.resource_type
    import aws_sdk_inspector2.types.tag_map


class Resource(TypedDict):
    type: "aws_sdk_inspector2.types.resource_type.ResourceType"
    """<p>The type of resource.</p>"""
    id: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The ID of the resource.</p>"""
    partition: NotRequired["aws_sdk_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The partition of the resource.</p>"""
    region: NotRequired["aws_sdk_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services Region the impacted resource is located in.</p>"""
    tags: NotRequired["aws_sdk_inspector2.types.tag_map.TagMap"]
    """<p>The tags attached to the resource.</p>"""
    details: NotRequired["aws_sdk_inspector2.types.resource_details.ResourceDetails"]
    """<p>An object that contains details about the resource involved in a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["id"] = value["id"]
    if "partition" in value:
        out["partition"] = value["partition"]
    if "region" in value:
        out["region"] = value["region"]
    if "tags" in value:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.serialize_json(value["tags"])
    if "details" in value:
        import aws_sdk_inspector2.types.resource_details

        out["details"] = aws_sdk_inspector2.types.resource_details.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("Resource.type required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Resource.id required")
    if "partition" in data:
        out["partition"] = data["partition"]
    if "region" in data:
        out["region"] = data["region"]
    if "tags" in data:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.deserialize_json(data["tags"])
    if "details" in data:
        import aws_sdk_inspector2.types.resource_details

        out["details"] = aws_sdk_inspector2.types.resource_details.deserialize_json(
            data["details"]
        )
    return out
