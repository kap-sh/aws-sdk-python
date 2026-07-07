"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ListEnrollmentStatusesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.account_id
    import aws_sdk_cost_optimization_hub.types.max_results


class ListEnrollmentStatusesRequest(TypedDict, closed=True):
    include_organization_info: "bool"
    """<p>Indicates whether to return the enrollment status for the organization.</p>"""
    account_id: NotRequired["aws_sdk_cost_optimization_hub.types.account_id.AccountId"]
    """<p>The account ID of a member account in the organization.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_cost_optimization_hub.types.max_results.MaxResults"
    ]
    """<p>The maximum number of objects that are returned for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnrollmentStatusesRequest) -> dict:
    out: dict = {}
    out["includeOrganizationInfo"] = value.get("include_organization_info", False)
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnrollmentStatusesRequest:
    out: ListEnrollmentStatusesRequest = {}  # type: ignore[typeddict-item]
    if "includeOrganizationInfo" in data:
        out["include_organization_info"] = data["includeOrganizationInfo"]
    else:
        out["include_organization_info"] = False
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
