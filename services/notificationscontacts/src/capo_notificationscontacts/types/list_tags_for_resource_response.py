"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notificationscontacts.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_notificationscontacts.types.tag_map.TagMap"]
    """<p>Key-value pairs that are assigned to a resource, usually for the purpose of grouping and searching for items. Tags are metadata that you define.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_notificationscontacts.types.tag_map

        out["tags"] = capo_notificationscontacts.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_notificationscontacts.types.tag_map

        out["tags"] = capo_notificationscontacts.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
