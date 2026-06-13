"""Generated from Smithy shape ``com.amazonaws.backupsearch#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.tag_map


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_backupsearch.types.tag_map.TagMap"]
    """<p>List of tags returned by the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_backupsearch.types.tag_map

        out["Tags"] = aws_sdk_backupsearch.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_backupsearch.types.tag_map

        out["tags"] = aws_sdk_backupsearch.types.tag_map.deserialize_json(data["Tags"])
    return out
