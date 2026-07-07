"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeDeploymentStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.stage_status
    import aws_sdk_sagemaker.types.string
    import aws_sdk_sagemaker.types.timestamp


class EdgeDeploymentStatus(TypedDict, closed=True):
    stage_status: NotRequired["aws_sdk_sagemaker.types.stage_status.StageStatus"]
    """<p>The general status of the current stage.</p>"""
    edge_deployment_success_in_stage: NotRequired[
        "aws_sdk_sagemaker.types.integer.Integer"
    ]
    """<p>The number of edge devices with the successful deployment in the current stage.</p>"""
    edge_deployment_pending_in_stage: NotRequired[
        "aws_sdk_sagemaker.types.integer.Integer"
    ]
    """<p>The number of edge devices yet to pick up the deployment in current stage, or in progress.</p>"""
    edge_deployment_failed_in_stage: NotRequired[
        "aws_sdk_sagemaker.types.integer.Integer"
    ]
    """<p>The number of edge devices that failed the deployment in current stage.</p>"""
    edge_deployment_status_message: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>A detailed message about deployment status in current stage.</p>"""
    edge_deployment_stage_start_time: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>The time when the deployment API started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeDeploymentStatus) -> dict:
    out: dict = {}
    if "stage_status" in value:
        import aws_sdk_sagemaker.types.stage_status

        out["StageStatus"] = (
            aws_sdk_sagemaker.types.stage_status.serialize_aws_json_1_1(
                value["stage_status"]
            )
        )
    if "edge_deployment_success_in_stage" in value:
        out["EdgeDeploymentSuccessInStage"] = value["edge_deployment_success_in_stage"]
    if "edge_deployment_pending_in_stage" in value:
        out["EdgeDeploymentPendingInStage"] = value["edge_deployment_pending_in_stage"]
    if "edge_deployment_failed_in_stage" in value:
        out["EdgeDeploymentFailedInStage"] = value["edge_deployment_failed_in_stage"]
    if "edge_deployment_status_message" in value:
        out["EdgeDeploymentStatusMessage"] = value["edge_deployment_status_message"]
    if "edge_deployment_stage_start_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EdgeDeploymentStageStartTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["edge_deployment_stage_start_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgeDeploymentStatus:
    out: EdgeDeploymentStatus = {}  # type: ignore[typeddict-item]
    if "StageStatus" in data:
        import aws_sdk_sagemaker.types.stage_status

        out["stage_status"] = (
            aws_sdk_sagemaker.types.stage_status.deserialize_aws_json_1_1(
                data["StageStatus"]
            )
        )
    if "EdgeDeploymentSuccessInStage" in data:
        out["edge_deployment_success_in_stage"] = data["EdgeDeploymentSuccessInStage"]
    if "EdgeDeploymentPendingInStage" in data:
        out["edge_deployment_pending_in_stage"] = data["EdgeDeploymentPendingInStage"]
    if "EdgeDeploymentFailedInStage" in data:
        out["edge_deployment_failed_in_stage"] = data["EdgeDeploymentFailedInStage"]
    if "EdgeDeploymentStatusMessage" in data:
        out["edge_deployment_status_message"] = data["EdgeDeploymentStatusMessage"]
    if "EdgeDeploymentStageStartTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["edge_deployment_stage_start_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["EdgeDeploymentStageStartTime"]
            )
        )
    return out
