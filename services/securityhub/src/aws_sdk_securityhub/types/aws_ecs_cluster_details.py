"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_cluster_cluster_settings_list
    import aws_sdk_securityhub.types.aws_ecs_cluster_configuration_details
    import aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsEcsClusterDetails(TypedDict):
    cluster_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the cluster. </p>"""
    active_services_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    r"""<p>The number of services that are running on the cluster in an <code>ACTIVE</code> state. You can view these services with the Amazon ECS <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html\"> <code>ListServices</code> </a> API operation. </p>"""
    capacity_providers: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The short name of one or more capacity providers to associate with the cluster.</p>"""
    cluster_settings: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_cluster_cluster_settings_list.AwsEcsClusterClusterSettingsList"
    ]
    """<p>The setting to use to create the cluster. Specifically used to configure whether to enable CloudWatch Container Insights for the cluster.</p>"""
    configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_cluster_configuration_details.AwsEcsClusterConfigurationDetails"
    ]
    """<p>The run command configuration for the cluster.</p>"""
    default_capacity_provider_strategy: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list.AwsEcsClusterDefaultCapacityProviderStrategyList"
    ]
    """<p>The default capacity provider strategy for the cluster. The default capacity provider strategy is used when services or tasks are run without a specified launch type or capacity provider strategy.</p>"""
    cluster_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A name that you use to identify your cluster. </p>"""
    registered_container_instances_count: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>The number of container instances registered into the cluster. This includes container instances in both <code>ACTIVE</code> and <code>DRAINING</code> status. </p>"""
    running_tasks_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of tasks in the cluster that are in the <code>RUNNING</code> state. </p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the cluster. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsClusterDetails) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "active_services_count" in value:
        out["ActiveServicesCount"] = value["active_services_count"]
    if "capacity_providers" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["CapacityProviders"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["capacity_providers"]
            )
        )
    if "cluster_settings" in value:
        import aws_sdk_securityhub.types.aws_ecs_cluster_cluster_settings_list

        out["ClusterSettings"] = (
            aws_sdk_securityhub.types.aws_ecs_cluster_cluster_settings_list.serialize_json(
                value["cluster_settings"]
            )
        )
    if "configuration" in value:
        import aws_sdk_securityhub.types.aws_ecs_cluster_configuration_details

        out["Configuration"] = (
            aws_sdk_securityhub.types.aws_ecs_cluster_configuration_details.serialize_json(
                value["configuration"]
            )
        )
    if "default_capacity_provider_strategy" in value:
        import aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list

        out["DefaultCapacityProviderStrategy"] = (
            aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list.serialize_json(
                value["default_capacity_provider_strategy"]
            )
        )
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "registered_container_instances_count" in value:
        out["RegisteredContainerInstancesCount"] = value[
            "registered_container_instances_count"
        ]
    if "running_tasks_count" in value:
        out["RunningTasksCount"] = value["running_tasks_count"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsEcsClusterDetails:
    out: AwsEcsClusterDetails = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "ActiveServicesCount" in data:
        out["active_services_count"] = data["ActiveServicesCount"]
    if "CapacityProviders" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["capacity_providers"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["CapacityProviders"]
            )
        )
    if "ClusterSettings" in data:
        import aws_sdk_securityhub.types.aws_ecs_cluster_cluster_settings_list

        out["cluster_settings"] = (
            aws_sdk_securityhub.types.aws_ecs_cluster_cluster_settings_list.deserialize_json(
                data["ClusterSettings"]
            )
        )
    if "Configuration" in data:
        import aws_sdk_securityhub.types.aws_ecs_cluster_configuration_details

        out["configuration"] = (
            aws_sdk_securityhub.types.aws_ecs_cluster_configuration_details.deserialize_json(
                data["Configuration"]
            )
        )
    if "DefaultCapacityProviderStrategy" in data:
        import aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list

        out["default_capacity_provider_strategy"] = (
            aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list.deserialize_json(
                data["DefaultCapacityProviderStrategy"]
            )
        )
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "RegisteredContainerInstancesCount" in data:
        out["registered_container_instances_count"] = data[
            "RegisteredContainerInstancesCount"
        ]
    if "RunningTasksCount" in data:
        out["running_tasks_count"] = data["RunningTasksCount"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
