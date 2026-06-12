"""Generated from Smithy shape ``com.amazonaws.mq#ListTagsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__map_of__string


class ListTagsResponse(TypedDict):
    tags: NotRequired["aws_sdk_mq.types.__map_of__string.__mapOf__string"]
    """<p>The key-value pair for the resource tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_mq.types.__map_of__string

        out["tags"] = aws_sdk_mq.types.__map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_mq.types.__map_of__string

        out["tags"] = aws_sdk_mq.types.__map_of__string.deserialize_json(data["tags"])
    return out
