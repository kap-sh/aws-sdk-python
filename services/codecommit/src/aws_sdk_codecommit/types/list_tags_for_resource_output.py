"""Generated from Smithy shape ``com.amazonaws.codecommit#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.next_token
    import aws_sdk_codecommit.types.tags_map


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_codecommit.types.tags_map.TagsMap"]
    """<p>A list of tag key and value pairs associated with the specified resource.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that allows the operation to batch the next results of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_codecommit.types.tags_map

        out["tags"] = aws_sdk_codecommit.types.tags_map.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_codecommit.types.tags_map

        out["tags"] = aws_sdk_codecommit.types.tags_map.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
