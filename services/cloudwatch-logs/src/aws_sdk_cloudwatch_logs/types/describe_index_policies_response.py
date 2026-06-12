"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeIndexPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.index_policies
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeIndexPoliciesResponse(TypedDict):
    index_policies: NotRequired[
        "aws_sdk_cloudwatch_logs.types.index_policies.IndexPolicies"
    ]
    """<p>An array containing the field index policies.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIndexPoliciesResponse) -> dict:
    out: dict = {}
    if "index_policies" in value:
        import aws_sdk_cloudwatch_logs.types.index_policies

        out["indexPolicies"] = (
            aws_sdk_cloudwatch_logs.types.index_policies.serialize_aws_json_1_1(
                value["index_policies"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIndexPoliciesResponse:
    out: DescribeIndexPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "indexPolicies" in data:
        import aws_sdk_cloudwatch_logs.types.index_policies

        out["index_policies"] = (
            aws_sdk_cloudwatch_logs.types.index_policies.deserialize_aws_json_1_1(
                data["indexPolicies"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
