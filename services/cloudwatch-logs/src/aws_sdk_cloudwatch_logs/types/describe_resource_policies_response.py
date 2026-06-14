"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeResourcePoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.resource_policies


class DescribeResourcePoliciesResponse(TypedDict):
    resource_policies: NotRequired[
        "aws_sdk_cloudwatch_logs.types.resource_policies.ResourcePolicies"
    ]
    """<p>The resource policies that exist in this account.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourcePoliciesResponse) -> dict:
    out: dict = {}
    if "resource_policies" in value:
        import aws_sdk_cloudwatch_logs.types.resource_policies

        out["resourcePolicies"] = (
            aws_sdk_cloudwatch_logs.types.resource_policies.serialize_aws_json_1_1(
                value["resource_policies"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourcePoliciesResponse:
    out: DescribeResourcePoliciesResponse = {}  # type: ignore[typeddict-item]
    if "resourcePolicies" in data:
        import aws_sdk_cloudwatch_logs.types.resource_policies

        out["resource_policies"] = (
            aws_sdk_cloudwatch_logs.types.resource_policies.deserialize_aws_json_1_1(
                data["resourcePolicies"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
