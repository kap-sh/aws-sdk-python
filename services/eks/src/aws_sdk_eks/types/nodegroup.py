"""Generated from Smithy shape ``com.amazonaws.eks#Nodegroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.ami_types
    import aws_sdk_eks.types.boxed_integer
    import aws_sdk_eks.types.capacity_types
    import aws_sdk_eks.types.labels_map
    import aws_sdk_eks.types.launch_template_specification
    import aws_sdk_eks.types.node_repair_config
    import aws_sdk_eks.types.nodegroup_health
    import aws_sdk_eks.types.nodegroup_resources
    import aws_sdk_eks.types.nodegroup_scaling_config
    import aws_sdk_eks.types.nodegroup_status
    import aws_sdk_eks.types.nodegroup_update_config
    import aws_sdk_eks.types.remote_access_config
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list
    import aws_sdk_eks.types.tag_map
    import aws_sdk_eks.types.taints_list
    import aws_sdk_eks.types.timestamp
    import aws_sdk_eks.types.warm_pool_config


class Nodegroup(TypedDict):
    nodegroup_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name associated with an Amazon EKS managed node group.</p>"""
    nodegroup_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) associated with the managed node group.</p>"""
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of your cluster.</p>"""
    version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Kubernetes version of the managed node group.</p>"""
    release_version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>If the node group was deployed using a launch template with a custom AMI, then this is the AMI ID that was specified in the launch template. For node groups that weren't deployed using a launch template, this is the version of the Amazon EKS optimized AMI that the node group was deployed with.</p>"""
    created_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp at object creation.</p>"""
    modified_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp for the last modification to the object.</p>"""
    status: NotRequired["aws_sdk_eks.types.nodegroup_status.NodegroupStatus"]
    """<p>The current status of the managed node group.</p>"""
    capacity_type: NotRequired["aws_sdk_eks.types.capacity_types.CapacityTypes"]
    """<p>The capacity type of your managed node group.</p>"""
    scaling_config: NotRequired[
        "aws_sdk_eks.types.nodegroup_scaling_config.NodegroupScalingConfig"
    ]
    """<p>The scaling configuration details for the Auto Scaling group that is associated with your node group.</p>"""
    instance_types: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>If the node group wasn't deployed with a launch template, then this is the instance type that is associated with the node group. If the node group was deployed with a launch template, then this is <code>null</code>.</p>"""
    subnets: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The subnets that were specified for the Auto Scaling group that is associated with your node group.</p>"""
    remote_access: NotRequired[
        "aws_sdk_eks.types.remote_access_config.RemoteAccessConfig"
    ]
    """<p>If the node group wasn't deployed with a launch template, then this is the remote access configuration that is associated with the node group. If the node group was deployed with a launch template, then this is <code>null</code>.</p>"""
    ami_type: NotRequired["aws_sdk_eks.types.ami_types.AMITypes"]
    """<p>If the node group was deployed using a launch template with a custom AMI, then this is <code>CUSTOM</code>. For node groups that weren't deployed using a launch template, this is the AMI type that was specified in the node group configuration.</p>"""
    node_role: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The IAM role associated with your node group. The Amazon EKS node <code>kubelet</code> daemon makes calls to Amazon Web Services APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies.</p>"""
    labels: NotRequired["aws_sdk_eks.types.labels_map.labelsMap"]
    """<p>The Kubernetes <code>labels</code> applied to the nodes in the node group.</p> <note> <p>Only <code>labels</code> that are applied with the Amazon EKS API are shown here. There may be other Kubernetes <code>labels</code> applied to the nodes in this group.</p> </note>"""
    taints: NotRequired["aws_sdk_eks.types.taints_list.taintsList"]
    """<p>The Kubernetes taints to be applied to the nodes in the node group when they are created. Effect is one of <code>No_Schedule</code>, <code>Prefer_No_Schedule</code>, or <code>No_Execute</code>. Kubernetes taints can be used together with tolerations to control how workloads are scheduled to your nodes. For more information, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html\">Node taints on managed node groups</a>.</p>"""
    resources: NotRequired["aws_sdk_eks.types.nodegroup_resources.NodegroupResources"]
    """<p>The resources associated with the node group, such as Auto Scaling groups and security groups for remote access.</p>"""
    disk_size: NotRequired["aws_sdk_eks.types.boxed_integer.BoxedInteger"]
    """<p>If the node group wasn't deployed with a launch template, then this is the disk size in the node group configuration. If the node group was deployed with a launch template, then this is <code>null</code>.</p>"""
    health: NotRequired["aws_sdk_eks.types.nodegroup_health.NodegroupHealth"]
    """<p>The health status of the node group. If there are issues with your node group's health, they are listed here.</p>"""
    update_config: NotRequired[
        "aws_sdk_eks.types.nodegroup_update_config.NodegroupUpdateConfig"
    ]
    """<p>The node group update configuration.</p>"""
    node_repair_config: NotRequired[
        "aws_sdk_eks.types.node_repair_config.NodeRepairConfig"
    ]
    """<p>The node auto repair configuration for the node group.</p>"""
    launch_template: NotRequired[
        "aws_sdk_eks.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>If a launch template was used to create the node group, then this is the launch template that was used.</p>"""
    tags: NotRequired["aws_sdk_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    warm_pool_config: NotRequired["aws_sdk_eks.types.warm_pool_config.WarmPoolConfig"]
    """<p>The warm pool configuration attached to the node group. Amazon EKS manages warm pools throughout the node group lifecycle using the <code>AWSServiceRoleForAmazonEKSNodegroup</code> service-linked role to create, update, and delete warm pool resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Nodegroup) -> dict:
    out: dict = {}
    if "nodegroup_name" in value:
        out["nodegroupName"] = value["nodegroup_name"]
    if "nodegroup_arn" in value:
        out["nodegroupArn"] = value["nodegroup_arn"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "version" in value:
        out["version"] = value["version"]
    if "release_version" in value:
        out["releaseVersion"] = value["release_version"]
    if "created_at" in value:
        import aws_sdk_eks.types.timestamp

        out["createdAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "modified_at" in value:
        import aws_sdk_eks.types.timestamp

        out["modifiedAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["modified_at"]
        )
    if "status" in value:
        import aws_sdk_eks.types.nodegroup_status

        out["status"] = aws_sdk_eks.types.nodegroup_status.serialize_json(
            value["status"]
        )
    if "capacity_type" in value:
        import aws_sdk_eks.types.capacity_types

        out["capacityType"] = aws_sdk_eks.types.capacity_types.serialize_json(
            value["capacity_type"]
        )
    if "scaling_config" in value:
        import aws_sdk_eks.types.nodegroup_scaling_config

        out["scalingConfig"] = (
            aws_sdk_eks.types.nodegroup_scaling_config.serialize_json(
                value["scaling_config"]
            )
        )
    if "instance_types" in value:
        import aws_sdk_eks.types.string_list

        out["instanceTypes"] = aws_sdk_eks.types.string_list.serialize_json(
            value["instance_types"]
        )
    if "subnets" in value:
        import aws_sdk_eks.types.string_list

        out["subnets"] = aws_sdk_eks.types.string_list.serialize_json(value["subnets"])
    if "remote_access" in value:
        import aws_sdk_eks.types.remote_access_config

        out["remoteAccess"] = aws_sdk_eks.types.remote_access_config.serialize_json(
            value["remote_access"]
        )
    if "ami_type" in value:
        import aws_sdk_eks.types.ami_types

        out["amiType"] = aws_sdk_eks.types.ami_types.serialize_json(value["ami_type"])
    if "node_role" in value:
        out["nodeRole"] = value["node_role"]
    if "labels" in value:
        import aws_sdk_eks.types.labels_map

        out["labels"] = aws_sdk_eks.types.labels_map.serialize_json(value["labels"])
    if "taints" in value:
        import aws_sdk_eks.types.taints_list

        out["taints"] = aws_sdk_eks.types.taints_list.serialize_json(value["taints"])
    if "resources" in value:
        import aws_sdk_eks.types.nodegroup_resources

        out["resources"] = aws_sdk_eks.types.nodegroup_resources.serialize_json(
            value["resources"]
        )
    if "disk_size" in value:
        out["diskSize"] = value["disk_size"]
    if "health" in value:
        import aws_sdk_eks.types.nodegroup_health

        out["health"] = aws_sdk_eks.types.nodegroup_health.serialize_json(
            value["health"]
        )
    if "update_config" in value:
        import aws_sdk_eks.types.nodegroup_update_config

        out["updateConfig"] = aws_sdk_eks.types.nodegroup_update_config.serialize_json(
            value["update_config"]
        )
    if "node_repair_config" in value:
        import aws_sdk_eks.types.node_repair_config

        out["nodeRepairConfig"] = aws_sdk_eks.types.node_repair_config.serialize_json(
            value["node_repair_config"]
        )
    if "launch_template" in value:
        import aws_sdk_eks.types.launch_template_specification

        out["launchTemplate"] = (
            aws_sdk_eks.types.launch_template_specification.serialize_json(
                value["launch_template"]
            )
        )
    if "tags" in value:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    if "warm_pool_config" in value:
        import aws_sdk_eks.types.warm_pool_config

        out["warmPoolConfig"] = aws_sdk_eks.types.warm_pool_config.serialize_json(
            value["warm_pool_config"]
        )
    return out


def deserialize_json(data: dict) -> Nodegroup:
    out: Nodegroup = {}  # type: ignore[typeddict-item]
    if "nodegroupName" in data:
        out["nodegroup_name"] = data["nodegroupName"]
    if "nodegroupArn" in data:
        out["nodegroup_arn"] = data["nodegroupArn"]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "version" in data:
        out["version"] = data["version"]
    if "releaseVersion" in data:
        out["release_version"] = data["releaseVersion"]
    if "createdAt" in data:
        import aws_sdk_eks.types.timestamp

        out["created_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "modifiedAt" in data:
        import aws_sdk_eks.types.timestamp

        out["modified_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    if "status" in data:
        import aws_sdk_eks.types.nodegroup_status

        out["status"] = aws_sdk_eks.types.nodegroup_status.deserialize_json(
            data["status"]
        )
    if "capacityType" in data:
        import aws_sdk_eks.types.capacity_types

        out["capacity_type"] = aws_sdk_eks.types.capacity_types.deserialize_json(
            data["capacityType"]
        )
    if "scalingConfig" in data:
        import aws_sdk_eks.types.nodegroup_scaling_config

        out["scaling_config"] = (
            aws_sdk_eks.types.nodegroup_scaling_config.deserialize_json(
                data["scalingConfig"]
            )
        )
    if "instanceTypes" in data:
        import aws_sdk_eks.types.string_list

        out["instance_types"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["instanceTypes"]
        )
    if "subnets" in data:
        import aws_sdk_eks.types.string_list

        out["subnets"] = aws_sdk_eks.types.string_list.deserialize_json(data["subnets"])
    if "remoteAccess" in data:
        import aws_sdk_eks.types.remote_access_config

        out["remote_access"] = aws_sdk_eks.types.remote_access_config.deserialize_json(
            data["remoteAccess"]
        )
    if "amiType" in data:
        import aws_sdk_eks.types.ami_types

        out["ami_type"] = aws_sdk_eks.types.ami_types.deserialize_json(data["amiType"])
    if "nodeRole" in data:
        out["node_role"] = data["nodeRole"]
    if "labels" in data:
        import aws_sdk_eks.types.labels_map

        out["labels"] = aws_sdk_eks.types.labels_map.deserialize_json(data["labels"])
    if "taints" in data:
        import aws_sdk_eks.types.taints_list

        out["taints"] = aws_sdk_eks.types.taints_list.deserialize_json(data["taints"])
    if "resources" in data:
        import aws_sdk_eks.types.nodegroup_resources

        out["resources"] = aws_sdk_eks.types.nodegroup_resources.deserialize_json(
            data["resources"]
        )
    if "diskSize" in data:
        out["disk_size"] = data["diskSize"]
    if "health" in data:
        import aws_sdk_eks.types.nodegroup_health

        out["health"] = aws_sdk_eks.types.nodegroup_health.deserialize_json(
            data["health"]
        )
    if "updateConfig" in data:
        import aws_sdk_eks.types.nodegroup_update_config

        out["update_config"] = (
            aws_sdk_eks.types.nodegroup_update_config.deserialize_json(
                data["updateConfig"]
            )
        )
    if "nodeRepairConfig" in data:
        import aws_sdk_eks.types.node_repair_config

        out["node_repair_config"] = (
            aws_sdk_eks.types.node_repair_config.deserialize_json(
                data["nodeRepairConfig"]
            )
        )
    if "launchTemplate" in data:
        import aws_sdk_eks.types.launch_template_specification

        out["launch_template"] = (
            aws_sdk_eks.types.launch_template_specification.deserialize_json(
                data["launchTemplate"]
            )
        )
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    if "warmPoolConfig" in data:
        import aws_sdk_eks.types.warm_pool_config

        out["warm_pool_config"] = aws_sdk_eks.types.warm_pool_config.deserialize_json(
            data["warmPoolConfig"]
        )
    return out
