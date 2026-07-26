"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_iot_wireless.types.tag_list.TagList"]
    """<p>The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_iot_wireless.types.tag_list

        out["Tags"] = capo_iot_wireless.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_iot_wireless.types.tag_list

        out["tags"] = capo_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    return out
