"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListSessionAnalyticsDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.session_specifications


class ListSessionAnalyticsDataResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot that the sessions belong to.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListSessionAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListSessionAnalyticsData request to return the next page of results. For a complete set of results, call the ListSessionAnalyticsData operation until the nextToken returned in the response is null.</p>"""
    sessions: NotRequired[
        "aws_sdk_lex_models_v2.types.session_specifications.SessionSpecifications"
    ]
    """<p>A list of objects, each of which contains information about a session with the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionAnalyticsDataResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sessions" in value:
        import aws_sdk_lex_models_v2.types.session_specifications

        out["sessions"] = (
            aws_sdk_lex_models_v2.types.session_specifications.serialize_json(
                value["sessions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSessionAnalyticsDataResponse:
    out: ListSessionAnalyticsDataResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sessions" in data:
        import aws_sdk_lex_models_v2.types.session_specifications

        out["sessions"] = (
            aws_sdk_lex_models_v2.types.session_specifications.deserialize_json(
                data["sessions"]
            )
        )
    return out
