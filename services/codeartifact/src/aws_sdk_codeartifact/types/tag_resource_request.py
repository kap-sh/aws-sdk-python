"""Generated from Smithy shape ``com.amazonaws.codeartifact#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.arn
    import aws_sdk_codeartifact.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_codeartifact.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to add or update tags for.</p>"""
    tags: "aws_sdk_codeartifact.types.tag_list.TagList"
    """<p>The tags you want to modify or add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_codeartifact.types.tag_list

    out["tags"] = aws_sdk_codeartifact.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_codeartifact.types.tag_list

        out["tags"] = aws_sdk_codeartifact.types.tag_list.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
