"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceGroupSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_capacity_requirements
    import aws_sdk_sagemaker.types.cluster_instance_count
    import aws_sdk_sagemaker.types.cluster_instance_group_name
    import aws_sdk_sagemaker.types.cluster_instance_requirements
    import aws_sdk_sagemaker.types.cluster_instance_storage_configs
    import aws_sdk_sagemaker.types.cluster_instance_type
    import aws_sdk_sagemaker.types.cluster_kubernetes_config
    import aws_sdk_sagemaker.types.cluster_life_cycle_config
    import aws_sdk_sagemaker.types.cluster_network_interface
    import aws_sdk_sagemaker.types.cluster_slurm_config
    import aws_sdk_sagemaker.types.cluster_threads_per_core
    import aws_sdk_sagemaker.types.image_id
    import aws_sdk_sagemaker.types.on_start_deep_health_checks
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.scheduled_update_config
    import aws_sdk_sagemaker.types.training_plan_arn
    import aws_sdk_sagemaker.types.vpc_config


class ClusterInstanceGroupSpecification(TypedDict):
    instance_count: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_count.ClusterInstanceCount"
    ]
    """<p>Specifies the number of instances to add to the instance group of a SageMaker HyperPod cluster.</p>"""
    min_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_count.ClusterInstanceCount"
    ]
    """<p>Defines the minimum number of instances required for an instance group to become <code>InService</code>. If this threshold isn't met within 3 hours, the instance group rolls back to its previous state - zero instances for new instance groups, or previous settings for existing instance groups. <code>MinInstanceCount</code> only affects the initial transition to <code>InService</code> and does not guarantee maintaining this minimum afterward. </p>"""
    instance_group_name: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>Specifies the name of the instance group.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_type.ClusterInstanceType"
    ]
    """<p>Specifies the instance type of the instance group.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_requirements.ClusterInstanceRequirements"
    ]
    """<p>The instance requirements for the instance group, including the instance types to use. Use this to create a flexible instance group that supports multiple instance types. The <code>InstanceType</code> and <code>InstanceRequirements</code> properties are mutually exclusive.</p>"""
    life_cycle_config: NotRequired[
        "aws_sdk_sagemaker.types.cluster_life_cycle_config.ClusterLifeCycleConfig"
    ]
    """<p>Specifies the LifeCycle configuration for the instance group.</p>"""
    execution_role: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>Specifies an IAM execution role to be assumed by the instance group.</p>"""
    threads_per_core: NotRequired[
        "aws_sdk_sagemaker.types.cluster_threads_per_core.ClusterThreadsPerCore"
    ]
    """<p>Specifies the value for <b>Threads per core</b>. For instance types that support multithreading, you can specify <code>1</code> for disabling multithreading and <code>2</code> for enabling multithreading. For instance types that doesn't support multithreading, specify <code>1</code>. For more information, see the reference table of <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html\">CPU cores and threads per CPU core per instance type</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>"""
    instance_storage_configs: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_storage_configs.ClusterInstanceStorageConfigs"
    ]
    """<p>Specifies the additional storage configurations for the instances in the SageMaker HyperPod cluster instance group.</p>"""
    on_start_deep_health_checks: NotRequired[
        "aws_sdk_sagemaker.types.on_start_deep_health_checks.OnStartDeepHealthChecks"
    ]
    """<p>A flag indicating whether deep health checks should be performed when the cluster instance group is created or updated.</p>"""
    training_plan_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN); of the training plan to use for this cluster instance group.</p> <p>For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see <code> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html\">CreateTrainingPlan</a> </code>.</p>"""
    override_vpc_config: NotRequired["aws_sdk_sagemaker.types.vpc_config.VpcConfig"]
    """<p>To configure multi-AZ deployments, customize the Amazon VPC configuration at the instance group level. You can specify different subnets and security groups across different AZs in the instance group specification to override a SageMaker HyperPod cluster's default Amazon VPC configuration. For more information about deploying a cluster in multiple AZs, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-multiple-availability-zones\">Setting up SageMaker HyperPod clusters across multiple AZs</a>.</p> <note> <p>When your Amazon VPC and subnets support IPv6, network communications differ based on the cluster orchestration platform:</p> <ul> <li> <p>Slurm-orchestrated clusters automatically configure nodes with dual IPv6 and IPv4 addresses, allowing immediate IPv6 network communications.</p> </li> <li> <p>In Amazon EKS-orchestrated clusters, nodes receive dual-stack addressing, but pods can only use IPv6 when the Amazon EKS cluster is explicitly IPv6-enabled. For information about deploying an IPv6 Amazon EKS cluster, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/deploy-ipv6-cluster.html#_deploy_an_ipv6_cluster_with_eksctl\">Amazon EKS IPv6 Cluster Deployment</a>.</p> </li> </ul> <p>Additional resources for IPv6 configuration:</p> <ul> <li> <p>For information about adding IPv6 support to your VPC, see to <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html\">IPv6 Support for VPC</a>.</p> </li> <li> <p>For information about creating a new IPv6-compatible VPC, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html\">Amazon VPC Creation Guide</a>.</p> </li> <li> <p>To configure SageMaker HyperPod with a custom Amazon VPC, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-optional-vpc\">Custom Amazon VPC Setup for SageMaker HyperPod</a>.</p> </li> </ul> </note>"""
    scheduled_update_config: NotRequired[
        "aws_sdk_sagemaker.types.scheduled_update_config.ScheduledUpdateConfig"
    ]
    """<p>The configuration object of the schedule that SageMaker uses to update the AMI.</p>"""
    image_id: NotRequired["aws_sdk_sagemaker.types.image_id.ImageId"]
    """<p>When configuring your HyperPod cluster, you can specify an image ID using one of the following options:</p> <ul> <li> <p> <code>HyperPodPublicAmiId</code>: Use a HyperPod public AMI</p> </li> <li> <p> <code>CustomAmiId</code>: Use your custom AMI</p> </li> <li> <p> <code>default</code>: Use the default latest system image</p> </li> </ul> <p>If you choose to use a custom AMI (<code>CustomAmiId</code>), ensure it meets the following requirements:</p> <ul> <li> <p>Encryption: The custom AMI must be unencrypted.</p> </li> <li> <p>Ownership: The custom AMI must be owned by the same Amazon Web Services account that is creating the HyperPod cluster.</p> </li> <li> <p>Volume support: Only the primary AMI snapshot volume is supported; additional AMI volumes are not supported.</p> </li> </ul> <p>When updating the instance group's AMI through the <code>UpdateClusterSoftware</code> operation, if an instance group uses a custom AMI, you must provide an <code>ImageId</code> or use the default as input. Note that if you don't specify an instance group in your <code>UpdateClusterSoftware</code> request, then all of the instance groups are patched with the specified image.</p>"""
    kubernetes_config: NotRequired[
        "aws_sdk_sagemaker.types.cluster_kubernetes_config.ClusterKubernetesConfig"
    ]
    """<p>Specifies the Kubernetes configuration for the instance group. You describe what you want the labels and taints to look like, and the cluster works to reconcile the actual state with the declared state for nodes in this instance group. </p>"""
    slurm_config: NotRequired[
        "aws_sdk_sagemaker.types.cluster_slurm_config.ClusterSlurmConfig"
    ]
    """<p>Specifies the Slurm configuration for the instance group.</p>"""
    capacity_requirements: NotRequired[
        "aws_sdk_sagemaker.types.cluster_capacity_requirements.ClusterCapacityRequirements"
    ]
    """<p>Specifies the capacity requirements for the instance group.</p>"""
    network_interface: NotRequired[
        "aws_sdk_sagemaker.types.cluster_network_interface.ClusterNetworkInterface"
    ]
    """<p>The network interface configuration for the instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceGroupSpecification) -> dict:
    out: dict = {}
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "min_instance_count" in value:
        out["MinInstanceCount"] = value["min_instance_count"]
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.cluster_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.cluster_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_requirements" in value:
        import aws_sdk_sagemaker.types.cluster_instance_requirements

        out["InstanceRequirements"] = (
            aws_sdk_sagemaker.types.cluster_instance_requirements.serialize_aws_json_1_1(
                value["instance_requirements"]
            )
        )
    if "life_cycle_config" in value:
        import aws_sdk_sagemaker.types.cluster_life_cycle_config

        out["LifeCycleConfig"] = (
            aws_sdk_sagemaker.types.cluster_life_cycle_config.serialize_aws_json_1_1(
                value["life_cycle_config"]
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
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "kubernetes_config" in value:
        import aws_sdk_sagemaker.types.cluster_kubernetes_config

        out["KubernetesConfig"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_config.serialize_aws_json_1_1(
                value["kubernetes_config"]
            )
        )
    if "slurm_config" in value:
        import aws_sdk_sagemaker.types.cluster_slurm_config

        out["SlurmConfig"] = (
            aws_sdk_sagemaker.types.cluster_slurm_config.serialize_aws_json_1_1(
                value["slurm_config"]
            )
        )
    if "capacity_requirements" in value:
        import aws_sdk_sagemaker.types.cluster_capacity_requirements

        out["CapacityRequirements"] = (
            aws_sdk_sagemaker.types.cluster_capacity_requirements.serialize_aws_json_1_1(
                value["capacity_requirements"]
            )
        )
    if "network_interface" in value:
        import aws_sdk_sagemaker.types.cluster_network_interface

        out["NetworkInterface"] = (
            aws_sdk_sagemaker.types.cluster_network_interface.serialize_aws_json_1_1(
                value["network_interface"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterInstanceGroupSpecification:
    out: ClusterInstanceGroupSpecification = {}  # type: ignore[typeddict-item]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "MinInstanceCount" in data:
        out["min_instance_count"] = data["MinInstanceCount"]
    if "InstanceGroupName" in data:
        out["instance_group_name"] = data["InstanceGroupName"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.cluster_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.cluster_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "InstanceRequirements" in data:
        import aws_sdk_sagemaker.types.cluster_instance_requirements

        out["instance_requirements"] = (
            aws_sdk_sagemaker.types.cluster_instance_requirements.deserialize_aws_json_1_1(
                data["InstanceRequirements"]
            )
        )
    if "LifeCycleConfig" in data:
        import aws_sdk_sagemaker.types.cluster_life_cycle_config

        out["life_cycle_config"] = (
            aws_sdk_sagemaker.types.cluster_life_cycle_config.deserialize_aws_json_1_1(
                data["LifeCycleConfig"]
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
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "KubernetesConfig" in data:
        import aws_sdk_sagemaker.types.cluster_kubernetes_config

        out["kubernetes_config"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_config.deserialize_aws_json_1_1(
                data["KubernetesConfig"]
            )
        )
    if "SlurmConfig" in data:
        import aws_sdk_sagemaker.types.cluster_slurm_config

        out["slurm_config"] = (
            aws_sdk_sagemaker.types.cluster_slurm_config.deserialize_aws_json_1_1(
                data["SlurmConfig"]
            )
        )
    if "CapacityRequirements" in data:
        import aws_sdk_sagemaker.types.cluster_capacity_requirements

        out["capacity_requirements"] = (
            aws_sdk_sagemaker.types.cluster_capacity_requirements.deserialize_aws_json_1_1(
                data["CapacityRequirements"]
            )
        )
    if "NetworkInterface" in data:
        import aws_sdk_sagemaker.types.cluster_network_interface

        out["network_interface"] = (
            aws_sdk_sagemaker.types.cluster_network_interface.deserialize_aws_json_1_1(
                data["NetworkInterface"]
            )
        )
    return out
