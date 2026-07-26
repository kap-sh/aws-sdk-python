"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.next_token
    import capo_kinesis_video.types.resource_tags


class ListTagsForResourceOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_kinesis_video.types.next_token.NextToken"]
    """<p>If you specify this parameter and the result of a <code>ListTagsForResource</code> call is truncated, the response includes a token that you can use in the next request to fetch the next set of tags. </p>"""
    tags: NotRequired["capo_kinesis_video.types.resource_tags.ResourceTags"]
    """<p>A map of tag keys and values associated with the specified signaling channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "tags" in value:
        import capo_kinesis_video.types.resource_tags

        out["Tags"] = capo_kinesis_video.types.resource_tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Tags" in data:
        import capo_kinesis_video.types.resource_tags

        out["tags"] = capo_kinesis_video.types.resource_tags.deserialize_json(
            data["Tags"]
        )
    return out
