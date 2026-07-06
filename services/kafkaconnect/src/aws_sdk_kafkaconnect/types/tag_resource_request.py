"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource to which you want to attach tags.</p>"""
    tags: "aws_sdk_kafkaconnect.types.tags.Tags"
    """<p>The tags that you want to attach to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_kafkaconnect.types.tags

    out["tags"] = aws_sdk_kafkaconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_kafkaconnect.types.tags

        out["tags"] = aws_sdk_kafkaconnect.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
