"""Generated from Smithy shape ``com.amazonaws.appfabric#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_appfabric.types.tag_list.TagList"]
    """<p>A map of the key-value pairs for the tag or tags assigned to the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_appfabric.types.tag_list

        out["tags"] = aws_sdk_appfabric.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_appfabric.types.tag_list

        out["tags"] = aws_sdk_appfabric.types.tag_list.deserialize_json(data["tags"])
    return out
