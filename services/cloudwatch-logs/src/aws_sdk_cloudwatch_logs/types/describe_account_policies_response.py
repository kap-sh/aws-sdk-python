"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeAccountPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.account_policies
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeAccountPoliciesResponse(TypedDict):
    account_policies: NotRequired[
        "aws_sdk_cloudwatch_logs.types.account_policies.AccountPolicies"
    ]
    """<p>An array of structures that contain information about the CloudWatch Logs account policies that match the specified filters.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. The token expires after 24 hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountPoliciesResponse) -> dict:
    out: dict = {}
    if "account_policies" in value:
        import aws_sdk_cloudwatch_logs.types.account_policies

        out["accountPolicies"] = (
            aws_sdk_cloudwatch_logs.types.account_policies.serialize_aws_json_1_1(
                value["account_policies"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountPoliciesResponse:
    out: DescribeAccountPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "accountPolicies" in data:
        import aws_sdk_cloudwatch_logs.types.account_policies

        out["account_policies"] = (
            aws_sdk_cloudwatch_logs.types.account_policies.deserialize_aws_json_1_1(
                data["accountPolicies"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
