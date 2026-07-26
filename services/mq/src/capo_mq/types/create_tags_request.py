"""Generated from Smithy shape ``com.amazonaws.mq#CreateTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__map_of__string
    import capo_mq.types.__string


class CreateTagsRequest(TypedDict, closed=True):
    resource_arn: "capo_mq.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource tag.</p>"""
    tags: NotRequired["capo_mq.types.__map_of__string.__mapOf__string"]
    """<p>The key-value pair for the resource tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTagsRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_mq.types.__map_of__string

        out["tags"] = capo_mq.types.__map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTagsRequest:
    out: CreateTagsRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_mq.types.__map_of__string

        out["tags"] = capo_mq.types.__map_of__string.deserialize_json(data["tags"])
    return out
