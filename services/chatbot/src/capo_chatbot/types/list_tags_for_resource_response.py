"""Generated from Smithy shape ``com.amazonaws.chatbot#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_chatbot.types.tag_list.TagList"]
    """<p>Key-value pairs that are assigned to a resource, usually for the purpose of grouping and searching for items. Tags are metadata that you define.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_chatbot.types.tag_list

        out["Tags"] = capo_chatbot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_chatbot.types.tag_list

        out["tags"] = capo_chatbot.types.tag_list.deserialize_json(data["Tags"])
    return out
