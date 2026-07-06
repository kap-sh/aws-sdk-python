"""Generated from Smithy shape ``com.amazonaws.qconnect#GetRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.max_results
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.recommendation_type
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.wait_time_seconds


class GetRecommendationsRequest(TypedDict, closed=True):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    session_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    max_results: NotRequired["aws_sdk_qconnect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    wait_time_seconds: "aws_sdk_qconnect.types.wait_time_seconds.WaitTimeSeconds"
    """<p>The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.</p>"""
    next_chunk_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of chunks. Use the value returned in the previous response in the next request to retrieve the next set of chunks.</p>"""
    recommendation_type: NotRequired[
        "aws_sdk_qconnect.types.recommendation_type.RecommendationType"
    ]
    """<p>The type of recommendation being requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommendationsRequest:
    out: GetRecommendationsRequest = {}  # type: ignore[typeddict-item]
    return out
