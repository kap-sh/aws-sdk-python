"""Generated from Smithy shape ``com.amazonaws.ecs#Cluster``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attachments
    import aws_sdk_ecs.types.capacity_provider_strategy
    import aws_sdk_ecs.types.cluster_configuration
    import aws_sdk_ecs.types.cluster_service_connect_defaults
    import aws_sdk_ecs.types.cluster_settings
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.statistics
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.tags


class Cluster(TypedDict):
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the cluster. For more information about the ARN format, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids\">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    cluster_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>A user-generated string that you use to identify your cluster.</p>"""
    configuration: NotRequired[
        "aws_sdk_ecs.types.cluster_configuration.ClusterConfiguration"
    ]
    """<p>The execute command and managed storage configuration for the cluster.</p>"""
    status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The status of the cluster. The following are the possible states that are returned.</p> <dl> <dt>ACTIVE</dt> <dd> <p>The cluster is ready to accept tasks and if applicable you can register container instances with the cluster.</p> </dd> <dt>PROVISIONING</dt> <dd> <p>The cluster has capacity providers that are associated with it and the resources needed for the capacity provider are being created.</p> </dd> <dt>DEPROVISIONING</dt> <dd> <p>The cluster has capacity providers that are associated with it and the resources needed for the capacity provider are being deleted.</p> </dd> <dt>FAILED</dt> <dd> <p>The cluster has capacity providers that are associated with it and the resources needed for the capacity provider have failed to create.</p> </dd> <dt>INACTIVE</dt> <dd> <p>The cluster has been deleted. Clusters with an <code>INACTIVE</code> status may remain discoverable in your account for a period of time. However, this behavior is subject to change in the future. We don't recommend that you rely on <code>INACTIVE</code> clusters persisting.</p> </dd> </dl>"""
    registered_container_instances_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of container instances registered into the cluster. This includes container instances in both <code>ACTIVE</code> and <code>DRAINING</code> status.</p>"""
    running_tasks_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of tasks in the cluster that are in the <code>RUNNING</code> state.</p>"""
    pending_tasks_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of tasks in the cluster that are in the <code>PENDING</code> state.</p>"""
    active_services_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of services that are running on the cluster in an <code>ACTIVE</code> state. You can view these services with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html\">ListServices</a>.</p>"""
    statistics: NotRequired["aws_sdk_ecs.types.statistics.Statistics"]
    """<p>Additional information about your clusters that are separated by launch type. They include the following:</p> <ul> <li> <p>runningEC2TasksCount</p> </li> <li> <p>RunningFargateTasksCount</p> </li> <li> <p>pendingEC2TasksCount</p> </li> <li> <p>pendingFargateTasksCount</p> </li> <li> <p>activeEC2ServiceCount</p> </li> <li> <p>activeFargateServiceCount</p> </li> <li> <p>drainingEC2ServiceCount</p> </li> <li> <p>drainingFargateServiceCount</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    settings: NotRequired["aws_sdk_ecs.types.cluster_settings.ClusterSettings"]
    """<p>The settings for the cluster. This parameter indicates whether CloudWatch Container Insights is on or off for a cluster.</p>"""
    capacity_providers: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The capacity providers associated with the cluster.</p>"""
    default_capacity_provider_strategy: NotRequired[
        "aws_sdk_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The default capacity provider strategy for the cluster. When services or tasks are run in the cluster with no launch type or capacity provider strategy specified, the default capacity provider strategy is used.</p>"""
    attachments: NotRequired["aws_sdk_ecs.types.attachments.Attachments"]
    """<p>The resources attached to a cluster. When using a capacity provider with a cluster, the capacity provider and associated resources are returned as cluster attachments.</p>"""
    attachments_status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The status of the capacity providers associated with the cluster. The following are the states that are returned.</p> <dl> <dt>UPDATE_IN_PROGRESS</dt> <dd> <p>The available capacity providers for the cluster are updating.</p> </dd> <dt>UPDATE_COMPLETE</dt> <dd> <p>The capacity providers have successfully updated.</p> </dd> <dt>UPDATE_FAILED</dt> <dd> <p>The capacity provider updates failed.</p> </dd> </dl>"""
    service_connect_defaults: NotRequired[
        "aws_sdk_ecs.types.cluster_service_connect_defaults.ClusterServiceConnectDefaults"
    ]
    """<p>Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the <code>enabled</code> parameter to <code>true</code> in the <code>ServiceConnectConfiguration</code>. You can set the namespace of each service individually in the <code>ServiceConnectConfiguration</code> to override this default parameter.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html\">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
