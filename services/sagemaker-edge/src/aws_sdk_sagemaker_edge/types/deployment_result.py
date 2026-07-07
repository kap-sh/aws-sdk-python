"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#DeploymentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_edge.types.deployment_models
    import aws_sdk_sagemaker_edge.types.entity_name
    import aws_sdk_sagemaker_edge.types.string
    import aws_sdk_sagemaker_edge.types.timestamp


class DeploymentResult(TypedDict, closed=True):
    deployment_name: NotRequired["aws_sdk_sagemaker_edge.types.entity_name.EntityName"]
    """<p>The name and unique ID of the deployment.</p>"""
    deployment_status: NotRequired[
        "aws_sdk_sagemaker_edge.types.entity_name.EntityName"
    ]
    """<p>Returns the bucket error code.</p>"""
    deployment_status_message: NotRequired["aws_sdk_sagemaker_edge.types.string.String"]
    """<p>Returns the detailed error message.</p>"""
    deployment_start_time: NotRequired[
        "aws_sdk_sagemaker_edge.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of when the deployment was started on the agent.</p>"""
    deployment_end_time: NotRequired["aws_sdk_sagemaker_edge.types.timestamp.Timestamp"]
    """<p>The timestamp of when the deployment was ended, and the agent got the deployment results.</p>"""
    deployment_models: NotRequired[
        "aws_sdk_sagemaker_edge.types.deployment_models.DeploymentModels"
    ]
    """<p>Returns a list of models deployed on the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentResult) -> dict:
    out: dict = {}
    if "deployment_name" in value:
        out["DeploymentName"] = value["deployment_name"]
    if "deployment_status" in value:
        out["DeploymentStatus"] = value["deployment_status"]
    if "deployment_status_message" in value:
        out["DeploymentStatusMessage"] = value["deployment_status_message"]
    if "deployment_start_time" in value:
        import aws_sdk_sagemaker_edge.types.timestamp

        out["DeploymentStartTime"] = (
            aws_sdk_sagemaker_edge.types.timestamp.serialize_json(
                value["deployment_start_time"]
            )
        )
    if "deployment_end_time" in value:
        import aws_sdk_sagemaker_edge.types.timestamp

        out["DeploymentEndTime"] = (
            aws_sdk_sagemaker_edge.types.timestamp.serialize_json(
                value["deployment_end_time"]
            )
        )
    if "deployment_models" in value:
        import aws_sdk_sagemaker_edge.types.deployment_models

        out["DeploymentModels"] = (
            aws_sdk_sagemaker_edge.types.deployment_models.serialize_json(
                value["deployment_models"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeploymentResult:
    out: DeploymentResult = {}  # type: ignore[typeddict-item]
    if "DeploymentName" in data:
        out["deployment_name"] = data["DeploymentName"]
    if "DeploymentStatus" in data:
        out["deployment_status"] = data["DeploymentStatus"]
    if "DeploymentStatusMessage" in data:
        out["deployment_status_message"] = data["DeploymentStatusMessage"]
    if "DeploymentStartTime" in data:
        import aws_sdk_sagemaker_edge.types.timestamp

        out["deployment_start_time"] = (
            aws_sdk_sagemaker_edge.types.timestamp.deserialize_json(
                data["DeploymentStartTime"]
            )
        )
    if "DeploymentEndTime" in data:
        import aws_sdk_sagemaker_edge.types.timestamp

        out["deployment_end_time"] = (
            aws_sdk_sagemaker_edge.types.timestamp.deserialize_json(
                data["DeploymentEndTime"]
            )
        )
    if "DeploymentModels" in data:
        import aws_sdk_sagemaker_edge.types.deployment_models

        out["deployment_models"] = (
            aws_sdk_sagemaker_edge.types.deployment_models.deserialize_json(
                data["DeploymentModels"]
            )
        )
    return out
