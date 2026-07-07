"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListSessionMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_session_results
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.next_token


class ListSessionMetricsResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier for the bot for which you retrieved session metrics.</p>"""
    results: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_session_results.AnalyticsSessionResults"
    ]
    """<p>The results for the session metrics.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListSessionMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListSessionMetrics request to return the next page of results. For a complete set of results, call the ListSessionMetrics operation until the nextToken returned in the response is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionMetricsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "results" in value:
        import aws_sdk_lex_models_v2.types.analytics_session_results

        out["results"] = (
            aws_sdk_lex_models_v2.types.analytics_session_results.serialize_json(
                value["results"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionMetricsResponse:
    out: ListSessionMetricsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "results" in data:
        import aws_sdk_lex_models_v2.types.analytics_session_results

        out["results"] = (
            aws_sdk_lex_models_v2.types.analytics_session_results.deserialize_json(
                data["results"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
