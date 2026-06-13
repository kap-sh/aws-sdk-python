"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.amazon_resource_name
    import aws_sdk_rolesanywhere.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_rolesanywhere.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource.</p>"""
    tags: "aws_sdk_rolesanywhere.types.tag_list.TagList"
    """<p>The tags to attach to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_rolesanywhere.types.tag_list

    out["tags"] = aws_sdk_rolesanywhere.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import aws_sdk_rolesanywhere.types.tag_list

        out["tags"] = aws_sdk_rolesanywhere.types.tag_list.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
