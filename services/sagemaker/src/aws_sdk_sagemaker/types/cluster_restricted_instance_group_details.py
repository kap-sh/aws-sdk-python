"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterRestrictedInstanceGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_count
    import aws_sdk_sagemaker.types.cluster_instance_group_name
    import aws_sdk_sagemaker.types.cluster_instance_storage_configs
    import aws_sdk_sagemaker.types.cluster_instance_type
    import aws_sdk_sagemaker.types.cluster_non_negative_instance_count
    import aws_sdk_sagemaker.types.cluster_threads_per_core
    import aws_sdk_sagemaker.types.environment_config_details
    import aws_sdk_sagemaker.types.instance_group_status
    import aws_sdk_sagemaker.types.instance_group_training_plan_status
    import aws_sdk_sagemaker.types.on_start_deep_health_checks
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.scheduled_update_config
    import aws_sdk_sagemaker.types.training_plan_arn
    import aws_sdk_sagemaker.types.vpc_config


class ClusterRestrictedInstanceGroupDetails(TypedDict, closed=True):
    current_count: NotRequired[
        "aws_sdk_sagemaker.types.cluster_non_negative_instance_count.ClusterNonNegativeInstanceCount"
    ]
    """<p>The number of instances that are currently in the restricted instance group of a SageMaker HyperPod cluster.</p>"""
    target_count: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_count.ClusterInstanceCount"
    ]
    """<p>The number of instances you specified to add to the restricted instance group of a SageMaker HyperPod cluster.</p>"""
    instance_group_name: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>The name of the restricted instance group of a SageMaker HyperPod cluster.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_type.ClusterInstanceType"
    ]
    """<p>The instance type of the restricted instance group of a SageMaker HyperPod cluster.</p>"""
    execution_role: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The execution role for the restricted instance group to assume.</p>"""
    threads_per_core: NotRequired[
        "aws_sdk_sagemaker.types.cluster_threads_per_core.ClusterThreadsPerCore"
    ]
    r"""<p>The number you specified to <code>TreadsPerCore</code> in <code>CreateCluster</code> for enabling or disabling multithreading. For instance types that support multithreading, you can specify 1 for disabling multithreading and 2 for enabling multithreading. For more information, see the reference table of <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html\">CPU cores and threads per CPU core per instance type</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>"""
    instance_storage_configs: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_storage_configs.ClusterInstanceStorageConfigs"
    ]
    """<p>The additional storage configurations for the instances in the SageMaker HyperPod cluster restricted instance group.</p>"""
    on_start_deep_health_checks: NotRequired[
        "aws_sdk_sagemaker.types.on_start_deep_health_checks.OnStartDeepHealthChecks"
    ]
    """<p>A flag indicating whether deep health checks should be performed when the cluster's restricted instance group is created or updated.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.instance_group_status.InstanceGroupStatus"
    ]
    """<p>The current status of the cluster's restricted instance group.</p> <ul> <li> <p> <code>InService</code>: The restricted instance group is active and healthy.</p> </li> <li> <p> <code>Creating</code>: The restricted instance group is being provisioned.</p> </li> <li> <p> <code>Updating</code>: The restricted instance group is being updated.</p> </li> <li> <p> <code>Failed</code>: The restricted instance group has failed to provision or is no longer healthy.</p> </li> <li> <p> <code>Degraded</code>: The restricted instance group is degraded, meaning that some instances have failed to provision or are no longer healthy.</p> </li> <li> <p> <code>Deleting</code>: The restricted instance group is being deleted.</p> </li> </ul>"""
    training_plan_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the training plan to filter clusters by. For more information about reserving GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see <code> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html\">CreateTrainingPlan</a> </code>.</p>"""
    training_plan_status: NotRequired[
        "aws_sdk_sagemaker.types.instance_group_training_plan_status.InstanceGroupTrainingPlanStatus"
    ]
    """<p>The current status of the training plan associated with this cluster restricted instance group.</p>"""
    override_vpc_config: NotRequired["aws_sdk_sagemaker.types.vpc_config.VpcConfig"]
    scheduled_update_config: NotRequired[
        "aws_sdk_sagemaker.types.scheduled_update_config.ScheduledUpdateConfig"
    ]
    environment_config: NotRequired[
        "aws_sdk_sagemaker.types.environment_config_details.EnvironmentConfigDetails"
    ]
    """<p>The configuration for the restricted instance groups (RIG) environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterRestrictedInstanceGroupDetails) -> dict:
    out: dict = {}
    if "current_count" in value:
        out["CurrentCount"] = value["current_count"]
    if "target_count" in value:
        out["TargetCount"] = value["target_count"]
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.cluster_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.cluster_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "execution_role" in value:
        out["ExecutionRole"] = value["execution_role"]
    if "threads_per_core" in value:
        out["ThreadsPerCore"] = value["threads_per_core"]
    if "instance_storage_configs" in value:
        import aws_sdk_sagemaker.types.cluster_instance_storage_configs

        out["InstanceStorageConfigs"] = (
            aws_sdk_sagemaker.types.cluster_instance_storage_configs.serialize_aws_json_1_1(
                value["instance_storage_configs"]
            )
        )
    if "on_start_deep_health_checks" in value:
        import aws_sdk_sagemaker.types.on_start_deep_health_checks

        out["OnStartDeepHealthChecks"] = (
            aws_sdk_sagemaker.types.on_start_deep_health_checks.serialize_aws_json_1_1(
                value["on_start_deep_health_checks"]
            )
        )
    if "status" in value:
        import aws_sdk_sagemaker.types.instance_group_status

        out["Status"] = (
            aws_sdk_sagemaker.types.instance_group_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    if "training_plan_status" in value:
        out["TrainingPlanStatus"] = value["training_plan_status"]
    if "override_vpc_config" in value:
        import aws_sdk_sagemaker.types.vpc_config

        out["OverrideVpcConfig"] = (
            aws_sdk_sagemaker.types.vpc_config.serialize_aws_json_1_1(
                value["override_vpc_config"]
            )
        )
    if "scheduled_update_config" in value:
        import aws_sdk_sagemaker.types.scheduled_update_config

        out["ScheduledUpdateConfig"] = (
            aws_sdk_sagemaker.types.scheduled_update_config.serialize_aws_json_1_1(
                value["scheduled_update_config"]
            )
        )
    if "environment_config" in value:
        import aws_sdk_sagemaker.types.environment_config_details

        out["EnvironmentConfig"] = (
            aws_sdk_sagemaker.types.environment_config_details.serialize_aws_json_1_1(
                value["environment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterRestrictedInstanceGroupDetails:
    out: ClusterRestrictedInstanceGroupDetails = {}  # type: ignore[typeddict-item]
    if "CurrentCount" in data:
        out["current_count"] = data["CurrentCount"]
    if "TargetCount" in data:
        out["target_count"] = data["TargetCount"]
    if "InstanceGroupName" in data:
        out["instance_group_name"] = data["InstanceGroupName"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.cluster_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.cluster_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "ExecutionRole" in data:
        out["execution_role"] = data["ExecutionRole"]
    if "ThreadsPerCore" in data:
        out["threads_per_core"] = data["ThreadsPerCore"]
    if "InstanceStorageConfigs" in data:
        import aws_sdk_sagemaker.types.cluster_instance_storage_configs

        out["instance_storage_configs"] = (
            aws_sdk_sagemaker.types.cluster_instance_storage_configs.deserialize_aws_json_1_1(
                data["InstanceStorageConfigs"]
            )
        )
    if "OnStartDeepHealthChecks" in data:
        import aws_sdk_sagemaker.types.on_start_deep_health_checks

        out["on_start_deep_health_checks"] = (
            aws_sdk_sagemaker.types.on_start_deep_health_checks.deserialize_aws_json_1_1(
                data["OnStartDeepHealthChecks"]
            )
        )
    if "Status" in data:
        import aws_sdk_sagemaker.types.instance_group_status

        out["status"] = (
            aws_sdk_sagemaker.types.instance_group_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "TrainingPlanArn" in data:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    if "TrainingPlanStatus" in data:
        out["training_plan_status"] = data["TrainingPlanStatus"]
    if "OverrideVpcConfig" in data:
        import aws_sdk_sagemaker.types.vpc_config

        out["override_vpc_config"] = (
            aws_sdk_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
                data["OverrideVpcConfig"]
            )
        )
    if "ScheduledUpdateConfig" in data:
        import aws_sdk_sagemaker.types.scheduled_update_config

        out["scheduled_update_config"] = (
            aws_sdk_sagemaker.types.scheduled_update_config.deserialize_aws_json_1_1(
                data["ScheduledUpdateConfig"]
            )
        )
    if "EnvironmentConfig" in data:
        import aws_sdk_sagemaker.types.environment_config_details

        out["environment_config"] = (
            aws_sdk_sagemaker.types.environment_config_details.deserialize_aws_json_1_1(
                data["EnvironmentConfig"]
            )
        )
    return out
