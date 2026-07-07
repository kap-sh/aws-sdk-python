"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterRestrictedInstanceGroupSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_count
    import aws_sdk_sagemaker.types.cluster_instance_group_name
    import aws_sdk_sagemaker.types.cluster_instance_storage_configs
    import aws_sdk_sagemaker.types.cluster_instance_type
    import aws_sdk_sagemaker.types.cluster_threads_per_core
    import aws_sdk_sagemaker.types.environment_config
    import aws_sdk_sagemaker.types.on_start_deep_health_checks
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.scheduled_update_config
    import aws_sdk_sagemaker.types.training_plan_arn
    import aws_sdk_sagemaker.types.vpc_config


class ClusterRestrictedInstanceGroupSpecification(TypedDict, closed=True):
    instance_count: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_count.ClusterInstanceCount"
    ]
    """<p>Specifies the number of instances to add to the restricted instance group of a SageMaker HyperPod cluster.</p>"""
    instance_group_name: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>Specifies the name of the restricted instance group.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_type.ClusterInstanceType"
    ]
    """<p>Specifies the instance type of the restricted instance group.</p>"""
    execution_role: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>Specifies an IAM execution role to be assumed by the restricted instance group.</p>"""
    threads_per_core: NotRequired[
        "aws_sdk_sagemaker.types.cluster_threads_per_core.ClusterThreadsPerCore"
    ]
    r"""<p>The number you specified to <code>TreadsPerCore</code> in <code>CreateCluster</code> for enabling or disabling multithreading. For instance types that support multithreading, you can specify 1 for disabling multithreading and 2 for enabling multithreading. For more information, see the reference table of <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html\">CPU cores and threads per CPU core per instance type</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>"""
    instance_storage_configs: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_storage_configs.ClusterInstanceStorageConfigs"
    ]
    """<p>Specifies the additional storage configurations for the instances in the SageMaker HyperPod cluster restricted instance group.</p>"""
    on_start_deep_health_checks: NotRequired[
        "aws_sdk_sagemaker.types.on_start_deep_health_checks.OnStartDeepHealthChecks"
    ]
    """<p>A flag indicating whether deep health checks should be performed when the cluster restricted instance group is created or updated.</p>"""
    training_plan_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the training plan to filter clusters by. For more information about reserving GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see <code> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html\">CreateTrainingPlan</a> </code>.</p>"""
    override_vpc_config: NotRequired["aws_sdk_sagemaker.types.vpc_config.VpcConfig"]
    scheduled_update_config: NotRequired[
        "aws_sdk_sagemaker.types.scheduled_update_config.ScheduledUpdateConfig"
    ]
    environment_config: NotRequired[
        "aws_sdk_sagemaker.types.environment_config.EnvironmentConfig"
    ]
    """<p>The configuration for the restricted instance groups (RIG) environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterRestrictedInstanceGroupSpecification) -> dict:
    out: dict = {}
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
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
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
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
        import aws_sdk_sagemaker.types.environment_config

        out["EnvironmentConfig"] = (
            aws_sdk_sagemaker.types.environment_config.serialize_aws_json_1_1(
                value["environment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterRestrictedInstanceGroupSpecification:
    out: ClusterRestrictedInstanceGroupSpecification = {}  # type: ignore[typeddict-item]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
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
    if "TrainingPlanArn" in data:
        out["training_plan_arn"] = data["TrainingPlanArn"]
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
        import aws_sdk_sagemaker.types.environment_config

        out["environment_config"] = (
            aws_sdk_sagemaker.types.environment_config.deserialize_aws_json_1_1(
                data["EnvironmentConfig"]
            )
        )
    return out
