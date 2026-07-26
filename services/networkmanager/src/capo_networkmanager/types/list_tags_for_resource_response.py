"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tag_list: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The list of tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import capo_networkmanager.types.tag_list

        out["TagList"] = capo_networkmanager.types.tag_list.serialize_json(
            value["tag_list"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import capo_networkmanager.types.tag_list

        out["tag_list"] = capo_networkmanager.types.tag_list.deserialize_json(
            data["TagList"]
        )
    return out
