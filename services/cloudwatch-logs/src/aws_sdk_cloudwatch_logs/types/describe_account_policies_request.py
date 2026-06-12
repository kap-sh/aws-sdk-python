"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeAccountPoliciesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.account_ids
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.policy_name
    import aws_sdk_cloudwatch_logs.types.policy_type


class DescribeAccountPoliciesRequest(TypedDict):
    policy_type: "aws_sdk_cloudwatch_logs.types.policy_type.PolicyType"
    """<p>Use this parameter to limit the returned policies to only the policies that match the policy type that you specify.</p>"""
    policy_name: NotRequired["aws_sdk_cloudwatch_logs.types.policy_name.PolicyName"]
    """<p>Use this parameter to limit the returned policies to only the policy with the name that you specify.</p>"""
    account_identifiers: NotRequired[
        "aws_sdk_cloudwatch_logs.types.account_ids.AccountIds"
    ]
    """<p>If you are using an account that is set up as a monitoring account for CloudWatch unified cross-account observability, you can use this to specify the account ID of a source account. If you do, the operation returns the account policy for the specified account. Currently, you can specify only one account ID in this parameter.</p> <p>If you omit this parameter, only the policy in the current account is returned.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountPoliciesRequest) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.policy_type

    out["policyType"] = (
        aws_sdk_cloudwatch_logs.types.policy_type.serialize_aws_json_1_1(
            value["policy_type"]
        )
    )
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "account_identifiers" in value:
        import aws_sdk_cloudwatch_logs.types.account_ids

        out["accountIdentifiers"] = (
            aws_sdk_cloudwatch_logs.types.account_ids.serialize_aws_json_1_1(
                value["account_identifiers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountPoliciesRequest:
    out: DescribeAccountPoliciesRequest = {}  # type: ignore[typeddict-item]
    if "policyType" in data:
        import aws_sdk_cloudwatch_logs.types.policy_type

        out["policy_type"] = (
            aws_sdk_cloudwatch_logs.types.policy_type.deserialize_aws_json_1_1(
                data["policyType"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccountPoliciesRequest.policy_type required"
        )
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "accountIdentifiers" in data:
        import aws_sdk_cloudwatch_logs.types.account_ids

        out["account_identifiers"] = (
            aws_sdk_cloudwatch_logs.types.account_ids.deserialize_aws_json_1_1(
                data["accountIdentifiers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
