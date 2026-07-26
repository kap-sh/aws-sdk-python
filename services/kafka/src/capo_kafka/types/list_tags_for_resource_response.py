"""Generated from Smithy shape ``com.amazonaws.kafka#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__map_of__string


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_kafka.types.__map_of__string.__mapOf__string"]
    """<p>The key-value pair for the resource tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.deserialize_json(data["tags"])
    return out
