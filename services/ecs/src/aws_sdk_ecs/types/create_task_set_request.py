"""Generated from Smithy shape ``com.amazonaws.ecs#CreateTaskSetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_provider_strategy
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.load_balancers
    import aws_sdk_ecs.types.network_configuration
    import aws_sdk_ecs.types.scale
    import aws_sdk_ecs.types.service_registries
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags


class CreateTaskSetRequest(TypedDict):
    service: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</p>"""
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</p>"""
    external_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the <code>ECS_TASK_SET_EXTERNAL_ID</code> Cloud Map attribute set to the provided value.</p>"""
    task_definition: "aws_sdk_ecs.types.string.String"
    """<p>The task definition for the tasks in the task set to use. If a revision isn't specified, the latest <code>ACTIVE</code> revision is used.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>An object representing the network configuration for a task set.</p>"""
    load_balancers: NotRequired["aws_sdk_ecs.types.load_balancers.LoadBalancers"]
    """<p>A load balancer object representing the load balancer to use with the task set. The supported load balancer types are either an Application Load Balancer or a Network Load Balancer.</p>"""
    service_registries: NotRequired[
        "aws_sdk_ecs.types.service_registries.ServiceRegistries"
    ]
    """<p>The details of the service discovery registries to assign to this task set. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html\">Service discovery</a>.</p>"""
    launch_type: NotRequired["aws_sdk_ecs.types.launch_type.LaunchType"]
    """<p>The launch type that new tasks in the task set uses. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html\">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p>"""
    capacity_provider_strategy: NotRequired[
        "aws_sdk_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy to use for the task set.</p> <p>A capacity provider strategy consists of one or more capacity providers along with the <code>base</code> and <code>weight</code> to assign to them. A capacity provider must be associated with the cluster to be used in a capacity provider strategy. The <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html\">PutClusterCapacityProviders</a> API is used to associate a capacity provider with a cluster. Only capacity providers with an <code>ACTIVE</code> or <code>UPDATING</code> status can be used.</p> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProviderProvider.html\">CreateCapacityProviderProvider</a>API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p> <p>The <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html\">PutClusterCapacityProviders</a> API operation is used to update the list of available capacity providers for a cluster after the cluster is created.</p>"""
    platform_version: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The platform version that the tasks in the task set uses. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the <code>LATEST</code> platform version is used.</p>"""
    scale: NotRequired["aws_sdk_ecs.types.scale.Scale"]
    """<p>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</p>"""
    client_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both. When a service is deleted, the tags are deleted.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
