"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_service_capacity_provider_strategy_list
    import capo_securityhub.types.aws_ecs_service_deployment_configuration_details
    import capo_securityhub.types.aws_ecs_service_deployment_controller_details
    import capo_securityhub.types.aws_ecs_service_load_balancers_list
    import capo_securityhub.types.aws_ecs_service_network_configuration_details
    import capo_securityhub.types.aws_ecs_service_placement_constraints_list
    import capo_securityhub.types.aws_ecs_service_placement_strategies_list
    import capo_securityhub.types.aws_ecs_service_service_registries_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsEcsServiceDetails(TypedDict, closed=True):
    capacity_provider_strategy: NotRequired[
        "capo_securityhub.types.aws_ecs_service_capacity_provider_strategy_list.AwsEcsServiceCapacityProviderStrategyList"
    ]
    """<p>The capacity provider strategy that the service uses.</p>"""
    cluster: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the cluster that hosts the service.</p>"""
    deployment_configuration: NotRequired[
        "capo_securityhub.types.aws_ecs_service_deployment_configuration_details.AwsEcsServiceDeploymentConfigurationDetails"
    ]
    """<p>Deployment parameters for the service. Includes the number of tasks that run and the order in which to start and stop tasks.</p>"""
    deployment_controller: NotRequired[
        "capo_securityhub.types.aws_ecs_service_deployment_controller_details.AwsEcsServiceDeploymentControllerDetails"
    ]
    """<p>Contains the deployment controller type that the service uses.</p>"""
    desired_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of instantiations of the task definition to run on the service.</p>"""
    enable_ecs_managed_tags: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether to enable Amazon ECS managed tags for the tasks in the service.</p>"""
    enable_execute_command: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the execute command functionality is enabled for the service.</p>"""
    health_check_grace_period_seconds: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>After a task starts, the amount of time in seconds that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks.</p>"""
    launch_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The launch type that the service uses.</p> <p>Valid values: <code>EC2</code> | <code>FARGATE</code> | <code>EXTERNAL</code> </p>"""
    load_balancers: NotRequired[
        "capo_securityhub.types.aws_ecs_service_load_balancers_list.AwsEcsServiceLoadBalancersList"
    ]
    """<p>Information about the load balancers that the service uses.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the service.</p>"""
    network_configuration: NotRequired[
        "capo_securityhub.types.aws_ecs_service_network_configuration_details.AwsEcsServiceNetworkConfigurationDetails"
    ]
    """<p>For tasks that use the <code>awsvpc</code> networking mode, the VPC subnet and security group configuration.</p>"""
    placement_constraints: NotRequired[
        "capo_securityhub.types.aws_ecs_service_placement_constraints_list.AwsEcsServicePlacementConstraintsList"
    ]
    """<p>The placement constraints for the tasks in the service.</p>"""
    placement_strategies: NotRequired[
        "capo_securityhub.types.aws_ecs_service_placement_strategies_list.AwsEcsServicePlacementStrategiesList"
    ]
    """<p>Information about how tasks for the service are placed.</p>"""
    platform_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The platform version on which to run the service. Only specified for tasks that are hosted on Fargate. If a platform version is not specified, the <code>LATEST</code> platform version is used by default.</p>"""
    propagate_tags: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates whether to propagate the tags from the task definition to the task or from the service to the task. If no value is provided, then tags are not propagated.</p> <p>Valid values: <code>TASK_DEFINITION</code> | <code>SERVICE</code> </p>"""
    role: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the IAM role that is associated with the service. The role allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.</p>"""
    scheduling_strategy: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The scheduling strategy to use for the service.</p> <p>The <code>REPLICA</code> scheduling strategy places and maintains the desired number of tasks across the cluster. By default, the service scheduler spreads tasks across Availability Zones. Task placement strategies and constraints are used to customize task placement decisions.</p> <p>The <code>DAEMON</code> scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that are specified in the cluster. The service scheduler also evaluates the task placement constraints for running tasks and stops tasks that don't meet the placement constraints.</p> <p>Valid values: <code>REPLICA</code> | <code>DAEMON</code> </p>"""
    service_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the service.</p>"""
    service_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the service.</p> <p>The name can contain up to 255 characters. It can use letters, numbers, underscores, and hyphens.</p>"""
    service_registries: NotRequired[
        "capo_securityhub.types.aws_ecs_service_service_registries_list.AwsEcsServiceServiceRegistriesList"
    ]
    """<p>Information about the service discovery registries to assign to the service.</p>"""
    task_definition: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The task definition to use for tasks in the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServiceDetails) -> dict:
    out: dict = {}
    if "capacity_provider_strategy" in value:
        import capo_securityhub.types.aws_ecs_service_capacity_provider_strategy_list

        out["CapacityProviderStrategy"] = (
            capo_securityhub.types.aws_ecs_service_capacity_provider_strategy_list.serialize_json(
                value["capacity_provider_strategy"]
            )
        )
    if "cluster" in value:
        out["Cluster"] = value["cluster"]
    if "deployment_configuration" in value:
        import capo_securityhub.types.aws_ecs_service_deployment_configuration_details

        out["DeploymentConfiguration"] = (
            capo_securityhub.types.aws_ecs_service_deployment_configuration_details.serialize_json(
                value["deployment_configuration"]
            )
        )
    if "deployment_controller" in value:
        import capo_securityhub.types.aws_ecs_service_deployment_controller_details

        out["DeploymentController"] = (
            capo_securityhub.types.aws_ecs_service_deployment_controller_details.serialize_json(
                value["deployment_controller"]
            )
        )
    if "desired_count" in value:
        out["DesiredCount"] = value["desired_count"]
    if "enable_ecs_managed_tags" in value:
        out["EnableEcsManagedTags"] = value["enable_ecs_managed_tags"]
    if "enable_execute_command" in value:
        out["EnableExecuteCommand"] = value["enable_execute_command"]
    if "health_check_grace_period_seconds" in value:
        out["HealthCheckGracePeriodSeconds"] = value[
            "health_check_grace_period_seconds"
        ]
    if "launch_type" in value:
        out["LaunchType"] = value["launch_type"]
    if "load_balancers" in value:
        import capo_securityhub.types.aws_ecs_service_load_balancers_list

        out["LoadBalancers"] = (
            capo_securityhub.types.aws_ecs_service_load_balancers_list.serialize_json(
                value["load_balancers"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "network_configuration" in value:
        import capo_securityhub.types.aws_ecs_service_network_configuration_details

        out["NetworkConfiguration"] = (
            capo_securityhub.types.aws_ecs_service_network_configuration_details.serialize_json(
                value["network_configuration"]
            )
        )
    if "placement_constraints" in value:
        import capo_securityhub.types.aws_ecs_service_placement_constraints_list

        out["PlacementConstraints"] = (
            capo_securityhub.types.aws_ecs_service_placement_constraints_list.serialize_json(
                value["placement_constraints"]
            )
        )
    if "placement_strategies" in value:
        import capo_securityhub.types.aws_ecs_service_placement_strategies_list

        out["PlacementStrategies"] = (
            capo_securityhub.types.aws_ecs_service_placement_strategies_list.serialize_json(
                value["placement_strategies"]
            )
        )
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "propagate_tags" in value:
        out["PropagateTags"] = value["propagate_tags"]
    if "role" in value:
        out["Role"] = value["role"]
    if "scheduling_strategy" in value:
        out["SchedulingStrategy"] = value["scheduling_strategy"]
    if "service_arn" in value:
        out["ServiceArn"] = value["service_arn"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "service_registries" in value:
        import capo_securityhub.types.aws_ecs_service_service_registries_list

        out["ServiceRegistries"] = (
            capo_securityhub.types.aws_ecs_service_service_registries_list.serialize_json(
                value["service_registries"]
            )
        )
    if "task_definition" in value:
        out["TaskDefinition"] = value["task_definition"]
    return out


def deserialize_json(data: dict) -> AwsEcsServiceDetails:
    out: AwsEcsServiceDetails = {}  # type: ignore[typeddict-item]
    if "CapacityProviderStrategy" in data:
        import capo_securityhub.types.aws_ecs_service_capacity_provider_strategy_list

        out["capacity_provider_strategy"] = (
            capo_securityhub.types.aws_ecs_service_capacity_provider_strategy_list.deserialize_json(
                data["CapacityProviderStrategy"]
            )
        )
    if "Cluster" in data:
        out["cluster"] = data["Cluster"]
    if "DeploymentConfiguration" in data:
        import capo_securityhub.types.aws_ecs_service_deployment_configuration_details

        out["deployment_configuration"] = (
            capo_securityhub.types.aws_ecs_service_deployment_configuration_details.deserialize_json(
                data["DeploymentConfiguration"]
            )
        )
    if "DeploymentController" in data:
        import capo_securityhub.types.aws_ecs_service_deployment_controller_details

        out["deployment_controller"] = (
            capo_securityhub.types.aws_ecs_service_deployment_controller_details.deserialize_json(
                data["DeploymentController"]
            )
        )
    if "DesiredCount" in data:
        out["desired_count"] = data["DesiredCount"]
    if "EnableEcsManagedTags" in data:
        out["enable_ecs_managed_tags"] = data["EnableEcsManagedTags"]
    if "EnableExecuteCommand" in data:
        out["enable_execute_command"] = data["EnableExecuteCommand"]
    if "HealthCheckGracePeriodSeconds" in data:
        out["health_check_grace_period_seconds"] = data["HealthCheckGracePeriodSeconds"]
    if "LaunchType" in data:
        out["launch_type"] = data["LaunchType"]
    if "LoadBalancers" in data:
        import capo_securityhub.types.aws_ecs_service_load_balancers_list

        out["load_balancers"] = (
            capo_securityhub.types.aws_ecs_service_load_balancers_list.deserialize_json(
                data["LoadBalancers"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "NetworkConfiguration" in data:
        import capo_securityhub.types.aws_ecs_service_network_configuration_details

        out["network_configuration"] = (
            capo_securityhub.types.aws_ecs_service_network_configuration_details.deserialize_json(
                data["NetworkConfiguration"]
            )
        )
    if "PlacementConstraints" in data:
        import capo_securityhub.types.aws_ecs_service_placement_constraints_list

        out["placement_constraints"] = (
            capo_securityhub.types.aws_ecs_service_placement_constraints_list.deserialize_json(
                data["PlacementConstraints"]
            )
        )
    if "PlacementStrategies" in data:
        import capo_securityhub.types.aws_ecs_service_placement_strategies_list

        out["placement_strategies"] = (
            capo_securityhub.types.aws_ecs_service_placement_strategies_list.deserialize_json(
                data["PlacementStrategies"]
            )
        )
    if "PlatformVersion" in data:
        out["platform_version"] = data["PlatformVersion"]
    if "PropagateTags" in data:
        out["propagate_tags"] = data["PropagateTags"]
    if "Role" in data:
        out["role"] = data["Role"]
    if "SchedulingStrategy" in data:
        out["scheduling_strategy"] = data["SchedulingStrategy"]
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    if "ServiceRegistries" in data:
        import capo_securityhub.types.aws_ecs_service_service_registries_list

        out["service_registries"] = (
            capo_securityhub.types.aws_ecs_service_service_registries_list.deserialize_json(
                data["ServiceRegistries"]
            )
        )
    if "TaskDefinition" in data:
        out["task_definition"] = data["TaskDefinition"]
    return out
