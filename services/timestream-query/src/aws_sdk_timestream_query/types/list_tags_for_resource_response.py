"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.next_tags_for_resource_results_token
    import aws_sdk_timestream_query.types.tag_list


class ListTagsForResourceResponse(TypedDict):
    tags: "aws_sdk_timestream_query.types.tag_list.TagList"
    """<p>The tags currently associated with the Timestream resource. </p>"""
    next_token: NotRequired[
        "aws_sdk_timestream_query.types.next_tags_for_resource_results_token.NextTagsForResourceResultsToken"
    ]
    """<p>A pagination token to resume pagination with a subsequent call to <code>ListTagsForResourceResponse</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import aws_sdk_timestream_query.types.tag_list

    out["Tags"] = aws_sdk_timestream_query.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_timestream_query.types.tag_list

        out["tags"] = aws_sdk_timestream_query.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
