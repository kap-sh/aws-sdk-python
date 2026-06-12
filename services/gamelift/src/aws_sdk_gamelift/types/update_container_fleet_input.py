"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateContainerFleetInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.connection_port_range
    import aws_sdk_gamelift.types.container_fleet_remove_attribute_list
    import aws_sdk_gamelift.types.container_group_definition_name_or_arn
    import aws_sdk_gamelift.types.deployment_configuration
    import aws_sdk_gamelift.types.fleet_id_or_arn
    import aws_sdk_gamelift.types.game_server_container_groups_per_instance
    import aws_sdk_gamelift.types.game_session_creation_limit_policy
    import aws_sdk_gamelift.types.ip_permissions_list
    import aws_sdk_gamelift.types.log_configuration
    import aws_sdk_gamelift.types.metric_group_list
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.protection_policy


class UpdateContainerFleetInput(TypedDict):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the container fleet to update. You can use either the fleet ID or ARN value.</p>"""
    game_server_container_group_definition_name: NotRequired[
        "aws_sdk_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>The name or ARN value of a new game server container group definition to deploy on the fleet. If you're updating the fleet to a specific version of a container group definition, use the ARN value and include the version number. If you're updating the fleet to the latest version of a container group definition, you can use the name value. You can't remove a fleet's game server container group definition, you can only update or replace it with another definition.</p> <p>Update a container group definition by calling <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html\">UpdateContainerGroupDefinition</a>. This operation creates a <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html\">ContainerGroupDefinition</a> resource with an incremented version. </p>"""
    per_instance_container_group_definition_name: NotRequired[
        "aws_sdk_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>The name or ARN value of a new per-instance container group definition to deploy on the fleet. If you're updating the fleet to a specific version of a container group definition, use the ARN value and include the version number. If you're updating the fleet to the latest version of a container group definition, you can use the name value.</p> <p>Update a container group definition by calling <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html\">UpdateContainerGroupDefinition</a>. This operation creates a <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html\">ContainerGroupDefinition</a> resource with an incremented version. </p> <p>To remove a fleet's per-instance container group definition, leave this parameter empty and use the parameter <code>RemoveAttributes</code>.</p>"""
    game_server_container_groups_per_instance: NotRequired[
        "aws_sdk_gamelift.types.game_server_container_groups_per_instance.GameServerContainerGroupsPerInstance"
    ]
    """<p>The number of times to replicate the game server container group on each fleet instance. By default, Amazon GameLift Servers calculates the maximum number of game server container groups that can fit on each instance. You can remove this property value to use the calculated value, or set it manually. If you set this number manually, Amazon GameLift Servers uses your value as long as it's less than the calculated maximum.</p>"""
    instance_connection_port_range: NotRequired[
        "aws_sdk_gamelift.types.connection_port_range.ConnectionPortRange"
    ]
    """<p>A revised set of port numbers to open on each fleet instance. By default, Amazon GameLift Servers calculates an optimal port range based on your fleet configuration. If you previously set this parameter manually, you can't reset this to use the calculated settings.</p> <p>The port range must not overlap with the Amazon GameLift Servers reserved port range <code>4092-4191</code>. This range is reserved for internal Amazon GameLift Servers services.</p>"""
    instance_inbound_permission_authorizations: NotRequired[
        "aws_sdk_gamelift.types.ip_permissions_list.IpPermissionsList"
    ]
    """<p>A set of ports to add to the container fleet's inbound permissions.</p> <p>The port range must not overlap with the Amazon GameLift Servers reserved port range <code>4092-4191</code>. This range is reserved for internal Amazon GameLift Servers services.</p>"""
    instance_inbound_permission_revocations: NotRequired[
        "aws_sdk_gamelift.types.ip_permissions_list.IpPermissionsList"
    ]
    """<p>A set of ports to remove from the container fleet's inbound permissions.</p>"""
    deployment_configuration: NotRequired[
        "aws_sdk_gamelift.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>Instructions for how to deploy updates to a container fleet, if the fleet update initiates a deployment. The deployment configuration lets you determine how to replace fleet instances and what actions to take if the deployment fails.</p>"""
    description: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A meaningful description of the container fleet.</p>"""
    metric_groups: NotRequired[
        "aws_sdk_gamelift.types.metric_group_list.MetricGroupList"
    ]
    """<p>The name of an Amazon Web Services CloudWatch metric group to add this fleet to. </p>"""
    new_game_session_protection_policy: NotRequired[
        "aws_sdk_gamelift.types.protection_policy.ProtectionPolicy"
    ]
    """<p>The game session protection policy to apply to all new game sessions that are started in this fleet. Game sessions that already exist are not affected. </p>"""
    game_session_creation_limit_policy: NotRequired[
        "aws_sdk_gamelift.types.game_session_creation_limit_policy.GameSessionCreationLimitPolicy"
    ]
    """<p>A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_gamelift.types.log_configuration.LogConfiguration"
    ]
    """<p>The method for collecting container logs for the fleet. </p>"""
    remove_attributes: NotRequired[
        "aws_sdk_gamelift.types.container_fleet_remove_attribute_list.ContainerFleetRemoveAttributeList"
    ]
    """<p>If set, this update removes a fleet's per-instance container group definition. You can't remove a fleet's game server container group definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContainerFleetInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "game_server_container_group_definition_name" in value:
        out["GameServerContainerGroupDefinitionName"] = value[
            "game_server_container_group_definition_name"
        ]
    if "per_instance_container_group_definition_name" in value:
        out["PerInstanceContainerGroupDefinitionName"] = value[
            "per_instance_container_group_definition_name"
        ]
    if "game_server_container_groups_per_instance" in value:
        out["GameServerContainerGroupsPerInstance"] = value[
            "game_server_container_groups_per_instance"
        ]
    if "instance_connection_port_range" in value:
        import aws_sdk_gamelift.types.connection_port_range

        out["InstanceConnectionPortRange"] = (
            aws_sdk_gamelift.types.connection_port_range.serialize_aws_json_1_1(
                value["instance_connection_port_range"]
            )
        )
    if "instance_inbound_permission_authorizations" in value:
        import aws_sdk_gamelift.types.ip_permissions_list

        out["InstanceInboundPermissionAuthorizations"] = (
            aws_sdk_gamelift.types.ip_permissions_list.serialize_aws_json_1_1(
                value["instance_inbound_permission_authorizations"]
            )
        )
    if "instance_inbound_permission_revocations" in value:
        import aws_sdk_gamelift.types.ip_permissions_list

        out["InstanceInboundPermissionRevocations"] = (
            aws_sdk_gamelift.types.ip_permissions_list.serialize_aws_json_1_1(
                value["instance_inbound_permission_revocations"]
            )
        )
    if "deployment_configuration" in value:
        import aws_sdk_gamelift.types.deployment_configuration

        out["DeploymentConfiguration"] = (
            aws_sdk_gamelift.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "metric_groups" in value:
        import aws_sdk_gamelift.types.metric_group_list

        out["MetricGroups"] = (
            aws_sdk_gamelift.types.metric_group_list.serialize_aws_json_1_1(
                value["metric_groups"]
            )
        )
    if "new_game_session_protection_policy" in value:
        import aws_sdk_gamelift.types.protection_policy

        out["NewGameSessionProtectionPolicy"] = (
            aws_sdk_gamelift.types.protection_policy.serialize_aws_json_1_1(
                value["new_game_session_protection_policy"]
            )
        )
    if "game_session_creation_limit_policy" in value:
        import aws_sdk_gamelift.types.game_session_creation_limit_policy

        out["GameSessionCreationLimitPolicy"] = (
            aws_sdk_gamelift.types.game_session_creation_limit_policy.serialize_aws_json_1_1(
                value["game_session_creation_limit_policy"]
            )
        )
    if "log_configuration" in value:
        import aws_sdk_gamelift.types.log_configuration

        out["LogConfiguration"] = (
            aws_sdk_gamelift.types.log_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    if "remove_attributes" in value:
        import aws_sdk_gamelift.types.container_fleet_remove_attribute_list

        out["RemoveAttributes"] = (
            aws_sdk_gamelift.types.container_fleet_remove_attribute_list.serialize_aws_json_1_1(
                value["remove_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContainerFleetInput:
    out: UpdateContainerFleetInput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "GameServerContainerGroupDefinitionName" in data:
        out["game_server_container_group_definition_name"] = data[
            "GameServerContainerGroupDefinitionName"
        ]
    if "PerInstanceContainerGroupDefinitionName" in data:
        out["per_instance_container_group_definition_name"] = data[
            "PerInstanceContainerGroupDefinitionName"
        ]
    if "GameServerContainerGroupsPerInstance" in data:
        out["game_server_container_groups_per_instance"] = data[
            "GameServerContainerGroupsPerInstance"
        ]
    if "InstanceConnectionPortRange" in data:
        import aws_sdk_gamelift.types.connection_port_range

        out["instance_connection_port_range"] = (
            aws_sdk_gamelift.types.connection_port_range.deserialize_aws_json_1_1(
                data["InstanceConnectionPortRange"]
            )
        )
    if "InstanceInboundPermissionAuthorizations" in data:
        import aws_sdk_gamelift.types.ip_permissions_list

        out["instance_inbound_permission_authorizations"] = (
            aws_sdk_gamelift.types.ip_permissions_list.deserialize_aws_json_1_1(
                data["InstanceInboundPermissionAuthorizations"]
            )
        )
    if "InstanceInboundPermissionRevocations" in data:
        import aws_sdk_gamelift.types.ip_permissions_list

        out["instance_inbound_permission_revocations"] = (
            aws_sdk_gamelift.types.ip_permissions_list.deserialize_aws_json_1_1(
                data["InstanceInboundPermissionRevocations"]
            )
        )
    if "DeploymentConfiguration" in data:
        import aws_sdk_gamelift.types.deployment_configuration

        out["deployment_configuration"] = (
            aws_sdk_gamelift.types.deployment_configuration.deserialize_aws_json_1_1(
                data["DeploymentConfiguration"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "MetricGroups" in data:
        import aws_sdk_gamelift.types.metric_group_list

        out["metric_groups"] = (
            aws_sdk_gamelift.types.metric_group_list.deserialize_aws_json_1_1(
                data["MetricGroups"]
            )
        )
    if "NewGameSessionProtectionPolicy" in data:
        import aws_sdk_gamelift.types.protection_policy

        out["new_game_session_protection_policy"] = (
            aws_sdk_gamelift.types.protection_policy.deserialize_aws_json_1_1(
                data["NewGameSessionProtectionPolicy"]
            )
        )
    if "GameSessionCreationLimitPolicy" in data:
        import aws_sdk_gamelift.types.game_session_creation_limit_policy

        out["game_session_creation_limit_policy"] = (
            aws_sdk_gamelift.types.game_session_creation_limit_policy.deserialize_aws_json_1_1(
                data["GameSessionCreationLimitPolicy"]
            )
        )
    if "LogConfiguration" in data:
        import aws_sdk_gamelift.types.log_configuration

        out["log_configuration"] = (
            aws_sdk_gamelift.types.log_configuration.deserialize_aws_json_1_1(
                data["LogConfiguration"]
            )
        )
    if "RemoveAttributes" in data:
        import aws_sdk_gamelift.types.container_fleet_remove_attribute_list

        out["remove_attributes"] = (
            aws_sdk_gamelift.types.container_fleet_remove_attribute_list.deserialize_aws_json_1_1(
                data["RemoveAttributes"]
            )
        )
    return out
