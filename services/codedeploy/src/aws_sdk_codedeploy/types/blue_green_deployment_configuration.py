"""Generated from Smithy shape ``com.amazonaws.codedeploy#BlueGreenDeploymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.blue_instance_termination_option
    import aws_sdk_codedeploy.types.deployment_ready_option
    import aws_sdk_codedeploy.types.green_fleet_provisioning_option


class BlueGreenDeploymentConfiguration(TypedDict, closed=True):
    terminate_blue_instances_on_deployment_success: NotRequired[
        "aws_sdk_codedeploy.types.blue_instance_termination_option.BlueInstanceTerminationOption"
    ]
    """<p>Information about whether to terminate instances in the original fleet during a blue/green deployment.</p>"""
    deployment_ready_option: NotRequired[
        "aws_sdk_codedeploy.types.deployment_ready_option.DeploymentReadyOption"
    ]
    """<p>Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.</p>"""
    green_fleet_provisioning_option: NotRequired[
        "aws_sdk_codedeploy.types.green_fleet_provisioning_option.GreenFleetProvisioningOption"
    ]
    """<p>Information about how instances are provisioned for a replacement environment in a blue/green deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueGreenDeploymentConfiguration) -> dict:
    out: dict = {}
    if "terminate_blue_instances_on_deployment_success" in value:
        import aws_sdk_codedeploy.types.blue_instance_termination_option

        out["terminateBlueInstancesOnDeploymentSuccess"] = (
            aws_sdk_codedeploy.types.blue_instance_termination_option.serialize_aws_json_1_1(
                value["terminate_blue_instances_on_deployment_success"]
            )
        )
    if "deployment_ready_option" in value:
        import aws_sdk_codedeploy.types.deployment_ready_option

        out["deploymentReadyOption"] = (
            aws_sdk_codedeploy.types.deployment_ready_option.serialize_aws_json_1_1(
                value["deployment_ready_option"]
            )
        )
    if "green_fleet_provisioning_option" in value:
        import aws_sdk_codedeploy.types.green_fleet_provisioning_option

        out["greenFleetProvisioningOption"] = (
            aws_sdk_codedeploy.types.green_fleet_provisioning_option.serialize_aws_json_1_1(
                value["green_fleet_provisioning_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BlueGreenDeploymentConfiguration:
    out: BlueGreenDeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if "terminateBlueInstancesOnDeploymentSuccess" in data:
        import aws_sdk_codedeploy.types.blue_instance_termination_option

        out["terminate_blue_instances_on_deployment_success"] = (
            aws_sdk_codedeploy.types.blue_instance_termination_option.deserialize_aws_json_1_1(
                data["terminateBlueInstancesOnDeploymentSuccess"]
            )
        )
    if "deploymentReadyOption" in data:
        import aws_sdk_codedeploy.types.deployment_ready_option

        out["deployment_ready_option"] = (
            aws_sdk_codedeploy.types.deployment_ready_option.deserialize_aws_json_1_1(
                data["deploymentReadyOption"]
            )
        )
    if "greenFleetProvisioningOption" in data:
        import aws_sdk_codedeploy.types.green_fleet_provisioning_option

        out["green_fleet_provisioning_option"] = (
            aws_sdk_codedeploy.types.green_fleet_provisioning_option.deserialize_aws_json_1_1(
                data["greenFleetProvisioningOption"]
            )
        )
    return out
