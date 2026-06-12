"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#DescribeScalingPlansResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.next_token
    import aws_sdk_auto_scaling_plans.types.scaling_plans


class DescribeScalingPlansResponse(TypedDict):
    scaling_plans: NotRequired[
        "aws_sdk_auto_scaling_plans.types.scaling_plans.ScalingPlans"
    ]
    """<p>Information about the scaling plans.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling_plans.types.next_token.NextToken"]
    """<p>The token required to get the next set of results. This value is <code>null</code> if there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScalingPlansResponse) -> dict:
    out: dict = {}
    if "scaling_plans" in value:
        import aws_sdk_auto_scaling_plans.types.scaling_plans

        out["ScalingPlans"] = (
            aws_sdk_auto_scaling_plans.types.scaling_plans.serialize_aws_json_1_1(
                value["scaling_plans"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScalingPlansResponse:
    out: DescribeScalingPlansResponse = {}  # type: ignore[typeddict-item]
    if "ScalingPlans" in data:
        import aws_sdk_auto_scaling_plans.types.scaling_plans

        out["scaling_plans"] = (
            aws_sdk_auto_scaling_plans.types.scaling_plans.deserialize_aws_json_1_1(
                data["ScalingPlans"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
