"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeploymentStage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.device_selection_config
    import capo_sagemaker.types.edge_deployment_config
    import capo_sagemaker.types.entity_name


class DeploymentStage(TypedDict, closed=True):
    stage_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the stage.</p>"""
    device_selection_config: NotRequired[
        "capo_sagemaker.types.device_selection_config.DeviceSelectionConfig"
    ]
    """<p>Configuration of the devices in the stage.</p>"""
    deployment_config: NotRequired[
        "capo_sagemaker.types.edge_deployment_config.EdgeDeploymentConfig"
    ]
    """<p>Configuration of the deployment details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStage) -> dict:
    out: dict = {}
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    if "device_selection_config" in value:
        import capo_sagemaker.types.device_selection_config

        out["DeviceSelectionConfig"] = (
            capo_sagemaker.types.device_selection_config.serialize_aws_json_1_1(
                value["device_selection_config"]
            )
        )
    if "deployment_config" in value:
        import capo_sagemaker.types.edge_deployment_config

        out["DeploymentConfig"] = (
            capo_sagemaker.types.edge_deployment_config.serialize_aws_json_1_1(
                value["deployment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentStage:
    out: DeploymentStage = {}  # type: ignore[typeddict-item]
    if "StageName" in data:
        out["stage_name"] = data["StageName"]
    if "DeviceSelectionConfig" in data:
        import capo_sagemaker.types.device_selection_config

        out["device_selection_config"] = (
            capo_sagemaker.types.device_selection_config.deserialize_aws_json_1_1(
                data["DeviceSelectionConfig"]
            )
        )
    if "DeploymentConfig" in data:
        import capo_sagemaker.types.edge_deployment_config

        out["deployment_config"] = (
            capo_sagemaker.types.edge_deployment_config.deserialize_aws_json_1_1(
                data["DeploymentConfig"]
            )
        )
    return out
