"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListChecksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_aws_service
    import capo_trustedadvisor.types.recommendation_language
    import capo_trustedadvisor.types.recommendation_pillar
    import capo_trustedadvisor.types.recommendation_source


class ListChecksRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    pillar: NotRequired[
        "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
    ]
    """<p>The pillar of the check</p>"""
    aws_service: NotRequired[
        "capo_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
    ]
    """<p>The aws service associated with the check</p>"""
    source: NotRequired[
        "capo_trustedadvisor.types.recommendation_source.RecommendationSource"
    ]
    """<p>The source of the check</p>"""
    language: NotRequired[
        "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
    ]
    """<p>The ISO 639-1 code for the language that you want your checks to appear in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChecksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChecksRequest:
    out: ListChecksRequest = {}  # type: ignore[typeddict-item]
    return out
