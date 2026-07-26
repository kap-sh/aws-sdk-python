"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.amazon_resource_name
    import capo_rolesanywhere.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_rolesanywhere.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource.</p>"""
    tags: "capo_rolesanywhere.types.tag_list.TagList"
    """<p>The tags to attach to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_rolesanywhere.types.tag_list

    out["tags"] = capo_rolesanywhere.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
