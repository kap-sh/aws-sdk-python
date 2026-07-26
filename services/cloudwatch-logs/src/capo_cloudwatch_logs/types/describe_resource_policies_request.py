"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeResourcePoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.policy_scope


class DescribeResourcePoliciesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of resource policies to be displayed with one call of this API.</p>"""
    resource_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the CloudWatch Logs resource for which to query the resource policy.</p>"""
    policy_scope: NotRequired["capo_cloudwatch_logs.types.policy_scope.PolicyScope"]
    """<p>Specifies the scope of the resource policy. Valid values are <code>ACCOUNT</code> or <code>RESOURCE</code>. When not specified, defaults to <code>ACCOUNT</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourcePoliciesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "policy_scope" in value:
        import capo_cloudwatch_logs.types.policy_scope

        out["policyScope"] = (
            capo_cloudwatch_logs.types.policy_scope.serialize_aws_json_1_1(
                value["policy_scope"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourcePoliciesRequest:
    out: DescribeResourcePoliciesRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "policyScope" in data:
        import capo_cloudwatch_logs.types.policy_scope

        out["policy_scope"] = (
            capo_cloudwatch_logs.types.policy_scope.deserialize_aws_json_1_1(
                data["policyScope"]
            )
        )
    return out
