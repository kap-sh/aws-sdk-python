"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#DescribeScalingPlanResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.max_results
    import aws_sdk_auto_scaling_plans.types.next_token
    import aws_sdk_auto_scaling_plans.types.scaling_plan_name
    import aws_sdk_auto_scaling_plans.types.scaling_plan_version


class DescribeScalingPlanResourcesRequest(TypedDict):
    scaling_plan_name: (
        "aws_sdk_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
    )
    """<p>The name of the scaling plan.</p>"""
    scaling_plan_version: (
        "aws_sdk_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    )
    """<p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>"""
    max_results: NotRequired["aws_sdk_auto_scaling_plans.types.max_results.MaxResults"]
    """<p>The maximum number of scalable resources to return. The value must be between 1 and 50. The default value is 50.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling_plans.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScalingPlanResourcesRequest) -> dict:
    out: dict = {}
    out["ScalingPlanName"] = value["scaling_plan_name"]
    out["ScalingPlanVersion"] = value["scaling_plan_version"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScalingPlanResourcesRequest:
    out: DescribeScalingPlanResourcesRequest = {}  # type: ignore[typeddict-item]
    if "ScalingPlanName" in data:
        out["scaling_plan_name"] = data["ScalingPlanName"]
    else:
        raise DeserializationError(
            "DescribeScalingPlanResourcesRequest.scaling_plan_name required"
        )
    if "ScalingPlanVersion" in data:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    else:
        raise DeserializationError(
            "DescribeScalingPlanResourcesRequest.scaling_plan_version required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
