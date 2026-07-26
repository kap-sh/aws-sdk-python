"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListTagsForGlobalResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__map_of_string


class ListTagsForGlobalResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_mediaconnect.types.__map_of_string.__mapOfString"]
    """<p>A map of tag keys and values associated with the global resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForGlobalResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForGlobalResourceResponse:
    out: ListTagsForGlobalResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    return out
