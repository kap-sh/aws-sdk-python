"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateEdgeDeploymentPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.deployment_stages
    import aws_sdk_sagemaker.types.edge_deployment_model_configs
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.tag_list


class CreateEdgeDeploymentPlanRequest(TypedDict, closed=True):
    edge_deployment_plan_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan.</p>"""
    model_configs: NotRequired[
        "aws_sdk_sagemaker.types.edge_deployment_model_configs.EdgeDeploymentModelConfigs"
    ]
    """<p>List of models associated with the edge deployment plan.</p>"""
    device_fleet_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The device fleet used for this edge deployment plan.</p>"""
    stages: NotRequired["aws_sdk_sagemaker.types.deployment_stages.DeploymentStages"]
    """<p>List of stages of the edge deployment plan. The number of stages is limited to 10 per deployment.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>List of tags with which to tag the edge deployment plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEdgeDeploymentPlanRequest) -> dict:
    out: dict = {}
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "model_configs" in value:
        import aws_sdk_sagemaker.types.edge_deployment_model_configs

        out["ModelConfigs"] = (
            aws_sdk_sagemaker.types.edge_deployment_model_configs.serialize_aws_json_1_1(
                value["model_configs"]
            )
        )
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "stages" in value:
        import aws_sdk_sagemaker.types.deployment_stages

        out["Stages"] = (
            aws_sdk_sagemaker.types.deployment_stages.serialize_aws_json_1_1(
                value["stages"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEdgeDeploymentPlanRequest:
    out: CreateEdgeDeploymentPlanRequest = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if "ModelConfigs" in data:
        import aws_sdk_sagemaker.types.edge_deployment_model_configs

        out["model_configs"] = (
            aws_sdk_sagemaker.types.edge_deployment_model_configs.deserialize_aws_json_1_1(
                data["ModelConfigs"]
            )
        )
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "Stages" in data:
        import aws_sdk_sagemaker.types.deployment_stages

        out["stages"] = (
            aws_sdk_sagemaker.types.deployment_stages.deserialize_aws_json_1_1(
                data["Stages"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
