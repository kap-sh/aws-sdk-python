"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ListEnrollmentStatusesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.account_enrollment_statuses


class ListEnrollmentStatusesResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_cost_optimization_hub.types.account_enrollment_statuses.AccountEnrollmentStatuses"
    ]
    """<p>The enrollment status of a specific account ID, including creation and last updated timestamps.</p>"""
    include_member_accounts: NotRequired["bool"]
    """<p>The enrollment status of all member accounts in the organization if the account is the management account or delegated administrator.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnrollmentStatusesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_cost_optimization_hub.types.account_enrollment_statuses

        out["items"] = (
            aws_sdk_cost_optimization_hub.types.account_enrollment_statuses.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "include_member_accounts" in value:
        out["includeMemberAccounts"] = value["include_member_accounts"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnrollmentStatusesResponse:
    out: ListEnrollmentStatusesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_cost_optimization_hub.types.account_enrollment_statuses

        out["items"] = (
            aws_sdk_cost_optimization_hub.types.account_enrollment_statuses.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "includeMemberAccounts" in data:
        out["include_member_accounts"] = data["includeMemberAccounts"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
