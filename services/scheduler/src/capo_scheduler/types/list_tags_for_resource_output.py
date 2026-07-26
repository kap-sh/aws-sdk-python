"""Generated from Smithy shape ``com.amazonaws.scheduler#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_scheduler.types.tag_list.TagList"]
    """<p>The list of tags associated with the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_scheduler.types.tag_list

        out["Tags"] = capo_scheduler.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_scheduler.types.tag_list

        out["tags"] = capo_scheduler.types.tag_list.deserialize_json(data["Tags"])
    return out
