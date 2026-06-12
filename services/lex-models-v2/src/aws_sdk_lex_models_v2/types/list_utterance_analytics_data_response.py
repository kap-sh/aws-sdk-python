"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListUtteranceAnalyticsDataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.utterance_specifications


class ListUtteranceAnalyticsDataResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot that the utterances belong to.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListUtteranceAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListUtteranceAnalyticsData request to return the next page of results. For a complete set of results, call the ListUtteranceAnalyticsData operation until the nextToken returned in the response is null.</p>"""
    utterances: NotRequired[
        "aws_sdk_lex_models_v2.types.utterance_specifications.UtteranceSpecifications"
    ]
    """<p>A list of objects, each of which contains information about an utterance in a user session with your bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUtteranceAnalyticsDataResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "utterances" in value:
        import aws_sdk_lex_models_v2.types.utterance_specifications

        out["utterances"] = (
            aws_sdk_lex_models_v2.types.utterance_specifications.serialize_json(
                value["utterances"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListUtteranceAnalyticsDataResponse:
    out: ListUtteranceAnalyticsDataResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "utterances" in data:
        import aws_sdk_lex_models_v2.types.utterance_specifications

        out["utterances"] = (
            aws_sdk_lex_models_v2.types.utterance_specifications.deserialize_json(
                data["utterances"]
            )
        )
    return out
