"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListRecommendationResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.account_recommendation_identifier
    import capo_trustedadvisor.types.exclusion_status
    import capo_trustedadvisor.types.recommendation_language
    import capo_trustedadvisor.types.resource_status


class ListRecommendationResourcesRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    status: NotRequired["capo_trustedadvisor.types.resource_status.ResourceStatus"]
    """<p>The status of the resource</p>"""
    exclusion_status: NotRequired[
        "capo_trustedadvisor.types.exclusion_status.ExclusionStatus"
    ]
    """<p>The exclusion status of the resource</p>"""
    region_code: NotRequired["str"]
    """<p>The AWS Region code of the resource</p>"""
    recommendation_identifier: "capo_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier"
    """<p>The Recommendation identifier</p>"""
    language: NotRequired[
        "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
    ]
    """<p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecommendationResourcesRequest:
    out: ListRecommendationResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
