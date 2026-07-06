"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetUtterancesViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_name
    import aws_sdk_lex_model_building_service.types.bot_versions
    import aws_sdk_lex_model_building_service.types.status_type


class GetUtterancesViewRequest(TypedDict, closed=True):
    bot_name: "aws_sdk_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot for which utterance information should be returned.</p>"""
    bot_versions: "aws_sdk_lex_model_building_service.types.bot_versions.BotVersions"
    """<p>An array of bot versions for which utterance information should be returned. The limit is 5 versions per request.</p>"""
    status_type: "aws_sdk_lex_model_building_service.types.status_type.StatusType"
    """<p>To return utterances that were recognized and handled, use <code>Detected</code>. To return utterances that were not recognized, use <code>Missed</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUtterancesViewRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUtterancesViewRequest:
    out: GetUtterancesViewRequest = {}  # type: ignore[typeddict-item]
    return out
