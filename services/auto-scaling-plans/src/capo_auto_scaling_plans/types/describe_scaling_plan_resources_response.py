"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#DescribeScalingPlanResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.next_token
    import capo_auto_scaling_plans.types.scaling_plan_resources


class DescribeScalingPlanResourcesResponse(TypedDict, closed=True):
    scaling_plan_resources: NotRequired[
        "capo_auto_scaling_plans.types.scaling_plan_resources.ScalingPlanResources"
    ]
    """<p>Information about the scalable resources.</p>"""
    next_token: NotRequired["capo_auto_scaling_plans.types.next_token.NextToken"]
    """<p>The token required to get the next set of results. This value is <code>null</code> if there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScalingPlanResourcesResponse) -> dict:
    out: dict = {}
    if "scaling_plan_resources" in value:
        import capo_auto_scaling_plans.types.scaling_plan_resources

        out["ScalingPlanResources"] = (
            capo_auto_scaling_plans.types.scaling_plan_resources.serialize_aws_json_1_1(
                value["scaling_plan_resources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScalingPlanResourcesResponse:
    out: DescribeScalingPlanResourcesResponse = {}  # type: ignore[typeddict-item]
    if "ScalingPlanResources" in data:
        import capo_auto_scaling_plans.types.scaling_plan_resources

        out["scaling_plan_resources"] = (
            capo_auto_scaling_plans.types.scaling_plan_resources.deserialize_aws_json_1_1(
                data["ScalingPlanResources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
