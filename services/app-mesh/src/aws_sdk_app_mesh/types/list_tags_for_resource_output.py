"""Generated from Smithy shape ``com.amazonaws.appmesh#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.tag_list


class ListTagsForResourceOutput(TypedDict):
    tags: "aws_sdk_app_mesh.types.tag_list.TagList"
    """<p>The tags for the resource.</p>"""
    next_token: NotRequired["str"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListTagsForResource</code> request. When the results of a <code>ListTagsForResource</code> request exceed <code>limit</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.tag_list

    out["tags"] = aws_sdk_app_mesh.types.tag_list.serialize_json(value["tags"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_app_mesh.types.tag_list

        out["tags"] = aws_sdk_app_mesh.types.tag_list.deserialize_json(data["tags"])
    else:
        raise DeserializationError("ListTagsForResourceOutput.tags required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
