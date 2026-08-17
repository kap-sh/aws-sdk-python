"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeIndexPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.index_policies
    import capo_cloudwatch_logs.types.next_token


class DescribeIndexPoliciesResponse(TypedDict, closed=True):
    index_policies: NotRequired[
        "capo_cloudwatch_logs.types.index_policies.IndexPolicies"
    ]
    """<p>An array containing the field index policies.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIndexPoliciesResponse) -> dict:
    out: dict = {}
    if "index_policies" in value:
        import capo_cloudwatch_logs.types.index_policies

        out["indexPolicies"] = (
            capo_cloudwatch_logs.types.index_policies.serialize_aws_json_1_1(
                value["index_policies"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIndexPoliciesResponse:
    out: DescribeIndexPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("indexPolicies") is not None:
        import capo_cloudwatch_logs.types.index_policies

        out["index_policies"] = (
            capo_cloudwatch_logs.types.index_policies.deserialize_aws_json_1_1(
                data["indexPolicies"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
