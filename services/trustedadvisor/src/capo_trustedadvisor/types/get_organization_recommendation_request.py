"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#GetOrganizationRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.organization_recommendation_identifier


class GetOrganizationRecommendationRequest(TypedDict, closed=True):
    organization_recommendation_identifier: "capo_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier"
    """<p>The Recommendation identifier</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOrganizationRecommendationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOrganizationRecommendationRequest:
    out: GetOrganizationRecommendationRequest = {}  # type: ignore[typeddict-item]
    return out
