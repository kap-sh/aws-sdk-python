"""Generated from Smithy shape ``com.amazonaws.ecs#Service``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.availability_zone_rebalancing
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.capacity_provider_strategy
    import aws_sdk_ecs.types.deployment_configuration
    import aws_sdk_ecs.types.deployment_controller
    import aws_sdk_ecs.types.deployments
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.load_balancers
    import aws_sdk_ecs.types.network_configuration
    import aws_sdk_ecs.types.placement_constraints
    import aws_sdk_ecs.types.placement_strategies
    import aws_sdk_ecs.types.propagate_tags
    import aws_sdk_ecs.types.resource_management_type
    import aws_sdk_ecs.types.scheduling_strategy
    import aws_sdk_ecs.types.service_current_revision_summary_list
    import aws_sdk_ecs.types.service_events
    import aws_sdk_ecs.types.service_registries
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.task_sets
    import aws_sdk_ecs.types.timestamp


class Service(TypedDict):
    service_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN that identifies the service. For more information about the ARN format, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids\">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    service_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster. However, you can have similarly named services in multiple clusters within a Region or across multiple Regions.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that hosts the service.</p>"""
    load_balancers: NotRequired["aws_sdk_ecs.types.load_balancers.LoadBalancers"]
    """<p>A list of Elastic Load Balancing load balancer objects. It contains the load balancer name, the container name, and the container port to access from the load balancer. The container name is as it appears in a container definition.</p>"""
    service_registries: NotRequired[
        "aws_sdk_ecs.types.service_registries.ServiceRegistries"
    ]
    """<p>The details for the service discovery registries to assign to this service. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html\">Service Discovery</a>.</p>"""
    status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The status of the service. The valid values are <code>ACTIVE</code>, <code>DRAINING</code>, or <code>INACTIVE</code>.</p>"""
    desired_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html\">CreateService</a> , and it can be modified with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html\">UpdateService</a>.</p>"""
    running_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of tasks in the cluster that are in the <code>RUNNING</code> state.</p>"""
    pending_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of tasks in the cluster that are in the <code>PENDING</code> state.</p>"""
    launch_type: NotRequired["aws_sdk_ecs.types.launch_type.LaunchType"]
    """<p>The launch type the service is using. When using the DescribeServices API, this field is omitted if the service was created using a capacity provider strategy.</p>"""
    capacity_provider_strategy: NotRequired[
        "aws_sdk_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy the service uses. When using the DescribeServices API, this field is omitted if the service was created using a launch type.</p>"""
    platform_version: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The platform version to run your service on. A platform version is only specified for tasks that are hosted on Fargate. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html\">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    platform_family: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The operating system that your tasks in the service run on. A platform family is specified only for tasks using the Fargate launch type. </p> <p> All tasks that run as part of this service must use the same <code>platformFamily</code> value as the service (for example, <code>LINUX</code>).</p>"""
    task_definition: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The task definition to use for tasks in the service. This value is specified when the service is created with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html\">CreateService</a>, and it can be modified with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html\">UpdateService</a>.</p>"""
    deployment_configuration: NotRequired[
        "aws_sdk_ecs.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</p>"""
    task_sets: NotRequired["aws_sdk_ecs.types.task_sets.TaskSets"]
    """<p>Information about a set of Amazon ECS tasks in either an CodeDeploy or an <code>EXTERNAL</code> deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.</p>"""
    deployments: NotRequired["aws_sdk_ecs.types.deployments.Deployments"]
    """<p>The current state of deployments for the service.</p>"""
    role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the IAM role that's associated with the service. It allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.</p>"""
    events: NotRequired["aws_sdk_ecs.types.service_events.ServiceEvents"]
    """<p>The event stream for your service. A maximum of 100 of the latest events are displayed.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the service was created.</p>"""
    current_service_deployment: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the current service deployment.</p>"""
    current_service_revisions: NotRequired[
        "aws_sdk_ecs.types.service_current_revision_summary_list.ServiceCurrentRevisionSummaryList"
    ]
    """<p>The list of the service revisions.</p>"""
    placement_constraints: NotRequired[
        "aws_sdk_ecs.types.placement_constraints.PlacementConstraints"
    ]
    """<p>The placement constraints for the tasks in the service.</p>"""
    placement_strategy: NotRequired[
        "aws_sdk_ecs.types.placement_strategies.PlacementStrategies"
    ]
    """<p>The placement strategy that determines how tasks for the service are placed.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the <code>awsvpc</code> networking mode.</p>"""
    health_check_grace_period_seconds: NotRequired[
        "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started.</p> <p>If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.</p>"""
    scheduling_strategy: NotRequired[
        "aws_sdk_ecs.types.scheduling_strategy.SchedulingStrategy"
    ]
    """<p>The scheduling strategy to use for the service. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html\">Services</a>.</p> <p>There are two service scheduler strategies available.</p> <ul> <li> <p> <code>REPLICA</code>-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions.</p> </li> <li> <p> <code>DAEMON</code>-The daemon scheduling strategy deploys exactly one task on each active container instance. This task meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks. It stop tasks that don't meet the placement constraints.</p> <note> <p>Fargate tasks don't support the <code>DAEMON</code> scheduling strategy.</p> </note> </li> </ul>"""
    deployment_controller: NotRequired[
        "aws_sdk_ecs.types.deployment_controller.DeploymentController"
    ]
    """<p>The deployment controller type the service is using. </p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value. You define bot the key and value.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    created_by: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The principal that created the service.</p>"""
    enable_ecs_managed_tags: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to use Amazon ECS managed tags for the tasks in the service. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html\">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    propagate_tags: NotRequired["aws_sdk_ecs.types.propagate_tags.PropagateTags"]
    """<p>Determines whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.</p>"""
    enable_execute_command: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether the execute command functionality is turned on for the service. If <code>true</code>, the execute command functionality is turned on for all containers in tasks as part of the service.</p>"""
    availability_zone_rebalancing: NotRequired[
        "aws_sdk_ecs.types.availability_zone_rebalancing.AvailabilityZoneRebalancing"
    ]
    """<p>Indicates whether to use Availability Zone rebalancing for the service.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html\">Balancing an Amazon ECS service across Availability Zones</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <p>The default behavior of <code>AvailabilityZoneRebalancing</code> differs between create and update requests:</p> <ul> <li> <p>For create service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults the value to <code>ENABLED</code>.</p> </li> <li> <p>For update service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults to the existing service’s <code>AvailabilityZoneRebalancing</code> value. If the service never had an <code>AvailabilityZoneRebalancing</code> value set, Amazon ECS treats this as <code>DISABLED</code>.</p> </li> </ul>"""
    resource_management_type: NotRequired[
        "aws_sdk_ecs.types.resource_management_type.ResourceManagementType"
    ]
    """<p>Identifies whether an ECS Service is an Express Service managed by ECS, or managed by the customer. The valid values are <code>ECS</code> and <code>CUSTOMER</code> </p>"""
