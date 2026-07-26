"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.tag_map


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_internetmonitor.types.tag_map.TagMap"]
    """<p>Tags for a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_internetmonitor.types.tag_map

        out["Tags"] = capo_internetmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_internetmonitor.types.tag_map

        out["tags"] = capo_internetmonitor.types.tag_map.deserialize_json(data["Tags"])
    return out
