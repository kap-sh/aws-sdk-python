"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateEdgeDeploymentPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_deployment_plan_arn


class CreateEdgeDeploymentPlanResponse(TypedDict, closed=True):
    edge_deployment_plan_arn: NotRequired[
        "capo_sagemaker.types.edge_deployment_plan_arn.EdgeDeploymentPlanArn"
    ]
    """<p>The ARN of the edge deployment plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEdgeDeploymentPlanResponse) -> dict:
    out: dict = {}
    if "edge_deployment_plan_arn" in value:
        out["EdgeDeploymentPlanArn"] = value["edge_deployment_plan_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEdgeDeploymentPlanResponse:
    out: CreateEdgeDeploymentPlanResponse = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanArn" in data:
        out["edge_deployment_plan_arn"] = data["EdgeDeploymentPlanArn"]
    return out
