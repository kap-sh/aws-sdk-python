"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.next_token
    import aws_sdk_kinesis_video.types.resource_tags


class ListTagsForResourceOutput(TypedDict):
    next_token: NotRequired["aws_sdk_kinesis_video.types.next_token.NextToken"]
    """<p>If you specify this parameter and the result of a <code>ListTagsForResource</code> call is truncated, the response includes a token that you can use in the next request to fetch the next set of tags. </p>"""
    tags: NotRequired["aws_sdk_kinesis_video.types.resource_tags.ResourceTags"]
    """<p>A map of tag keys and values associated with the specified signaling channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "tags" in value:
        import aws_sdk_kinesis_video.types.resource_tags

        out["Tags"] = aws_sdk_kinesis_video.types.resource_tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Tags" in data:
        import aws_sdk_kinesis_video.types.resource_tags

        out["tags"] = aws_sdk_kinesis_video.types.resource_tags.deserialize_json(
            data["Tags"]
        )
    return out
