"""Generated from Smithy shape ``com.amazonaws.oam#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_oam.types.tag_map_output


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_oam.types.tag_map_output.TagMapOutput"]
    """<p>The list of tags associated with the requested resource.&gt;</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_oam.types.tag_map_output

        out["Tags"] = capo_oam.types.tag_map_output.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_oam.types.tag_map_output

        out["tags"] = capo_oam.types.tag_map_output.deserialize_json(data["Tags"])
    return out
