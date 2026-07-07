"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListUtteranceMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_utterance_results
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.next_token


class ListUtteranceMetricsResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier for the bot for which you retrieved utterance metrics.</p>"""
    results: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_utterance_results.AnalyticsUtteranceResults"
    ]
    """<p>The results for the utterance metrics.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListUtteranceMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListUtteranceMetrics request to return the next page of results. For a complete set of results, call the ListUtteranceMetrics operation until the nextToken returned in the response is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUtteranceMetricsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "results" in value:
        import aws_sdk_lex_models_v2.types.analytics_utterance_results

        out["results"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_results.serialize_json(
                value["results"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUtteranceMetricsResponse:
    out: ListUtteranceMetricsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "results" in data:
        import aws_sdk_lex_models_v2.types.analytics_utterance_results

        out["results"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_results.deserialize_json(
                data["results"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
