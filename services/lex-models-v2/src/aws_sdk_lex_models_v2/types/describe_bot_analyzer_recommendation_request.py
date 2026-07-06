"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotAnalyzerRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.uuid


class DescribeBotAnalyzerRecommendationRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot.</p>"""
    bot_analyzer_request_id: "aws_sdk_lex_models_v2.types.uuid.UUID"
    """<p>The unique identifier of the analysis request.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from a previous request was truncated, the <code>nextToken</code> value is used to retrieve the next page of recommendations.</p>"""
    max_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of recommendations to return in the response. The default is 5.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotAnalyzerRecommendationRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> DescribeBotAnalyzerRecommendationRequest:
    out: DescribeBotAnalyzerRecommendationRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
