"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchTopicsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.topic_summaries


class SearchTopicsResponse(TypedDict, closed=True):
    topic_summary_list: NotRequired[
        "aws_sdk_quicksight.types.topic_summaries.TopicSummaries"
    ]
    """<p>A list of topic summaries that is returned by the search topic request.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchTopicsResponse) -> dict:
    out: dict = {}
    if "topic_summary_list" in value:
        import aws_sdk_quicksight.types.topic_summaries

        out["TopicSummaryList"] = (
            aws_sdk_quicksight.types.topic_summaries.serialize_json(
                value["topic_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchTopicsResponse:
    out: SearchTopicsResponse = {}  # type: ignore[typeddict-item]
    if "TopicSummaryList" in data:
        import aws_sdk_quicksight.types.topic_summaries

        out["topic_summary_list"] = (
            aws_sdk_quicksight.types.topic_summaries.deserialize_json(
                data["TopicSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
