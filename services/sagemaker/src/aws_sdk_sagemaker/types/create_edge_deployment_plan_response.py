"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateEdgeDeploymentPlanResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_deployment_plan_arn


class CreateEdgeDeploymentPlanResponse(TypedDict):
    edge_deployment_plan_arn: NotRequired[
        "aws_sdk_sagemaker.types.edge_deployment_plan_arn.EdgeDeploymentPlanArn"
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
