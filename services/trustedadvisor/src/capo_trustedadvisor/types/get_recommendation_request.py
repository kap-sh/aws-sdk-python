"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#GetRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.account_recommendation_identifier
    import capo_trustedadvisor.types.recommendation_language


class GetRecommendationRequest(TypedDict, closed=True):
    recommendation_identifier: "capo_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier"
    """<p>The Recommendation identifier</p>"""
    language: NotRequired[
        "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
    ]
    """<p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommendationRequest:
    out: GetRecommendationRequest = {}  # type: ignore[typeddict-item]
    return out
