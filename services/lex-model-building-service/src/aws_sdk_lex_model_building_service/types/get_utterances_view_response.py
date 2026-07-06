"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetUtterancesViewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_name
    import aws_sdk_lex_model_building_service.types.lists_of_utterances


class GetUtterancesViewResponse(TypedDict, closed=True):
    bot_name: NotRequired["aws_sdk_lex_model_building_service.types.bot_name.BotName"]
    """<p>The name of the bot for which utterance information was returned.</p>"""
    utterances: NotRequired[
        "aws_sdk_lex_model_building_service.types.lists_of_utterances.ListsOfUtterances"
    ]
    """<p>An array of <a>UtteranceList</a> objects, each containing a list of <a>UtteranceData</a> objects describing the utterances that were processed by your bot. The response contains a maximum of 100 <code>UtteranceData</code> objects for each version. Amazon Lex returns the most frequent utterances received by the bot in the last 15 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUtterancesViewResponse) -> dict:
    out: dict = {}
    if "bot_name" in value:
        out["botName"] = value["bot_name"]
    if "utterances" in value:
        import aws_sdk_lex_model_building_service.types.lists_of_utterances

        out["utterances"] = (
            aws_sdk_lex_model_building_service.types.lists_of_utterances.serialize_json(
                value["utterances"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetUtterancesViewResponse:
    out: GetUtterancesViewResponse = {}  # type: ignore[typeddict-item]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    if "utterances" in data:
        import aws_sdk_lex_model_building_service.types.lists_of_utterances

        out["utterances"] = (
            aws_sdk_lex_model_building_service.types.lists_of_utterances.deserialize_json(
                data["utterances"]
            )
        )
    return out
