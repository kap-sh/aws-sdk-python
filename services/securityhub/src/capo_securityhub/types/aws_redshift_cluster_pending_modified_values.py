"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterPendingModifiedValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsRedshiftClusterPendingModifiedValues(TypedDict, closed=True):
    automated_snapshot_retention_period: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The pending or in-progress change to the automated snapshot retention period.</p>"""
    cluster_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The pending or in-progress change to the identifier for the cluster.</p>"""
    cluster_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The pending or in-progress change to the cluster type.</p>"""
    cluster_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The pending or in-progress change to the service version.</p>"""
    encryption_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The encryption type for a cluster.</p>"""
    enhanced_vpc_routing: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether to create the cluster with enhanced VPC routing enabled.</p>"""
    maintenance_track_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the maintenance track that the cluster changes to during the next maintenance window.</p>"""
    master_user_password: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The pending or in-progress change to the master user password for the cluster.</p>"""
    node_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The pending or in-progress change to the cluster's node type.</p>"""
    number_of_nodes: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The pending or in-progress change to the number of nodes in the cluster.</p>"""
    publicly_accessible: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>The pending or in-progress change to whether the cluster can be connected to from the public network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterPendingModifiedValues) -> dict:
    out: dict = {}
    if "automated_snapshot_retention_period" in value:
        out["AutomatedSnapshotRetentionPeriod"] = value[
            "automated_snapshot_retention_period"
        ]
    if "cluster_identifier" in value:
        out["ClusterIdentifier"] = value["cluster_identifier"]
    if "cluster_type" in value:
        out["ClusterType"] = value["cluster_type"]
    if "cluster_version" in value:
        out["ClusterVersion"] = value["cluster_version"]
    if "encryption_type" in value:
        out["EncryptionType"] = value["encryption_type"]
    if "enhanced_vpc_routing" in value:
        out["EnhancedVpcRouting"] = value["enhanced_vpc_routing"]
    if "maintenance_track_name" in value:
        out["MaintenanceTrackName"] = value["maintenance_track_name"]
    if "master_user_password" in value:
        out["MasterUserPassword"] = value["master_user_password"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "number_of_nodes" in value:
        out["NumberOfNodes"] = value["number_of_nodes"]
    if "publicly_accessible" in value:
        out["PubliclyAccessible"] = value["publicly_accessible"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterPendingModifiedValues:
    out: AwsRedshiftClusterPendingModifiedValues = {}  # type: ignore[typeddict-item]
    if "AutomatedSnapshotRetentionPeriod" in data:
        out["automated_snapshot_retention_period"] = data[
            "AutomatedSnapshotRetentionPeriod"
        ]
    if "ClusterIdentifier" in data:
        out["cluster_identifier"] = data["ClusterIdentifier"]
    if "ClusterType" in data:
        out["cluster_type"] = data["ClusterType"]
    if "ClusterVersion" in data:
        out["cluster_version"] = data["ClusterVersion"]
    if "EncryptionType" in data:
        out["encryption_type"] = data["EncryptionType"]
    if "EnhancedVpcRouting" in data:
        out["enhanced_vpc_routing"] = data["EnhancedVpcRouting"]
    if "MaintenanceTrackName" in data:
        out["maintenance_track_name"] = data["MaintenanceTrackName"]
    if "MasterUserPassword" in data:
        out["master_user_password"] = data["MasterUserPassword"]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "NumberOfNodes" in data:
        out["number_of_nodes"] = data["NumberOfNodes"]
    if "PubliclyAccessible" in data:
        out["publicly_accessible"] = data["PubliclyAccessible"]
    return out
