"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateEdgeDeploymentStageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.deployment_stages
    import aws_sdk_sagemaker.types.entity_name


class CreateEdgeDeploymentStageRequest(TypedDict):
    edge_deployment_plan_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan.</p>"""
    stages: NotRequired["aws_sdk_sagemaker.types.deployment_stages.DeploymentStages"]
    """<p>List of stages to be added to the edge deployment plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEdgeDeploymentStageRequest) -> dict:
    out: dict = {}
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "stages" in value:
        import aws_sdk_sagemaker.types.deployment_stages

        out["Stages"] = (
            aws_sdk_sagemaker.types.deployment_stages.serialize_aws_json_1_1(
                value["stages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEdgeDeploymentStageRequest:
    out: CreateEdgeDeploymentStageRequest = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if "Stages" in data:
        import aws_sdk_sagemaker.types.deployment_stages

        out["stages"] = (
            aws_sdk_sagemaker.types.deployment_stages.deserialize_aws_json_1_1(
                data["Stages"]
            )
        )
    return out
