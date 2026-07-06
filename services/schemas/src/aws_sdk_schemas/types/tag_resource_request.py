"""Generated from Smithy shape ``com.amazonaws.schemas#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_schemas.types.__string.__string"
    """<p>The ARN of the resource.</p>"""
    tags: NotRequired["aws_sdk_schemas.types.tags.Tags"]
    """<p>Tags associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.deserialize_json(data["tags"])
    return out
