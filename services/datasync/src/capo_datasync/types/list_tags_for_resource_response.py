"""Generated from Smithy shape ``com.amazonaws.datasync#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.next_token
    import capo_datasync.types.output_tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_datasync.types.output_tag_list.OutputTagList"]
    """<p>An array of tags applied to the specified resource.</p>"""
    next_token: NotRequired["capo_datasync.types.next_token.NextToken"]
    """<p>The opaque string that indicates the position to begin the next list of results in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_datasync.types.output_tag_list

        out["Tags"] = capo_datasync.types.output_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_datasync.types.output_tag_list

        out["tags"] = capo_datasync.types.output_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
