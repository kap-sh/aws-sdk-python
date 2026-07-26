"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_chime_sdk_meetings.types.tag_list.TagList"]
    """<p>The tags requested for the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_chime_sdk_meetings.types.tag_list

        out["Tags"] = capo_chime_sdk_meetings.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_chime_sdk_meetings.types.tag_list

        out["tags"] = capo_chime_sdk_meetings.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out
