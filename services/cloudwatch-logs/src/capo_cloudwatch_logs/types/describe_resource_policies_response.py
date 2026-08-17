"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeResourcePoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.resource_policies


class DescribeResourcePoliciesResponse(TypedDict, closed=True):
    resource_policies: NotRequired[
        "capo_cloudwatch_logs.types.resource_policies.ResourcePolicies"
    ]
    """<p>The resource policies that exist in this account.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourcePoliciesResponse) -> dict:
    out: dict = {}
    if "resource_policies" in value:
        import capo_cloudwatch_logs.types.resource_policies

        out["resourcePolicies"] = (
            capo_cloudwatch_logs.types.resource_policies.serialize_aws_json_1_1(
                value["resource_policies"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourcePoliciesResponse:
    out: DescribeResourcePoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourcePolicies") is not None:
        import capo_cloudwatch_logs.types.resource_policies

        out["resource_policies"] = (
            capo_cloudwatch_logs.types.resource_policies.deserialize_aws_json_1_1(
                data["resourcePolicies"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
