"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeDeploymentPlanSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_deployment_plan_arn
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.timestamp


class EdgeDeploymentPlanSummary(TypedDict):
    edge_deployment_plan_arn: NotRequired[
        "aws_sdk_sagemaker.types.edge_deployment_plan_arn.EdgeDeploymentPlanArn"
    ]
    """<p>The ARN of the edge deployment plan.</p>"""
    edge_deployment_plan_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan.</p>"""
    device_fleet_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the device fleet used for the deployment. </p>"""
    edge_deployment_success: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The number of edge devices with the successful deployment.</p>"""
    edge_deployment_pending: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The number of edge devices yet to pick up the deployment, or in progress.</p>"""
    edge_deployment_failed: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The number of edge devices that failed the deployment.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the edge deployment plan was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the edge deployment plan was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeDeploymentPlanSummary) -> dict:
    out: dict = {}
    if "edge_deployment_plan_arn" in value:
        out["EdgeDeploymentPlanArn"] = value["edge_deployment_plan_arn"]
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "edge_deployment_success" in value:
        out["EdgeDeploymentSuccess"] = value["edge_deployment_success"]
    if "edge_deployment_pending" in value:
        out["EdgeDeploymentPending"] = value["edge_deployment_pending"]
    if "edge_deployment_failed" in value:
        out["EdgeDeploymentFailed"] = value["edge_deployment_failed"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgeDeploymentPlanSummary:
    out: EdgeDeploymentPlanSummary = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanArn" in data:
        out["edge_deployment_plan_arn"] = data["EdgeDeploymentPlanArn"]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "EdgeDeploymentSuccess" in data:
        out["edge_deployment_success"] = data["EdgeDeploymentSuccess"]
    if "EdgeDeploymentPending" in data:
        out["edge_deployment_pending"] = data["EdgeDeploymentPending"]
    if "EdgeDeploymentFailed" in data:
        out["edge_deployment_failed"] = data["EdgeDeploymentFailed"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
