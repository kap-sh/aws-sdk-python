"""Generated from Smithy shape ``com.amazonaws.lambda#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.taggable_resource
    import aws_sdk_lambda.types.tags


class TagResourceRequest(TypedDict):
    resource: "aws_sdk_lambda.types.taggable_resource.TaggableResource"
    """<p>The resource's Amazon Resource Name (ARN).</p>"""
    tags: "aws_sdk_lambda.types.tags.Tags"
    """<p>A list of tags to apply to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.tags

    out["Tags"] = aws_sdk_lambda.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_lambda.types.tags

        out["tags"] = aws_sdk_lambda.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
