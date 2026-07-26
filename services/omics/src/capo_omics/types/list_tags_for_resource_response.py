"""Generated from Smithy shape ``com.amazonaws.omics#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "capo_omics.types.tag_map.TagMap"
    """<p>A list of tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import capo_omics.types.tag_map

    out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    return out
