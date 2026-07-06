"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.next_token
    import aws_sdk_bedrock_agentcore.types.recommendation_status


class ListRecommendationsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agentcore.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    status_filter: NotRequired[
        "aws_sdk_bedrock_agentcore.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Optional filter to return only recommendations with the specified status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecommendationsRequest:
    out: ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
    return out
