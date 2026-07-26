"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteEdgeDeploymentPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name


class DeleteEdgeDeploymentPlanRequest(TypedDict, closed=True):
    edge_deployment_plan_name: NotRequired[
        "capo_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEdgeDeploymentPlanRequest) -> dict:
    out: dict = {}
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEdgeDeploymentPlanRequest:
    out: DeleteEdgeDeploymentPlanRequest = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    return out
