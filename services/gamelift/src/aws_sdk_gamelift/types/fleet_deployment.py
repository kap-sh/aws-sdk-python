"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.deployment_configuration
    import aws_sdk_gamelift.types.deployment_id
    import aws_sdk_gamelift.types.deployment_status
    import aws_sdk_gamelift.types.fleet_binary_arn
    import aws_sdk_gamelift.types.fleet_id
    import aws_sdk_gamelift.types.timestamp


class FleetDeployment(TypedDict, closed=True):
    deployment_id: NotRequired["aws_sdk_gamelift.types.deployment_id.DeploymentId"]
    """<p>A unique identifier for the deployment. </p>"""
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the container fleet. </p>"""
    game_server_binary_arn: NotRequired[
        "aws_sdk_gamelift.types.fleet_binary_arn.FleetBinaryArn"
    ]
    """<p>The unique identifier for the version of the game server container group definition that is being deployed.</p>"""
    rollback_game_server_binary_arn: NotRequired[
        "aws_sdk_gamelift.types.fleet_binary_arn.FleetBinaryArn"
    ]
    """<p>The unique identifier for the version of the game server container group definition to roll back to if deployment fails. Amazon GameLift Servers sets this property to the container group definition version that the fleet used when it was last active.</p>"""
    per_instance_binary_arn: NotRequired[
        "aws_sdk_gamelift.types.fleet_binary_arn.FleetBinaryArn"
    ]
    """<p>The unique identifier for the version of the per-instance container group definition that is being deployed. </p>"""
    rollback_per_instance_binary_arn: NotRequired[
        "aws_sdk_gamelift.types.fleet_binary_arn.FleetBinaryArn"
    ]
    """<p>The unique identifier for the version of the per-instance container group definition to roll back to if deployment fails. Amazon GameLift Servers sets this property to the container group definition version that the fleet used when it was last active.</p>"""
    deployment_status: NotRequired[
        "aws_sdk_gamelift.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of fleet deployment activity in the location. </p> <ul> <li> <p> <code>IN_PROGRESS</code> -- The deployment is in progress.</p> </li> <li> <p> <code>IMPAIRED</code> -- The deployment failed and the fleet has some impaired containers. </p> </li> <li> <p> <code>COMPLETE</code> -- The deployment has completed successfully.</p> </li> <li> <p> <code>ROLLBACK_IN_PROGRESS</code> -- The deployment failed and rollback has been initiated.</p> </li> <li> <p> <code>ROLLBACK_IN_COMPLETE</code> -- The deployment failed and rollback has been completed.</p> </li> <li> <p> <code>CANCELLED</code> -- The deployment was cancelled.</p> </li> </ul>"""
    deployment_configuration: NotRequired[
        "aws_sdk_gamelift.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>Instructions for how to deploy updates to a container fleet and what actions to take if the deployment fails.</p>"""
    creation_time: NotRequired["aws_sdk_gamelift.types.timestamp.Timestamp"]
    r"""<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>\"1469498468.057\"</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetDeployment) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "game_server_binary_arn" in value:
        out["GameServerBinaryArn"] = value["game_server_binary_arn"]
    if "rollback_game_server_binary_arn" in value:
        out["RollbackGameServerBinaryArn"] = value["rollback_game_server_binary_arn"]
    if "per_instance_binary_arn" in value:
        out["PerInstanceBinaryArn"] = value["per_instance_binary_arn"]
    if "rollback_per_instance_binary_arn" in value:
        out["RollbackPerInstanceBinaryArn"] = value["rollback_per_instance_binary_arn"]
    if "deployment_status" in value:
        import aws_sdk_gamelift.types.deployment_status

        out["DeploymentStatus"] = (
            aws_sdk_gamelift.types.deployment_status.serialize_aws_json_1_1(
                value["deployment_status"]
            )
        )
    if "deployment_configuration" in value:
        import aws_sdk_gamelift.types.deployment_configuration

        out["DeploymentConfiguration"] = (
            aws_sdk_gamelift.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_gamelift.types.timestamp

        out["CreationTime"] = aws_sdk_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetDeployment:
    out: FleetDeployment = {}  # type: ignore[typeddict-item]
    if "DeploymentId" in data:
        out["deployment_id"] = data["DeploymentId"]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "GameServerBinaryArn" in data:
        out["game_server_binary_arn"] = data["GameServerBinaryArn"]
    if "RollbackGameServerBinaryArn" in data:
        out["rollback_game_server_binary_arn"] = data["RollbackGameServerBinaryArn"]
    if "PerInstanceBinaryArn" in data:
        out["per_instance_binary_arn"] = data["PerInstanceBinaryArn"]
    if "RollbackPerInstanceBinaryArn" in data:
        out["rollback_per_instance_binary_arn"] = data["RollbackPerInstanceBinaryArn"]
    if "DeploymentStatus" in data:
        import aws_sdk_gamelift.types.deployment_status

        out["deployment_status"] = (
            aws_sdk_gamelift.types.deployment_status.deserialize_aws_json_1_1(
                data["DeploymentStatus"]
            )
        )
    if "DeploymentConfiguration" in data:
        import aws_sdk_gamelift.types.deployment_configuration

        out["deployment_configuration"] = (
            aws_sdk_gamelift.types.deployment_configuration.deserialize_aws_json_1_1(
                data["DeploymentConfiguration"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_gamelift.types.timestamp

        out["creation_time"] = (
            aws_sdk_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
