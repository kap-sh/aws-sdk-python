"""Generated from Smithy shape ``com.amazonaws.s3files#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3files.types.tag_list


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_s3files.types.tag_list.TagList"]
    """<p>An array of tags associated with the resource.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token to use in a subsequent request if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_s3files.types.tag_list

        out["tags"] = aws_sdk_s3files.types.tag_list.serialize_json(value["tags"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_s3files.types.tag_list

        out["tags"] = aws_sdk_s3files.types.tag_list.deserialize_json(data["tags"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
