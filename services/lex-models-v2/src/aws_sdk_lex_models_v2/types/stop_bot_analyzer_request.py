"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StopBotAnalyzerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.uuid


class StopBotAnalyzerRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot.</p>"""
    bot_analyzer_request_id: "aws_sdk_lex_models_v2.types.uuid.UUID"
    """<p>The unique identifier of the analysis request to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopBotAnalyzerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopBotAnalyzerRequest:
    out: StopBotAnalyzerRequest = {}  # type: ignore[typeddict-item]
    return out
