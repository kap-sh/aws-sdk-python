"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopEdgeDeploymentStageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class StopEdgeDeploymentStageRequest(TypedDict):
    edge_deployment_plan_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan to stop.</p>"""
    stage_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the stage to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopEdgeDeploymentStageRequest) -> dict:
    out: dict = {}
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopEdgeDeploymentStageRequest:
    out: StopEdgeDeploymentStageRequest = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if "StageName" in data:
        out["stage_name"] = data["StageName"]
    return out
