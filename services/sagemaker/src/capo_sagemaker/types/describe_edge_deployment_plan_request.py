"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeEdgeDeploymentPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.deployment_stage_max_results
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.next_token


class DescribeEdgeDeploymentPlanRequest(TypedDict, closed=True):
    edge_deployment_plan_name: NotRequired[
        "capo_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the deployment plan to describe.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the edge deployment plan has enough stages to require tokening, then this is the response from the last list of stages returned.</p>"""
    max_results: NotRequired[
        "capo_sagemaker.types.deployment_stage_max_results.DeploymentStageMaxResults"
    ]
    """<p>The maximum number of results to select (50 by default).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEdgeDeploymentPlanRequest) -> dict:
    out: dict = {}
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEdgeDeploymentPlanRequest:
    out: DescribeEdgeDeploymentPlanRequest = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
