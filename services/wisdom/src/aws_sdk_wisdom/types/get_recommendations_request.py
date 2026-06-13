"""Generated from Smithy shape ``com.amazonaws.wisdom#GetRecommendationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.max_results
    import aws_sdk_wisdom.types.uuid_or_arn
    import aws_sdk_wisdom.types.wait_time_seconds


class GetRecommendationsRequest(TypedDict):
    assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    session_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    max_results: NotRequired["aws_sdk_wisdom.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    wait_time_seconds: "aws_sdk_wisdom.types.wait_time_seconds.WaitTimeSeconds"
    """<p>The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommendationsRequest:
    out: GetRecommendationsRequest = {}  # type: ignore[typeddict-item]
    return out
