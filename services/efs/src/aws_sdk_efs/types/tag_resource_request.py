"""Generated from Smithy shape ``com.amazonaws.efs#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.resource_id
    import aws_sdk_efs.types.tags


class TagResourceRequest(TypedDict):
    resource_id: "aws_sdk_efs.types.resource_id.ResourceId"
    """<p>The ID specifying the EFS resource that you want to create a tag for.</p>"""
    tags: "aws_sdk_efs.types.tags.Tags"
    """<p>An array of <code>Tag</code> objects to add. Each <code>Tag</code> object is a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_efs.types.tags

    out["Tags"] = aws_sdk_efs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_efs.types.tags

        out["tags"] = aws_sdk_efs.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
