"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotAnalyzerRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.uuid


class DeleteBotAnalyzerRecommendationRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot.</p>"""
    bot_analyzer_request_id: "capo_lex_models_v2.types.uuid.UUID"
    """<p>The unique identifier of the analysis request whose recommendations should be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotAnalyzerRecommendationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotAnalyzerRecommendationRequest:
    out: DeleteBotAnalyzerRecommendationRequest = {}  # type: ignore[typeddict-item]
    return out
