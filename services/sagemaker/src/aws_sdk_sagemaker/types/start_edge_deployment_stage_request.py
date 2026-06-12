"""Generated from Smithy shape ``com.amazonaws.sagemaker#StartEdgeDeploymentStageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class StartEdgeDeploymentStageRequest(TypedDict):
    edge_deployment_plan_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan to start.</p>"""
    stage_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the stage to start.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartEdgeDeploymentStageRequest) -> dict:
    out: dict = {}
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartEdgeDeploymentStageRequest:
    out: StartEdgeDeploymentStageRequest = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if "StageName" in data:
        out["stage_name"] = data["StageName"]
    return out
