"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgePresetDeploymentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_preset_deployment_artifact
    import aws_sdk_sagemaker.types.edge_preset_deployment_status
    import aws_sdk_sagemaker.types.edge_preset_deployment_type
    import aws_sdk_sagemaker.types.string


class EdgePresetDeploymentOutput(TypedDict):
    type: NotRequired[
        "aws_sdk_sagemaker.types.edge_preset_deployment_type.EdgePresetDeploymentType"
    ]
    """<p>The deployment type created by SageMaker Edge Manager. Currently only supports Amazon Web Services IoT Greengrass Version 2 components.</p>"""
    artifact: NotRequired[
        "aws_sdk_sagemaker.types.edge_preset_deployment_artifact.EdgePresetDeploymentArtifact"
    ]
    """<p>The Amazon Resource Name (ARN) of the generated deployable resource.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.edge_preset_deployment_status.EdgePresetDeploymentStatus"
    ]
    """<p>The status of the deployable resource.</p>"""
    status_message: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>Returns a message describing the status of the deployed resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgePresetDeploymentOutput) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_sagemaker.types.edge_preset_deployment_type

        out["Type"] = (
            aws_sdk_sagemaker.types.edge_preset_deployment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "artifact" in value:
        out["Artifact"] = value["artifact"]
    if "status" in value:
        import aws_sdk_sagemaker.types.edge_preset_deployment_status

        out["Status"] = (
            aws_sdk_sagemaker.types.edge_preset_deployment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgePresetDeploymentOutput:
    out: EdgePresetDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_sagemaker.types.edge_preset_deployment_type

        out["type"] = (
            aws_sdk_sagemaker.types.edge_preset_deployment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Artifact" in data:
        out["artifact"] = data["Artifact"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.edge_preset_deployment_status

        out["status"] = (
            aws_sdk_sagemaker.types.edge_preset_deployment_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
