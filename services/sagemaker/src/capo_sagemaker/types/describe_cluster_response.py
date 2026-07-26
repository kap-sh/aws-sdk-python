"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.cluster_auto_scaling_config_output
    import capo_sagemaker.types.cluster_instance_group_details_list
    import capo_sagemaker.types.cluster_name
    import capo_sagemaker.types.cluster_node_provisioning_mode
    import capo_sagemaker.types.cluster_node_recovery
    import capo_sagemaker.types.cluster_orchestrator
    import capo_sagemaker.types.cluster_restricted_instance_group_details_list
    import capo_sagemaker.types.cluster_restricted_instance_groups_config_output
    import capo_sagemaker.types.cluster_status
    import capo_sagemaker.types.cluster_tiered_storage_config
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.string
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.vpc_config


class DescribeClusterResponse(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.</p>"""
    cluster_name: NotRequired["capo_sagemaker.types.cluster_name.ClusterName"]
    """<p>The name of the SageMaker HyperPod cluster.</p>"""
    cluster_status: NotRequired["capo_sagemaker.types.cluster_status.ClusterStatus"]
    """<p>The status of the SageMaker HyperPod cluster.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the SageMaker Cluster is created.</p>"""
    failure_message: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The failure message of the SageMaker HyperPod cluster.</p>"""
    instance_groups: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_details_list.ClusterInstanceGroupDetailsList"
    ]
    """<p>The instance groups of the SageMaker HyperPod cluster.</p>"""
    restricted_instance_groups: NotRequired[
        "capo_sagemaker.types.cluster_restricted_instance_group_details_list.ClusterRestrictedInstanceGroupDetailsList"
    ]
    """<p>The specialized instance groups for training models like Amazon Nova to be created in the SageMaker HyperPod cluster.</p>"""
    restricted_instance_groups_config: NotRequired[
        "capo_sagemaker.types.cluster_restricted_instance_groups_config_output.ClusterRestrictedInstanceGroupsConfigOutput"
    ]
    """<p>The configuration for the restricted instance groups (RIG) in the SageMaker HyperPod cluster.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    orchestrator: NotRequired[
        "capo_sagemaker.types.cluster_orchestrator.ClusterOrchestrator"
    ]
    """<p>The type of orchestrator used for the SageMaker HyperPod cluster. </p>"""
    tiered_storage_config: NotRequired[
        "capo_sagemaker.types.cluster_tiered_storage_config.ClusterTieredStorageConfig"
    ]
    """<p>The current configuration for managed tier checkpointing on the HyperPod cluster. For example, this shows whether the feature is enabled and the percentage of cluster memory allocated for checkpoint storage.</p>"""
    node_recovery: NotRequired[
        "capo_sagemaker.types.cluster_node_recovery.ClusterNodeRecovery"
    ]
    """<p>The node recovery mode configured for the SageMaker HyperPod cluster.</p>"""
    node_provisioning_mode: NotRequired[
        "capo_sagemaker.types.cluster_node_provisioning_mode.ClusterNodeProvisioningMode"
    ]
    """<p>The mode used for provisioning nodes in the cluster.</p>"""
    cluster_role: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that HyperPod uses for cluster autoscaling operations.</p>"""
    auto_scaling: NotRequired[
        "capo_sagemaker.types.cluster_auto_scaling_config_output.ClusterAutoScalingConfigOutput"
    ]
    """<p>The current autoscaling configuration and status for the autoscaler.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterResponse) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "cluster_status" in value:
        import capo_sagemaker.types.cluster_status

        out["ClusterStatus"] = (
            capo_sagemaker.types.cluster_status.serialize_aws_json_1_1(
                value["cluster_status"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "instance_groups" in value:
        import capo_sagemaker.types.cluster_instance_group_details_list

        out["InstanceGroups"] = (
            capo_sagemaker.types.cluster_instance_group_details_list.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    if "restricted_instance_groups" in value:
        import capo_sagemaker.types.cluster_restricted_instance_group_details_list

        out["RestrictedInstanceGroups"] = (
            capo_sagemaker.types.cluster_restricted_instance_group_details_list.serialize_aws_json_1_1(
                value["restricted_instance_groups"]
            )
        )
    if "restricted_instance_groups_config" in value:
        import capo_sagemaker.types.cluster_restricted_instance_groups_config_output

        out["RestrictedInstanceGroupsConfig"] = (
            capo_sagemaker.types.cluster_restricted_instance_groups_config_output.serialize_aws_json_1_1(
                value["restricted_instance_groups_config"]
            )
        )
    if "vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["VpcConfig"] = capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "orchestrator" in value:
        import capo_sagemaker.types.cluster_orchestrator

        out["Orchestrator"] = (
            capo_sagemaker.types.cluster_orchestrator.serialize_aws_json_1_1(
                value["orchestrator"]
            )
        )
    if "tiered_storage_config" in value:
        import capo_sagemaker.types.cluster_tiered_storage_config

        out["TieredStorageConfig"] = (
            capo_sagemaker.types.cluster_tiered_storage_config.serialize_aws_json_1_1(
                value["tiered_storage_config"]
            )
        )
    if "node_recovery" in value:
        import capo_sagemaker.types.cluster_node_recovery

        out["NodeRecovery"] = (
            capo_sagemaker.types.cluster_node_recovery.serialize_aws_json_1_1(
                value["node_recovery"]
            )
        )
    if "node_provisioning_mode" in value:
        import capo_sagemaker.types.cluster_node_provisioning_mode

        out["NodeProvisioningMode"] = (
            capo_sagemaker.types.cluster_node_provisioning_mode.serialize_aws_json_1_1(
                value["node_provisioning_mode"]
            )
        )
    if "cluster_role" in value:
        out["ClusterRole"] = value["cluster_role"]
    if "auto_scaling" in value:
        import capo_sagemaker.types.cluster_auto_scaling_config_output

        out["AutoScaling"] = (
            capo_sagemaker.types.cluster_auto_scaling_config_output.serialize_aws_json_1_1(
                value["auto_scaling"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterResponse:
    out: DescribeClusterResponse = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "ClusterStatus" in data:
        import capo_sagemaker.types.cluster_status

        out["cluster_status"] = (
            capo_sagemaker.types.cluster_status.deserialize_aws_json_1_1(
                data["ClusterStatus"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "InstanceGroups" in data:
        import capo_sagemaker.types.cluster_instance_group_details_list

        out["instance_groups"] = (
            capo_sagemaker.types.cluster_instance_group_details_list.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    if "RestrictedInstanceGroups" in data:
        import capo_sagemaker.types.cluster_restricted_instance_group_details_list

        out["restricted_instance_groups"] = (
            capo_sagemaker.types.cluster_restricted_instance_group_details_list.deserialize_aws_json_1_1(
                data["RestrictedInstanceGroups"]
            )
        )
    if "RestrictedInstanceGroupsConfig" in data:
        import capo_sagemaker.types.cluster_restricted_instance_groups_config_output

        out["restricted_instance_groups_config"] = (
            capo_sagemaker.types.cluster_restricted_instance_groups_config_output.deserialize_aws_json_1_1(
                data["RestrictedInstanceGroupsConfig"]
            )
        )
    if "VpcConfig" in data:
        import capo_sagemaker.types.vpc_config

        out["vpc_config"] = capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if "Orchestrator" in data:
        import capo_sagemaker.types.cluster_orchestrator

        out["orchestrator"] = (
            capo_sagemaker.types.cluster_orchestrator.deserialize_aws_json_1_1(
                data["Orchestrator"]
            )
        )
    if "TieredStorageConfig" in data:
        import capo_sagemaker.types.cluster_tiered_storage_config

        out["tiered_storage_config"] = (
            capo_sagemaker.types.cluster_tiered_storage_config.deserialize_aws_json_1_1(
                data["TieredStorageConfig"]
            )
        )
    if "NodeRecovery" in data:
        import capo_sagemaker.types.cluster_node_recovery

        out["node_recovery"] = (
            capo_sagemaker.types.cluster_node_recovery.deserialize_aws_json_1_1(
                data["NodeRecovery"]
            )
        )
    if "NodeProvisioningMode" in data:
        import capo_sagemaker.types.cluster_node_provisioning_mode

        out["node_provisioning_mode"] = (
            capo_sagemaker.types.cluster_node_provisioning_mode.deserialize_aws_json_1_1(
                data["NodeProvisioningMode"]
            )
        )
    if "ClusterRole" in data:
        out["cluster_role"] = data["ClusterRole"]
    if "AutoScaling" in data:
        import capo_sagemaker.types.cluster_auto_scaling_config_output

        out["auto_scaling"] = (
            capo_sagemaker.types.cluster_auto_scaling_config_output.deserialize_aws_json_1_1(
                data["AutoScaling"]
            )
        )
    return out
