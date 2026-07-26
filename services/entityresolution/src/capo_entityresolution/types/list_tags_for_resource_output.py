"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.tag_map


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: "capo_entityresolution.types.tag_map.TagMap"
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    import capo_entityresolution.types.tag_map

    out["tags"] = capo_entityresolution.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_entityresolution.types.tag_map

        out["tags"] = capo_entityresolution.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("ListTagsForResourceOutput.tags required")
    return out
