"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeAccountPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.account_policies
    import capo_cloudwatch_logs.types.next_token


class DescribeAccountPoliciesResponse(TypedDict, closed=True):
    account_policies: NotRequired[
        "capo_cloudwatch_logs.types.account_policies.AccountPolicies"
    ]
    """<p>An array of structures that contain information about the CloudWatch Logs account policies that match the specified filters.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. The token expires after 24 hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountPoliciesResponse) -> dict:
    out: dict = {}
    if "account_policies" in value:
        import capo_cloudwatch_logs.types.account_policies

        out["accountPolicies"] = (
            capo_cloudwatch_logs.types.account_policies.serialize_aws_json_1_1(
                value["account_policies"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountPoliciesResponse:
    out: DescribeAccountPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountPolicies") is not None:
        import capo_cloudwatch_logs.types.account_policies

        out["account_policies"] = (
            capo_cloudwatch_logs.types.account_policies.deserialize_aws_json_1_1(
                data["accountPolicies"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
