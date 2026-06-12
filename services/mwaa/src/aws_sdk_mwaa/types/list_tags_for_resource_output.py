"""Generated from Smithy shape ``com.amazonaws.mwaa#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mwaa.types.tag_map

class ListTagsForResourceOutput(TypedDict):
    tags: NotRequired["aws_sdk_mwaa.types.tag_map.TagMap"]
    """<p>The key-value tag pairs associated to your environment. For more information, refer to <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_mwaa.types.tag_map
        out["Tags"] = aws_sdk_mwaa.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_mwaa.types.tag_map
        out["tags"] = aws_sdk_mwaa.types.tag_map.deserialize_json(data["Tags"])
    return out