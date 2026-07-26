"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgePresetDeploymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_preset_deployment_artifact
    import capo_sagemaker.types.edge_preset_deployment_status
    import capo_sagemaker.types.edge_preset_deployment_type
    import capo_sagemaker.types.string


class EdgePresetDeploymentOutput(TypedDict, closed=True):
    type: NotRequired[
        "capo_sagemaker.types.edge_preset_deployment_type.EdgePresetDeploymentType"
    ]
    """<p>The deployment type created by SageMaker Edge Manager. Currently only supports Amazon Web Services IoT Greengrass Version 2 components.</p>"""
    artifact: NotRequired[
        "capo_sagemaker.types.edge_preset_deployment_artifact.EdgePresetDeploymentArtifact"
    ]
    """<p>The Amazon Resource Name (ARN) of the generated deployable resource.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.edge_preset_deployment_status.EdgePresetDeploymentStatus"
    ]
    """<p>The status of the deployable resource.</p>"""
    status_message: NotRequired["capo_sagemaker.types.string.String"]
    """<p>Returns a message describing the status of the deployed resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgePresetDeploymentOutput) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_sagemaker.types.edge_preset_deployment_type

        out["Type"] = (
            capo_sagemaker.types.edge_preset_deployment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "artifact" in value:
        out["Artifact"] = value["artifact"]
    if "status" in value:
        import capo_sagemaker.types.edge_preset_deployment_status

        out["Status"] = (
            capo_sagemaker.types.edge_preset_deployment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgePresetDeploymentOutput:
    out: EdgePresetDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_sagemaker.types.edge_preset_deployment_type

        out["type"] = (
            capo_sagemaker.types.edge_preset_deployment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Artifact" in data:
        out["artifact"] = data["Artifact"]
    if "Status" in data:
        import capo_sagemaker.types.edge_preset_deployment_status

        out["status"] = (
            capo_sagemaker.types.edge_preset_deployment_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
