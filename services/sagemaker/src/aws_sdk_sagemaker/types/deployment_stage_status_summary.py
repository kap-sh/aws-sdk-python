"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeploymentStageStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.device_selection_config
    import aws_sdk_sagemaker.types.edge_deployment_config
    import aws_sdk_sagemaker.types.edge_deployment_status
    import aws_sdk_sagemaker.types.entity_name


class DeploymentStageStatusSummary(TypedDict, closed=True):
    stage_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the stage.</p>"""
    device_selection_config: NotRequired[
        "aws_sdk_sagemaker.types.device_selection_config.DeviceSelectionConfig"
    ]
    """<p>Configuration of the devices in the stage.</p>"""
    deployment_config: NotRequired[
        "aws_sdk_sagemaker.types.edge_deployment_config.EdgeDeploymentConfig"
    ]
    """<p>Configuration of the deployment details.</p>"""
    deployment_status: NotRequired[
        "aws_sdk_sagemaker.types.edge_deployment_status.EdgeDeploymentStatus"
    ]
    """<p>General status of the current state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStageStatusSummary) -> dict:
    out: dict = {}
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    if "device_selection_config" in value:
        import aws_sdk_sagemaker.types.device_selection_config

        out["DeviceSelectionConfig"] = (
            aws_sdk_sagemaker.types.device_selection_config.serialize_aws_json_1_1(
                value["device_selection_config"]
            )
        )
    if "deployment_config" in value:
        import aws_sdk_sagemaker.types.edge_deployment_config

        out["DeploymentConfig"] = (
            aws_sdk_sagemaker.types.edge_deployment_config.serialize_aws_json_1_1(
                value["deployment_config"]
            )
        )
    if "deployment_status" in value:
        import aws_sdk_sagemaker.types.edge_deployment_status

        out["DeploymentStatus"] = (
            aws_sdk_sagemaker.types.edge_deployment_status.serialize_aws_json_1_1(
                value["deployment_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentStageStatusSummary:
    out: DeploymentStageStatusSummary = {}  # type: ignore[typeddict-item]
    if "StageName" in data:
        out["stage_name"] = data["StageName"]
    if "DeviceSelectionConfig" in data:
        import aws_sdk_sagemaker.types.device_selection_config

        out["device_selection_config"] = (
            aws_sdk_sagemaker.types.device_selection_config.deserialize_aws_json_1_1(
                data["DeviceSelectionConfig"]
            )
        )
    if "DeploymentConfig" in data:
        import aws_sdk_sagemaker.types.edge_deployment_config

        out["deployment_config"] = (
            aws_sdk_sagemaker.types.edge_deployment_config.deserialize_aws_json_1_1(
                data["DeploymentConfig"]
            )
        )
    if "DeploymentStatus" in data:
        import aws_sdk_sagemaker.types.edge_deployment_status

        out["deployment_status"] = (
            aws_sdk_sagemaker.types.edge_deployment_status.deserialize_aws_json_1_1(
                data["DeploymentStatus"]
            )
        )
    return out
