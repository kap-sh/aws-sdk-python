"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListIntentMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_results
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.next_token


class ListIntentMetricsResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier for the bot for which you retrieved intent metrics.</p>"""
    results: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_intent_results.AnalyticsIntentResults"
    ]
    """<p>The results for the intent metrics.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListIntentMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListIntentMetrics request to return the next page of results. For a complete set of results, call the ListIntentMetrics operation until the nextToken returned in the response is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntentMetricsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "results" in value:
        import aws_sdk_lex_models_v2.types.analytics_intent_results

        out["results"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_results.serialize_json(
                value["results"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIntentMetricsResponse:
    out: ListIntentMetricsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "results" in data:
        import aws_sdk_lex_models_v2.types.analytics_intent_results

        out["results"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_results.deserialize_json(
                data["results"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
