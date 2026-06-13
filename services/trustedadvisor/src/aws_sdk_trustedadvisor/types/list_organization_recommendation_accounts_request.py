"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListOrganizationRecommendationAccountsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.account_id
    import aws_sdk_trustedadvisor.types.organization_recommendation_identifier


class ListOrganizationRecommendationAccountsRequest(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    organization_recommendation_identifier: "aws_sdk_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier"
    """<p>The Recommendation identifier</p>"""
    affected_account_id: NotRequired[
        "aws_sdk_trustedadvisor.types.account_id.AccountId"
    ]
    """<p>An account affected by this organization recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationRecommendationAccountsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOrganizationRecommendationAccountsRequest:
    out: ListOrganizationRecommendationAccountsRequest = {}  # type: ignore[typeddict-item]
    return out
