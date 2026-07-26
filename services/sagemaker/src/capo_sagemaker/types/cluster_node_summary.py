"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNodeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_image_version_status
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.cluster_instance_status_details
    import capo_sagemaker.types.cluster_instance_type
    import capo_sagemaker.types.cluster_private_dns_hostname
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.ultra_server_info


class ClusterNodeSummary(TypedDict, closed=True):
    instance_group_name: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>The name of the instance group in which the instance is.</p>"""
    instance_id: NotRequired["str"]
    """<p>The ID of the instance.</p>"""
    node_logical_id: NotRequired["str"]
    """<p>A unique identifier for the node that persists throughout its lifecycle, from provisioning request to termination. This identifier can be used to track the node even before it has an assigned <code>InstanceId</code>. This field is only included when <code>IncludeNodeLogicalIds</code> is set to <code>True</code> in the <code>ListClusterNodes</code> request.</p>"""
    instance_type: NotRequired[
        "capo_sagemaker.types.cluster_instance_type.ClusterInstanceType"
    ]
    """<p>The type of the instance.</p>"""
    launch_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the instance is launched.</p>"""
    last_software_update_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when SageMaker last updated the software of the instances in the cluster.</p>"""
    instance_status: NotRequired[
        "capo_sagemaker.types.cluster_instance_status_details.ClusterInstanceStatusDetails"
    ]
    """<p>The status of the instance.</p>"""
    ultra_server_info: NotRequired[
        "capo_sagemaker.types.ultra_server_info.UltraServerInfo"
    ]
    """<p>Contains information about the UltraServer.</p>"""
    private_dns_hostname: NotRequired[
        "capo_sagemaker.types.cluster_private_dns_hostname.ClusterPrivateDnsHostname"
    ]
    """<p>The private DNS hostname of the SageMaker HyperPod cluster node.</p>"""
    image_version_status: NotRequired[
        "capo_sagemaker.types.cluster_image_version_status.ClusterImageVersionStatus"
    ]
    """<p>The status of the image version for the cluster node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNodeSummary) -> dict:
    out: dict = {}
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "node_logical_id" in value:
        out["NodeLogicalId"] = value["node_logical_id"]
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
    if "instance_status" in value:
        import capo_sagemaker.types.cluster_instance_status_details

        out["InstanceStatus"] = (
            capo_sagemaker.types.cluster_instance_status_details.serialize_aws_json_1_1(
                value["instance_status"]
            )
        )
    if "ultra_server_info" in value:
        import capo_sagemaker.types.ultra_server_info

        out["UltraServerInfo"] = (
            capo_sagemaker.types.ultra_server_info.serialize_aws_json_1_1(
                value["ultra_server_info"]
            )
        )
    if "private_dns_hostname" in value:
        out["PrivateDnsHostname"] = value["private_dns_hostname"]
    if "image_version_status" in value:
        import capo_sagemaker.types.cluster_image_version_status

        out["ImageVersionStatus"] = (
            capo_sagemaker.types.cluster_image_version_status.serialize_aws_json_1_1(
                value["image_version_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterNodeSummary:
    out: ClusterNodeSummary = {}  # type: ignore[typeddict-item]
    if "InstanceGroupName" in data:
        out["instance_group_name"] = data["InstanceGroupName"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "NodeLogicalId" in data:
        out["node_logical_id"] = data["NodeLogicalId"]
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
    if "InstanceStatus" in data:
        import capo_sagemaker.types.cluster_instance_status_details

        out["instance_status"] = (
            capo_sagemaker.types.cluster_instance_status_details.deserialize_aws_json_1_1(
                data["InstanceStatus"]
            )
        )
    if "UltraServerInfo" in data:
        import capo_sagemaker.types.ultra_server_info

        out["ultra_server_info"] = (
            capo_sagemaker.types.ultra_server_info.deserialize_aws_json_1_1(
                data["UltraServerInfo"]
            )
        )
    if "PrivateDnsHostname" in data:
        out["private_dns_hostname"] = data["PrivateDnsHostname"]
    if "ImageVersionStatus" in data:
        import capo_sagemaker.types.cluster_image_version_status

        out["image_version_status"] = (
            capo_sagemaker.types.cluster_image_version_status.deserialize_aws_json_1_1(
                data["ImageVersionStatus"]
            )
        )
    return out
