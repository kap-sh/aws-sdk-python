"""Generated from Smithy shape ``com.amazonaws.quicksight#ListTopicsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.topic_summaries


class ListTopicsResponse(TypedDict):
    topics_summaries: NotRequired[
        "aws_sdk_quicksight.types.topic_summaries.TopicSummaries"
    ]
    """<p>A list of topic summaries.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicsResponse) -> dict:
    out: dict = {}
    if "topics_summaries" in value:
        import aws_sdk_quicksight.types.topic_summaries

        out["TopicsSummaries"] = (
            aws_sdk_quicksight.types.topic_summaries.serialize_json(
                value["topics_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListTopicsResponse:
    out: ListTopicsResponse = {}  # type: ignore[typeddict-item]
    if "TopicsSummaries" in data:
        import aws_sdk_quicksight.types.topic_summaries

        out["topics_summaries"] = (
            aws_sdk_quicksight.types.topic_summaries.deserialize_json(
                data["TopicsSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
