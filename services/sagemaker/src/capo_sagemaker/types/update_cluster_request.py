"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_auto_scaling_config
    import capo_sagemaker.types.cluster_instance_group_specifications
    import capo_sagemaker.types.cluster_instance_groups_to_delete
    import capo_sagemaker.types.cluster_name_or_arn
    import capo_sagemaker.types.cluster_node_provisioning_mode
    import capo_sagemaker.types.cluster_node_recovery
    import capo_sagemaker.types.cluster_orchestrator
    import capo_sagemaker.types.cluster_restricted_instance_group_specifications
    import capo_sagemaker.types.cluster_restricted_instance_groups_config
    import capo_sagemaker.types.cluster_tiered_storage_config
    import capo_sagemaker.types.role_arn


class UpdateClusterRequest(TypedDict, closed=True):
    cluster_name: NotRequired[
        "capo_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>Specify the name of the SageMaker HyperPod cluster you want to update.</p>"""
    instance_groups: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_specifications.ClusterInstanceGroupSpecifications"
    ]
    """<p>Specify the instance groups to update.</p>"""
    restricted_instance_groups: NotRequired[
        "capo_sagemaker.types.cluster_restricted_instance_group_specifications.ClusterRestrictedInstanceGroupSpecifications"
    ]
    """<p>The specialized instance groups for training models like Amazon Nova to be created in the SageMaker HyperPod cluster.</p>"""
    restricted_instance_groups_config: NotRequired[
        "capo_sagemaker.types.cluster_restricted_instance_groups_config.ClusterRestrictedInstanceGroupsConfig"
    ]
    """<p>The configuration for the restricted instance groups (RIG) in the SageMaker HyperPod cluster.</p>"""
    tiered_storage_config: NotRequired[
        "capo_sagemaker.types.cluster_tiered_storage_config.ClusterTieredStorageConfig"
    ]
    """<p>Updates the configuration for managed tier checkpointing on the HyperPod cluster. For example, you can enable or disable the feature and modify the percentage of cluster memory allocated for checkpoint storage.</p>"""
    node_recovery: NotRequired[
        "capo_sagemaker.types.cluster_node_recovery.ClusterNodeRecovery"
    ]
    """<p>The node recovery mode to be applied to the SageMaker HyperPod cluster.</p>"""
    instance_groups_to_delete: NotRequired[
        "capo_sagemaker.types.cluster_instance_groups_to_delete.ClusterInstanceGroupsToDelete"
    ]
    """<p>Specify the names of the instance groups to delete. Use a single <code>,</code> as the separator between multiple names.</p>"""
    node_provisioning_mode: NotRequired[
        "capo_sagemaker.types.cluster_node_provisioning_mode.ClusterNodeProvisioningMode"
    ]
    """<p>Determines how instance provisioning is handled during cluster operations. In <code>Continuous</code> mode, the cluster provisions available instances incrementally and retries until the target count is reached. The cluster becomes operational once cluster-level resources are ready. Use <code>CurrentCount</code> and <code>TargetCount</code> in <code>DescribeCluster</code> to track provisioning progress.</p>"""
    cluster_role: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that HyperPod assumes for cluster autoscaling operations. Cannot be updated while autoscaling is enabled.</p>"""
    auto_scaling: NotRequired[
        "capo_sagemaker.types.cluster_auto_scaling_config.ClusterAutoScalingConfig"
    ]
    """<p>Updates the autoscaling configuration for the cluster. Use to enable or disable automatic node scaling.</p>"""
    orchestrator: NotRequired[
        "capo_sagemaker.types.cluster_orchestrator.ClusterOrchestrator"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "instance_groups" in value:
        import capo_sagemaker.types.cluster_instance_group_specifications

        out["InstanceGroups"] = (
            capo_sagemaker.types.cluster_instance_group_specifications.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    if "restricted_instance_groups" in value:
        import capo_sagemaker.types.cluster_restricted_instance_group_specifications

        out["RestrictedInstanceGroups"] = (
            capo_sagemaker.types.cluster_restricted_instance_group_specifications.serialize_aws_json_1_1(
                value["restricted_instance_groups"]
            )
        )
    if "restricted_instance_groups_config" in value:
        import capo_sagemaker.types.cluster_restricted_instance_groups_config

        out["RestrictedInstanceGroupsConfig"] = (
            capo_sagemaker.types.cluster_restricted_instance_groups_config.serialize_aws_json_1_1(
                value["restricted_instance_groups_config"]
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
    if "instance_groups_to_delete" in value:
        import capo_sagemaker.types.cluster_instance_groups_to_delete

        out["InstanceGroupsToDelete"] = (
            capo_sagemaker.types.cluster_instance_groups_to_delete.serialize_aws_json_1_1(
                value["instance_groups_to_delete"]
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
        import capo_sagemaker.types.cluster_auto_scaling_config

        out["AutoScaling"] = (
            capo_sagemaker.types.cluster_auto_scaling_config.serialize_aws_json_1_1(
                value["auto_scaling"]
            )
        )
    if "orchestrator" in value:
        import capo_sagemaker.types.cluster_orchestrator

        out["Orchestrator"] = (
            capo_sagemaker.types.cluster_orchestrator.serialize_aws_json_1_1(
                value["orchestrator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterRequest:
    out: UpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "InstanceGroups" in data:
        import capo_sagemaker.types.cluster_instance_group_specifications

        out["instance_groups"] = (
            capo_sagemaker.types.cluster_instance_group_specifications.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    if "RestrictedInstanceGroups" in data:
        import capo_sagemaker.types.cluster_restricted_instance_group_specifications

        out["restricted_instance_groups"] = (
            capo_sagemaker.types.cluster_restricted_instance_group_specifications.deserialize_aws_json_1_1(
                data["RestrictedInstanceGroups"]
            )
        )
    if "RestrictedInstanceGroupsConfig" in data:
        import capo_sagemaker.types.cluster_restricted_instance_groups_config

        out["restricted_instance_groups_config"] = (
            capo_sagemaker.types.cluster_restricted_instance_groups_config.deserialize_aws_json_1_1(
                data["RestrictedInstanceGroupsConfig"]
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
    if "InstanceGroupsToDelete" in data:
        import capo_sagemaker.types.cluster_instance_groups_to_delete

        out["instance_groups_to_delete"] = (
            capo_sagemaker.types.cluster_instance_groups_to_delete.deserialize_aws_json_1_1(
                data["InstanceGroupsToDelete"]
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
        import capo_sagemaker.types.cluster_auto_scaling_config

        out["auto_scaling"] = (
            capo_sagemaker.types.cluster_auto_scaling_config.deserialize_aws_json_1_1(
                data["AutoScaling"]
            )
        )
    if "Orchestrator" in data:
        import capo_sagemaker.types.cluster_orchestrator

        out["orchestrator"] = (
            capo_sagemaker.types.cluster_orchestrator.deserialize_aws_json_1_1(
                data["Orchestrator"]
            )
        )
    return out
