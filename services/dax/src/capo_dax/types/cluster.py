"""Generated from Smithy shape ``com.amazonaws.dax#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.cluster_endpoint_encryption_type
    import capo_dax.types.endpoint
    import capo_dax.types.integer_optional
    import capo_dax.types.network_type
    import capo_dax.types.node_identifier_list
    import capo_dax.types.node_list
    import capo_dax.types.notification_configuration
    import capo_dax.types.parameter_group_status
    import capo_dax.types.security_group_membership_list
    import capo_dax.types.sse_description
    import capo_dax.types.string


class Cluster(TypedDict, closed=True):
    cluster_name: NotRequired["capo_dax.types.string.String"]
    """<p>The name of the DAX cluster.</p>"""
    description: NotRequired["capo_dax.types.string.String"]
    """<p>The description of the cluster.</p>"""
    cluster_arn: NotRequired["capo_dax.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster. </p>"""
    total_nodes: NotRequired["capo_dax.types.integer_optional.IntegerOptional"]
    """<p>The total number of nodes in the cluster.</p>"""
    active_nodes: NotRequired["capo_dax.types.integer_optional.IntegerOptional"]
    """<p>The number of nodes in the cluster that are active (i.e., capable of serving requests).</p>"""
    node_type: NotRequired["capo_dax.types.string.String"]
    """<p>The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)</p>"""
    status: NotRequired["capo_dax.types.string.String"]
    """<p>The current status of the cluster.</p>"""
    cluster_discovery_endpoint: NotRequired["capo_dax.types.endpoint.Endpoint"]
    """<p>The endpoint for this DAX cluster, consisting of a DNS name, a port number, and a URL. Applications should use the URL to configure the DAX client to find their cluster.</p>"""
    node_ids_to_remove: NotRequired[
        "capo_dax.types.node_identifier_list.NodeIdentifierList"
    ]
    """<p>A list of nodes to be removed from the cluster.</p>"""
    nodes: NotRequired["capo_dax.types.node_list.NodeList"]
    """<p>A list of nodes that are currently in the cluster.</p>"""
    preferred_maintenance_window: NotRequired["capo_dax.types.string.String"]
    """<p>A range of time when maintenance of DAX cluster software will be performed. For example: <code>sun:01:00-sun:09:00</code>. Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.</p>"""
    notification_configuration: NotRequired[
        "capo_dax.types.notification_configuration.NotificationConfiguration"
    ]
    """<p>Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).</p>"""
    subnet_group: NotRequired["capo_dax.types.string.String"]
    """<p>The subnet group where the DAX cluster is running.</p>"""
    security_groups: NotRequired[
        "capo_dax.types.security_group_membership_list.SecurityGroupMembershipList"
    ]
    """<p>A list of security groups, and the status of each, for the nodes in the cluster.</p>"""
    iam_role_arn: NotRequired["capo_dax.types.string.String"]
    """<p>A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.</p>"""
    parameter_group: NotRequired[
        "capo_dax.types.parameter_group_status.ParameterGroupStatus"
    ]
    """<p>The parameter group being used by nodes in the cluster.</p>"""
    sse_description: NotRequired["capo_dax.types.sse_description.SSEDescription"]
    """<p>The description of the server-side encryption status on the specified DAX cluster.</p>"""
    cluster_endpoint_encryption_type: NotRequired[
        "capo_dax.types.cluster_endpoint_encryption_type.ClusterEndpointEncryptionType"
    ]
    """<p>The type of encryption supported by the cluster's endpoint. Values are:</p> <ul> <li> <p> <code>NONE</code> for no encryption</p> <p> <code>TLS</code> for Transport Layer Security</p> </li> </ul>"""
    network_type: NotRequired["capo_dax.types.network_type.NetworkType"]
    """<p>The IP address type of the cluster. Values are:</p> <ul> <li> <p> <code>ipv4</code> - IPv4 addresses only</p> </li> <li> <p> <code>ipv6</code> - IPv6 addresses only</p> </li> <li> <p> <code>dual_stack</code> - Both IPv4 and IPv6 addresses</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Cluster) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "total_nodes" in value:
        out["TotalNodes"] = value["total_nodes"]
    if "active_nodes" in value:
        out["ActiveNodes"] = value["active_nodes"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "status" in value:
        out["Status"] = value["status"]
    if "cluster_discovery_endpoint" in value:
        import capo_dax.types.endpoint

        out["ClusterDiscoveryEndpoint"] = (
            capo_dax.types.endpoint.serialize_aws_json_1_1(
                value["cluster_discovery_endpoint"]
            )
        )
    if "node_ids_to_remove" in value:
        import capo_dax.types.node_identifier_list

        out["NodeIdsToRemove"] = (
            capo_dax.types.node_identifier_list.serialize_aws_json_1_1(
                value["node_ids_to_remove"]
            )
        )
    if "nodes" in value:
        import capo_dax.types.node_list

        out["Nodes"] = capo_dax.types.node_list.serialize_aws_json_1_1(value["nodes"])
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "notification_configuration" in value:
        import capo_dax.types.notification_configuration

        out["NotificationConfiguration"] = (
            capo_dax.types.notification_configuration.serialize_aws_json_1_1(
                value["notification_configuration"]
            )
        )
    if "subnet_group" in value:
        out["SubnetGroup"] = value["subnet_group"]
    if "security_groups" in value:
        import capo_dax.types.security_group_membership_list

        out["SecurityGroups"] = (
            capo_dax.types.security_group_membership_list.serialize_aws_json_1_1(
                value["security_groups"]
            )
        )
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "parameter_group" in value:
        import capo_dax.types.parameter_group_status

        out["ParameterGroup"] = (
            capo_dax.types.parameter_group_status.serialize_aws_json_1_1(
                value["parameter_group"]
            )
        )
    if "sse_description" in value:
        import capo_dax.types.sse_description

        out["SSEDescription"] = capo_dax.types.sse_description.serialize_aws_json_1_1(
            value["sse_description"]
        )
    if "cluster_endpoint_encryption_type" in value:
        import capo_dax.types.cluster_endpoint_encryption_type

        out["ClusterEndpointEncryptionType"] = (
            capo_dax.types.cluster_endpoint_encryption_type.serialize_aws_json_1_1(
                value["cluster_endpoint_encryption_type"]
            )
        )
    if "network_type" in value:
        import capo_dax.types.network_type

        out["NetworkType"] = capo_dax.types.network_type.serialize_aws_json_1_1(
            value["network_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "TotalNodes" in data:
        out["total_nodes"] = data["TotalNodes"]
    if "ActiveNodes" in data:
        out["active_nodes"] = data["ActiveNodes"]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "ClusterDiscoveryEndpoint" in data:
        import capo_dax.types.endpoint

        out["cluster_discovery_endpoint"] = (
            capo_dax.types.endpoint.deserialize_aws_json_1_1(
                data["ClusterDiscoveryEndpoint"]
            )
        )
    if "NodeIdsToRemove" in data:
        import capo_dax.types.node_identifier_list

        out["node_ids_to_remove"] = (
            capo_dax.types.node_identifier_list.deserialize_aws_json_1_1(
                data["NodeIdsToRemove"]
            )
        )
    if "Nodes" in data:
        import capo_dax.types.node_list

        out["nodes"] = capo_dax.types.node_list.deserialize_aws_json_1_1(data["Nodes"])
    if "PreferredMaintenanceWindow" in data:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if "NotificationConfiguration" in data:
        import capo_dax.types.notification_configuration

        out["notification_configuration"] = (
            capo_dax.types.notification_configuration.deserialize_aws_json_1_1(
                data["NotificationConfiguration"]
            )
        )
    if "SubnetGroup" in data:
        out["subnet_group"] = data["SubnetGroup"]
    if "SecurityGroups" in data:
        import capo_dax.types.security_group_membership_list

        out["security_groups"] = (
            capo_dax.types.security_group_membership_list.deserialize_aws_json_1_1(
                data["SecurityGroups"]
            )
        )
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    if "ParameterGroup" in data:
        import capo_dax.types.parameter_group_status

        out["parameter_group"] = (
            capo_dax.types.parameter_group_status.deserialize_aws_json_1_1(
                data["ParameterGroup"]
            )
        )
    if "SSEDescription" in data:
        import capo_dax.types.sse_description

        out["sse_description"] = (
            capo_dax.types.sse_description.deserialize_aws_json_1_1(
                data["SSEDescription"]
            )
        )
    if "ClusterEndpointEncryptionType" in data:
        import capo_dax.types.cluster_endpoint_encryption_type

        out["cluster_endpoint_encryption_type"] = (
            capo_dax.types.cluster_endpoint_encryption_type.deserialize_aws_json_1_1(
                data["ClusterEndpointEncryptionType"]
            )
        )
    if "NetworkType" in data:
        import capo_dax.types.network_type

        out["network_type"] = capo_dax.types.network_type.deserialize_aws_json_1_1(
            data["NetworkType"]
        )
    return out
