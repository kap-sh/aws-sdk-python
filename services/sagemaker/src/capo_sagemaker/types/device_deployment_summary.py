"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceDeploymentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.device_arn
    import capo_sagemaker.types.device_deployment_status
    import capo_sagemaker.types.device_description
    import capo_sagemaker.types.device_name
    import capo_sagemaker.types.edge_deployment_plan_arn
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.string
    import capo_sagemaker.types.timestamp


class DeviceDeploymentSummary(TypedDict, closed=True):
    edge_deployment_plan_arn: NotRequired[
        "capo_sagemaker.types.edge_deployment_plan_arn.EdgeDeploymentPlanArn"
    ]
    """<p>The ARN of the edge deployment plan.</p>"""
    edge_deployment_plan_name: NotRequired[
        "capo_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan.</p>"""
    stage_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the stage in the edge deployment plan.</p>"""
    deployed_stage_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the deployed stage.</p>"""
    device_fleet_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet to which the device belongs to.</p>"""
    device_name: NotRequired["capo_sagemaker.types.device_name.DeviceName"]
    """<p>The name of the device.</p>"""
    device_arn: NotRequired["capo_sagemaker.types.device_arn.DeviceArn"]
    """<p>The ARN of the device.</p>"""
    device_deployment_status: NotRequired[
        "capo_sagemaker.types.device_deployment_status.DeviceDeploymentStatus"
    ]
    """<p>The deployment status of the device.</p>"""
    device_deployment_status_message: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The detailed error message for the deployoment status result.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.device_description.DeviceDescription"
    ]
    """<p>The description of the device.</p>"""
    deployment_start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the deployment on the device started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceDeploymentSummary) -> dict:
    out: dict = {}
    if "edge_deployment_plan_arn" in value:
        out["EdgeDeploymentPlanArn"] = value["edge_deployment_plan_arn"]
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    if "deployed_stage_name" in value:
        out["DeployedStageName"] = value["deployed_stage_name"]
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "device_arn" in value:
        out["DeviceArn"] = value["device_arn"]
    if "device_deployment_status" in value:
        import capo_sagemaker.types.device_deployment_status

        out["DeviceDeploymentStatus"] = (
            capo_sagemaker.types.device_deployment_status.serialize_aws_json_1_1(
                value["device_deployment_status"]
            )
        )
    if "device_deployment_status_message" in value:
        out["DeviceDeploymentStatusMessage"] = value["device_deployment_status_message"]
    if "description" in value:
        out["Description"] = value["description"]
    if "deployment_start_time" in value:
        import capo_sagemaker.types.timestamp

        out["DeploymentStartTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["deployment_start_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceDeploymentSummary:
    out: DeviceDeploymentSummary = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanArn" in data:
        out["edge_deployment_plan_arn"] = data["EdgeDeploymentPlanArn"]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if "StageName" in data:
        out["stage_name"] = data["StageName"]
    if "DeployedStageName" in data:
        out["deployed_stage_name"] = data["DeployedStageName"]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "DeviceArn" in data:
        out["device_arn"] = data["DeviceArn"]
    if "DeviceDeploymentStatus" in data:
        import capo_sagemaker.types.device_deployment_status

        out["device_deployment_status"] = (
            capo_sagemaker.types.device_deployment_status.deserialize_aws_json_1_1(
                data["DeviceDeploymentStatus"]
            )
        )
    if "DeviceDeploymentStatusMessage" in data:
        out["device_deployment_status_message"] = data["DeviceDeploymentStatusMessage"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DeploymentStartTime" in data:
        import capo_sagemaker.types.timestamp

        out["deployment_start_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["DeploymentStartTime"]
            )
        )
    return out
