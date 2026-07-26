"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.tags


class ListTagsForResourceResult(TypedDict, closed=True):
    tags: NotRequired["capo_codestar_notifications.types.tags.Tags"]
    """<p>The tags associated with the notification rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codestar_notifications.types.tags

        out["Tags"] = capo_codestar_notifications.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_codestar_notifications.types.tags

        out["tags"] = capo_codestar_notifications.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
