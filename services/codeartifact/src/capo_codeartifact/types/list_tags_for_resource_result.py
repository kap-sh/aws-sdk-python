"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.tag_list


class ListTagsForResourceResult(TypedDict, closed=True):
    tags: NotRequired["capo_codeartifact.types.tag_list.TagList"]
    """<p>A list of tag key and value pairs associated with the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codeartifact.types.tag_list

        out["tags"] = capo_codeartifact.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_codeartifact.types.tag_list

        out["tags"] = capo_codeartifact.types.tag_list.deserialize_json(data["tags"])
    return out
