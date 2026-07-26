"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#GetOrganizationRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.organization_recommendation


class GetOrganizationRecommendationResponse(TypedDict, closed=True):
    organization_recommendation: NotRequired[
        "capo_trustedadvisor.types.organization_recommendation.OrganizationRecommendation"
    ]
    """<p>The Recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOrganizationRecommendationResponse) -> dict:
    out: dict = {}
    if "organization_recommendation" in value:
        import capo_trustedadvisor.types.organization_recommendation

        out["organizationRecommendation"] = (
            capo_trustedadvisor.types.organization_recommendation.serialize_json(
                value["organization_recommendation"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetOrganizationRecommendationResponse:
    out: GetOrganizationRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "organizationRecommendation" in data:
        import capo_trustedadvisor.types.organization_recommendation

        out["organization_recommendation"] = (
            capo_trustedadvisor.types.organization_recommendation.deserialize_json(
                data["organizationRecommendation"]
            )
        )
    return out
