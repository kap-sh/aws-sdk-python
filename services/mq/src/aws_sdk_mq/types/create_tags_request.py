"""Generated from Smithy shape ``com.amazonaws.mq#CreateTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__map_of__string
    import aws_sdk_mq.types.__string


class CreateTagsRequest(TypedDict):
    resource_arn: "aws_sdk_mq.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource tag.</p>"""
    tags: NotRequired["aws_sdk_mq.types.__map_of__string.__mapOf__string"]
    """<p>The key-value pair for the resource tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTagsRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_mq.types.__map_of__string

        out["tags"] = aws_sdk_mq.types.__map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTagsRequest:
    out: CreateTagsRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_mq.types.__map_of__string

        out["tags"] = aws_sdk_mq.types.__map_of__string.deserialize_json(data["tags"])
    return out
