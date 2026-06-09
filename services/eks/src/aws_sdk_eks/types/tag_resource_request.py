"""Generated from Smithy shape ``com.amazonaws.eks#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>"""
    tags: "aws_sdk_eks.types.tag_map.TagMap"
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_eks.types.tag_map

    out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
