"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteEdgeDeploymentStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name


class DeleteEdgeDeploymentStageRequest(TypedDict, closed=True):
    edge_deployment_plan_name: NotRequired[
        "capo_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan from which the stage will be deleted.</p>"""
    stage_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the stage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEdgeDeploymentStageRequest) -> dict:
    out: dict = {}
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEdgeDeploymentStageRequest:
    out: DeleteEdgeDeploymentStageRequest = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if "StageName" in data:
        out["stage_name"] = data["StageName"]
    return out
