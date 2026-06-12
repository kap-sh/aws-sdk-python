"""Generated from Smithy shape ``com.amazonaws.dsql#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_dsql.types.tag_map

class ListTagsForResourceOutput(TypedDict):
    tags: NotRequired["aws_sdk_dsql.types.tag_map.TagMap"]
    """<p>A map of key and value pairs that you used to tag your resource.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_dsql.types.tag_map
        out["tags"] = aws_sdk_dsql.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_dsql.types.tag_map
        out["tags"] = aws_sdk_dsql.types.tag_map.deserialize_json(data["tags"])
    return out