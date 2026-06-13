"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListOrganizationRecommendationResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.account_id
    import aws_sdk_trustedadvisor.types.exclusion_status
    import aws_sdk_trustedadvisor.types.organization_recommendation_identifier
    import aws_sdk_trustedadvisor.types.resource_status


class ListOrganizationRecommendationResourcesRequest(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    status: NotRequired["aws_sdk_trustedadvisor.types.resource_status.ResourceStatus"]
    """<p>The status of the resource</p>"""
    exclusion_status: NotRequired[
        "aws_sdk_trustedadvisor.types.exclusion_status.ExclusionStatus"
    ]
    """<p>The exclusion status of the resource</p>"""
    region_code: NotRequired["str"]
    """<p>The AWS Region code of the resource</p>"""
    organization_recommendation_identifier: "aws_sdk_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier"
    """<p>The AWS Organization organization's Recommendation identifier</p>"""
    affected_account_id: NotRequired[
        "aws_sdk_trustedadvisor.types.account_id.AccountId"
    ]
    """<p>An account affected by this organization recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationRecommendationResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOrganizationRecommendationResourcesRequest:
    out: ListOrganizationRecommendationResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
