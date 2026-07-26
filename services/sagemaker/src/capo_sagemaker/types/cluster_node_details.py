"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNodeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_capacity_type
    import capo_sagemaker.types.cluster_image_version_status
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.cluster_instance_placement
    import capo_sagemaker.types.cluster_instance_status_details
    import capo_sagemaker.types.cluster_instance_storage_configs
    import capo_sagemaker.types.cluster_instance_type
    import capo_sagemaker.types.cluster_kubernetes_config_node_details
    import capo_sagemaker.types.cluster_life_cycle_config
    import capo_sagemaker.types.cluster_network_interface_details
    import capo_sagemaker.types.cluster_node_logical_id
    import capo_sagemaker.types.cluster_private_dns_hostname
    import capo_sagemaker.types.cluster_private_primary_ip
    import capo_sagemaker.types.cluster_private_primary_ipv6
    import capo_sagemaker.types.cluster_threads_per_core
    import capo_sagemaker.types.image_id
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.ultra_server_info
    import capo_sagemaker.types.vpc_config


class ClusterNodeDetails(TypedDict, closed=True):
    instance_group_name: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>The instance group name in which the instance is.</p>"""
    instance_id: NotRequired["str"]
    """<p>The ID of the instance.</p>"""
    node_logical_id: NotRequired[
        "capo_sagemaker.types.cluster_node_logical_id.ClusterNodeLogicalId"
    ]
    """<p>A unique identifier for the node that persists throughout its lifecycle, from provisioning request to termination. This identifier can be used to track the node even before it has an assigned <code>InstanceId</code>.</p>"""
    instance_status: NotRequired[
        "capo_sagemaker.types.cluster_instance_status_details.ClusterInstanceStatusDetails"
    ]
    """<p>The status of the instance.</p>"""
    instance_type: NotRequired[
        "capo_sagemaker.types.cluster_instance_type.ClusterInstanceType"
    ]
    """<p>The type of the instance.</p>"""
    launch_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the instance is launched.</p>"""
    last_software_update_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the cluster was last updated.</p>"""
    life_cycle_config: NotRequired[
        "capo_sagemaker.types.cluster_life_cycle_config.ClusterLifeCycleConfig"
    ]
    """<p>The LifeCycle configuration applied to the instance.</p>"""
    override_vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    """<p>The customized Amazon VPC configuration at the instance group level that overrides the default Amazon VPC configuration of the SageMaker HyperPod cluster.</p>"""
    threads_per_core: NotRequired[
        "capo_sagemaker.types.cluster_threads_per_core.ClusterThreadsPerCore"
    ]
    """<p>The number of threads per CPU core you specified under <code>CreateCluster</code>.</p>"""
    instance_storage_configs: NotRequired[
        "capo_sagemaker.types.cluster_instance_storage_configs.ClusterInstanceStorageConfigs"
    ]
    """<p>The configurations of additional storage specified to the instance group where the instance (node) is launched.</p>"""
    private_primary_ip: NotRequired[
        "capo_sagemaker.types.cluster_private_primary_ip.ClusterPrivatePrimaryIp"
    ]
    """<p>The private primary IP address of the SageMaker HyperPod cluster node.</p>"""
    private_primary_ipv6: NotRequired[
        "capo_sagemaker.types.cluster_private_primary_ipv6.ClusterPrivatePrimaryIpv6"
    ]
    """<p>The private primary IPv6 address of the SageMaker HyperPod cluster node when configured with an Amazon VPC that supports IPv6 and includes subnets with IPv6 addressing enabled in either the cluster Amazon VPC configuration or the instance group Amazon VPC configuration.</p>"""
    private_dns_hostname: NotRequired[
        "capo_sagemaker.types.cluster_private_dns_hostname.ClusterPrivateDnsHostname"
    ]
    """<p>The private DNS hostname of the SageMaker HyperPod cluster node.</p>"""
    placement: NotRequired[
        "capo_sagemaker.types.cluster_instance_placement.ClusterInstancePlacement"
    ]
    """<p>The placement details of the SageMaker HyperPod cluster node.</p>"""
    current_image_id: NotRequired["capo_sagemaker.types.image_id.ImageId"]
    """<p>The ID of the Amazon Machine Image (AMI) currently in use by the node.</p>"""
    desired_image_id: NotRequired["capo_sagemaker.types.image_id.ImageId"]
    """<p>The ID of the Amazon Machine Image (AMI) desired for the node.</p>"""
    image_version_status: NotRequired[
        "capo_sagemaker.types.cluster_image_version_status.ClusterImageVersionStatus"
    ]
    """<p>The status of the image version for the cluster node.</p>"""
    ultra_server_info: NotRequired[
        "capo_sagemaker.types.ultra_server_info.UltraServerInfo"
    ]
    """<p>Contains information about the UltraServer.</p>"""
    kubernetes_config: NotRequired[
        "capo_sagemaker.types.cluster_kubernetes_config_node_details.ClusterKubernetesConfigNodeDetails"
    ]
    """<p>The Kubernetes configuration applied to this node, showing both the current and desired state of labels and taints. The cluster works to reconcile the actual state with the declared state. </p>"""
    capacity_type: NotRequired[
        "capo_sagemaker.types.cluster_capacity_type.ClusterCapacityType"
    ]
    """<p>The capacity type of the node. Valid values are <code>OnDemand</code> and <code>Spot</code>. When set to <code>OnDemand</code>, the node is launched as an On-Demand instance. When set to <code>Spot</code>, the node is launched as a Spot instance. </p>"""
    network_interface: NotRequired[
        "capo_sagemaker.types.cluster_network_interface_details.ClusterNetworkInterfaceDetails"
    ]
    """<p>The network interface configuration for the cluster node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNodeDetails) -> dict:
    out: dict = {}
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "node_logical_id" in value:
        out["NodeLogicalId"] = value["node_logical_id"]
    if "instance_status" in value:
        import capo_sagemaker.types.cluster_instance_status_details

        out["InstanceStatus"] = (
            capo_sagemaker.types.cluster_instance_status_details.serialize_aws_json_1_1(
                value["instance_status"]
            )
        )
    if "instance_type" in value:
        import capo_sagemaker.types.cluster_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.cluster_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "launch_time" in value:
        import capo_sagemaker.types.timestamp

        out["LaunchTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["launch_time"]
        )
    if "last_software_update_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastSoftwareUpdateTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_software_update_time"]
            )
        )
    if "life_cycle_config" in value:
        import capo_sagemaker.types.cluster_life_cycle_config

        out["LifeCycleConfig"] = (
            capo_sagemaker.types.cluster_life_cycle_config.serialize_aws_json_1_1(
                value["life_cycle_config"]
            )
        )
    if "override_vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["OverrideVpcConfig"] = (
            capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
                value["override_vpc_config"]
            )
        )
    if "threads_per_core" in value:
        out["ThreadsPerCore"] = value["threads_per_core"]
    if "instance_storage_configs" in value:
        import capo_sagemaker.types.cluster_instance_storage_configs

        out["InstanceStorageConfigs"] = (
            capo_sagemaker.types.cluster_instance_storage_configs.serialize_aws_json_1_1(
                value["instance_storage_configs"]
            )
        )
    if "private_primary_ip" in value:
        out["PrivatePrimaryIp"] = value["private_primary_ip"]
    if "private_primary_ipv6" in value:
        out["PrivatePrimaryIpv6"] = value["private_primary_ipv6"]
    if "private_dns_hostname" in value:
        out["PrivateDnsHostname"] = value["private_dns_hostname"]
    if "placement" in value:
        import capo_sagemaker.types.cluster_instance_placement

        out["Placement"] = (
            capo_sagemaker.types.cluster_instance_placement.serialize_aws_json_1_1(
                value["placement"]
            )
        )
    if "current_image_id" in value:
        out["CurrentImageId"] = value["current_image_id"]
    if "desired_image_id" in value:
        out["DesiredImageId"] = value["desired_image_id"]
    if "image_version_status" in value:
        import capo_sagemaker.types.cluster_image_version_status

        out["ImageVersionStatus"] = (
            capo_sagemaker.types.cluster_image_version_status.serialize_aws_json_1_1(
                value["image_version_status"]
            )
        )
    if "ultra_server_info" in value:
        import capo_sagemaker.types.ultra_server_info

        out["UltraServerInfo"] = (
            capo_sagemaker.types.ultra_server_info.serialize_aws_json_1_1(
                value["ultra_server_info"]
            )
        )
    if "kubernetes_config" in value:
        import capo_sagemaker.types.cluster_kubernetes_config_node_details

        out["KubernetesConfig"] = (
            capo_sagemaker.types.cluster_kubernetes_config_node_details.serialize_aws_json_1_1(
                value["kubernetes_config"]
            )
        )
    if "capacity_type" in value:
        import capo_sagemaker.types.cluster_capacity_type

        out["CapacityType"] = (
            capo_sagemaker.types.cluster_capacity_type.serialize_aws_json_1_1(
                value["capacity_type"]
            )
        )
    if "network_interface" in value:
        import capo_sagemaker.types.cluster_network_interface_details

        out["NetworkInterface"] = (
            capo_sagemaker.types.cluster_network_interface_details.serialize_aws_json_1_1(
                value["network_interface"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterNodeDetails:
    out: ClusterNodeDetails = {}  # type: ignore[typeddict-item]
    if "InstanceGroupName" in data:
        out["instance_group_name"] = data["InstanceGroupName"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "NodeLogicalId" in data:
        out["node_logical_id"] = data["NodeLogicalId"]
    if "InstanceStatus" in data:
        import capo_sagemaker.types.cluster_instance_status_details

        out["instance_status"] = (
            capo_sagemaker.types.cluster_instance_status_details.deserialize_aws_json_1_1(
                data["InstanceStatus"]
            )
        )
    if "InstanceType" in data:
        import capo_sagemaker.types.cluster_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.cluster_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "LaunchTime" in data:
        import capo_sagemaker.types.timestamp

        out["launch_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["LaunchTime"]
        )
    if "LastSoftwareUpdateTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_software_update_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastSoftwareUpdateTime"]
            )
        )
    if "LifeCycleConfig" in data:
        import capo_sagemaker.types.cluster_life_cycle_config

        out["life_cycle_config"] = (
            capo_sagemaker.types.cluster_life_cycle_config.deserialize_aws_json_1_1(
                data["LifeCycleConfig"]
            )
        )
    if "OverrideVpcConfig" in data:
        import capo_sagemaker.types.vpc_config

        out["override_vpc_config"] = (
            capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
                data["OverrideVpcConfig"]
            )
        )
    if "ThreadsPerCore" in data:
        out["threads_per_core"] = data["ThreadsPerCore"]
    if "InstanceStorageConfigs" in data:
        import capo_sagemaker.types.cluster_instance_storage_configs

        out["instance_storage_configs"] = (
            capo_sagemaker.types.cluster_instance_storage_configs.deserialize_aws_json_1_1(
                data["InstanceStorageConfigs"]
            )
        )
    if "PrivatePrimaryIp" in data:
        out["private_primary_ip"] = data["PrivatePrimaryIp"]
    if "PrivatePrimaryIpv6" in data:
        out["private_primary_ipv6"] = data["PrivatePrimaryIpv6"]
    if "PrivateDnsHostname" in data:
        out["private_dns_hostname"] = data["PrivateDnsHostname"]
    if "Placement" in data:
        import capo_sagemaker.types.cluster_instance_placement

        out["placement"] = (
            capo_sagemaker.types.cluster_instance_placement.deserialize_aws_json_1_1(
                data["Placement"]
            )
        )
    if "CurrentImageId" in data:
        out["current_image_id"] = data["CurrentImageId"]
    if "DesiredImageId" in data:
        out["desired_image_id"] = data["DesiredImageId"]
    if "ImageVersionStatus" in data:
        import capo_sagemaker.types.cluster_image_version_status

        out["image_version_status"] = (
            capo_sagemaker.types.cluster_image_version_status.deserialize_aws_json_1_1(
                data["ImageVersionStatus"]
            )
        )
    if "UltraServerInfo" in data:
        import capo_sagemaker.types.ultra_server_info

        out["ultra_server_info"] = (
            capo_sagemaker.types.ultra_server_info.deserialize_aws_json_1_1(
                data["UltraServerInfo"]
            )
        )
    if "KubernetesConfig" in data:
        import capo_sagemaker.types.cluster_kubernetes_config_node_details

        out["kubernetes_config"] = (
            capo_sagemaker.types.cluster_kubernetes_config_node_details.deserialize_aws_json_1_1(
                data["KubernetesConfig"]
            )
        )
    if "CapacityType" in data:
        import capo_sagemaker.types.cluster_capacity_type

        out["capacity_type"] = (
            capo_sagemaker.types.cluster_capacity_type.deserialize_aws_json_1_1(
                data["CapacityType"]
            )
        )
    if "NetworkInterface" in data:
        import capo_sagemaker.types.cluster_network_interface_details

        out["network_interface"] = (
            capo_sagemaker.types.cluster_network_interface_details.deserialize_aws_json_1_1(
                data["NetworkInterface"]
            )
        )
    return out
