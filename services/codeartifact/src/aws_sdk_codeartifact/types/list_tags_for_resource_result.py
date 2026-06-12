"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.tag_list


class ListTagsForResourceResult(TypedDict):
    tags: NotRequired["aws_sdk_codeartifact.types.tag_list.TagList"]
    """<p>A list of tag key and value pairs associated with the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_codeartifact.types.tag_list

        out["tags"] = aws_sdk_codeartifact.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_codeartifact.types.tag_list

        out["tags"] = aws_sdk_codeartifact.types.tag_list.deserialize_json(data["tags"])
    return out
