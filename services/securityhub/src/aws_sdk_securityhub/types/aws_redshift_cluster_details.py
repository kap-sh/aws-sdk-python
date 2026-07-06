"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_nodes
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_groups
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_security_groups
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_snapshot_copy_status
    import aws_sdk_securityhub.types.aws_redshift_cluster_deferred_maintenance_windows
    import aws_sdk_securityhub.types.aws_redshift_cluster_elastic_ip_status
    import aws_sdk_securityhub.types.aws_redshift_cluster_endpoint
    import aws_sdk_securityhub.types.aws_redshift_cluster_hsm_status
    import aws_sdk_securityhub.types.aws_redshift_cluster_iam_roles
    import aws_sdk_securityhub.types.aws_redshift_cluster_logging_status
    import aws_sdk_securityhub.types.aws_redshift_cluster_pending_modified_values
    import aws_sdk_securityhub.types.aws_redshift_cluster_resize_info
    import aws_sdk_securityhub.types.aws_redshift_cluster_restore_status
    import aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_groups
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class AwsRedshiftClusterDetails(TypedDict, closed=True):
    allow_version_upgrade: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether major version upgrades are applied automatically to the cluster during the maintenance window.</p>"""
    automated_snapshot_retention_period: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>The number of days that automatic cluster snapshots are retained.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the Availability Zone in which the cluster is located.</p>"""
    cluster_availability_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The availability status of the cluster for queries. Possible values are the following:</p> <ul> <li> <p> <code>Available</code> - The cluster is available for queries.</p> </li> <li> <p> <code>Unavailable</code> - The cluster is not available for queries.</p> </li> <li> <p> <code>Maintenance</code> - The cluster is intermittently available for queries due to maintenance activities.</p> </li> <li> <p> <code>Modifying</code> -The cluster is intermittently available for queries due to changes that modify the cluster.</p> </li> <li> <p> <code>Failed</code> - The cluster failed and is not available for queries.</p> </li> </ul>"""
    cluster_create_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the cluster was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    cluster_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The unique identifier of the cluster.</p>"""
    cluster_nodes: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_cluster_nodes.AwsRedshiftClusterClusterNodes"
    ]
    """<p>The nodes in the cluster.</p>"""
    cluster_parameter_groups: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_groups.AwsRedshiftClusterClusterParameterGroups"
    ]
    """<p>The list of cluster parameter groups that are associated with this cluster.</p>"""
    cluster_public_key: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The public key for the cluster.</p>"""
    cluster_revision_number: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The specific revision number of the database in the cluster.</p>"""
    cluster_security_groups: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_cluster_security_groups.AwsRedshiftClusterClusterSecurityGroups"
    ]
    """<p>A list of cluster security groups that are associated with the cluster.</p>"""
    cluster_snapshot_copy_status: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_cluster_snapshot_copy_status.AwsRedshiftClusterClusterSnapshotCopyStatus"
    ]
    """<p>Information about the destination Region and retention period for the cross-Region snapshot copy.</p>"""
    cluster_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The current status of the cluster.</p> <p>Valid values: <code>available</code> | <code>available, prep-for-resize</code> | <code>available, resize-cleanup</code> |<code> cancelling-resize</code> | <code>creating</code> | <code>deleting</code> | <code>final-snapshot</code> | <code>hardware-failure</code> | <code>incompatible-hsm</code> |<code> incompatible-network</code> | <code>incompatible-parameters</code> | <code>incompatible-restore</code> | <code>modifying</code> | <code>paused</code> | <code>rebooting</code> | <code>renaming</code> | <code>resizing</code> | <code>rotating-keys</code> | <code>storage-full</code> | <code>updating-hsm</code> </p>"""
    cluster_subnet_group_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.</p>"""
    cluster_version: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version ID of the Amazon Redshift engine that runs on the cluster.</p>"""
    db_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the initial database that was created when the cluster was created.</p> <p>The same name is returned for the life of the cluster.</p> <p>If an initial database is not specified, a database named <code>devdev</code> is created by default.</p>"""
    deferred_maintenance_windows: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_deferred_maintenance_windows.AwsRedshiftClusterDeferredMaintenanceWindows"
    ]
    """<p>List of time windows during which maintenance was deferred.</p>"""
    elastic_ip_status: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_elastic_ip_status.AwsRedshiftClusterElasticIpStatus"
    ]
    """<p>Information about the status of the Elastic IP (EIP) address.</p>"""
    elastic_resize_number_of_node_options: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The number of nodes that you can use the elastic resize method to resize the cluster to.</p>"""
    encrypted: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the data in the cluster is encrypted at rest.</p>"""
    endpoint: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_endpoint.AwsRedshiftClusterEndpoint"
    ]
    """<p>The connection endpoint.</p>"""
    enhanced_vpc_routing: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether to create the cluster with enhanced VPC routing enabled.</p>"""
    expected_next_snapshot_schedule_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the next snapshot is expected to be taken. The cluster must have a valid snapshot schedule and have backups enabled.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    expected_next_snapshot_schedule_time_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the next expected snapshot.</p> <p>Valid values: <code>OnTrack</code> | <code>Pending</code> </p>"""
    hsm_status: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_hsm_status.AwsRedshiftClusterHsmStatus"
    ]
    """<p>Information about whether the Amazon Redshift cluster finished applying any changes to hardware security module (HSM) settings that were specified in a modify cluster command.</p>"""
    iam_roles: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_iam_roles.AwsRedshiftClusterIamRoles"
    ]
    """<p>A list of IAM roles that the cluster can use to access other Amazon Web Services services.</p>"""
    kms_key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the KMS encryption key that is used to encrypt data in the cluster.</p>"""
    maintenance_track_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the maintenance track for the cluster.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>The default number of days to retain a manual snapshot.</p> <p>If the value is <code>-1</code>, the snapshot is retained indefinitely.</p> <p>This setting doesn't change the retention period of existing snapshots.</p> <p>Valid values: Either <code>-1</code> or an integer between 1 and 3,653</p>"""
    master_username: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The master user name for the cluster. This name is used to connect to the database that is specified in as the value of <code>DBName</code>.</p>"""
    next_maintenance_window_start_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates the start of the next maintenance window.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    node_type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The node type for the nodes in the cluster.</p>"""
    number_of_nodes: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of compute nodes in the cluster.</p>"""
    pending_actions: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>A list of cluster operations that are waiting to start.</p>"""
    pending_modified_values: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_pending_modified_values.AwsRedshiftClusterPendingModifiedValues"
    ]
    """<p>A list of changes to the cluster that are currently pending.</p>"""
    preferred_maintenance_window: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.</p> <p>Format: <code> <i><day></i>:HH:MM-<i><day></i>:HH:MM</code> </p> <p>For the day values, use <code>mon</code> | <code>tue</code> | <code>wed</code> | <code>thu</code> | <code>fri</code> | <code>sat</code> | <code>sun</code> </p> <p>For example, <code>sun:09:32-sun:10:02</code> </p>"""
    publicly_accessible: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the cluster can be accessed from a public network.</p>"""
    resize_info: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_resize_info.AwsRedshiftClusterResizeInfo"
    ]
    """<p>Information about the resize operation for the cluster.</p>"""
    restore_status: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_restore_status.AwsRedshiftClusterRestoreStatus"
    ]
    """<p>Information about the status of a cluster restore action. Only applies to a cluster that was created by restoring a snapshot.</p>"""
    snapshot_schedule_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A unique identifier for the cluster snapshot schedule.</p>"""
    snapshot_schedule_state: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The current state of the cluster snapshot schedule.</p> <p>Valid values: <code>MODIFYING</code> | <code>ACTIVE</code> | <code>FAILED</code> </p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the VPC that the cluster is in, if the cluster is in a VPC.</p>"""
    vpc_security_groups: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_groups.AwsRedshiftClusterVpcSecurityGroups"
    ]
    """<p>The list of VPC security groups that the cluster belongs to, if the cluster is in a VPC.</p>"""
    logging_status: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_logging_status.AwsRedshiftClusterLoggingStatus"
    ]
    """<p>Information about the logging status of the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterDetails) -> dict:
    out: dict = {}
    if "allow_version_upgrade" in value:
        out["AllowVersionUpgrade"] = value["allow_version_upgrade"]
    if "automated_snapshot_retention_period" in value:
        out["AutomatedSnapshotRetentionPeriod"] = value[
            "automated_snapshot_retention_period"
        ]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "cluster_availability_status" in value:
        out["ClusterAvailabilityStatus"] = value["cluster_availability_status"]
    if "cluster_create_time" in value:
        out["ClusterCreateTime"] = value["cluster_create_time"]
    if "cluster_identifier" in value:
        out["ClusterIdentifier"] = value["cluster_identifier"]
    if "cluster_nodes" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_nodes

        out["ClusterNodes"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_nodes.serialize_json(
                value["cluster_nodes"]
            )
        )
    if "cluster_parameter_groups" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_groups

        out["ClusterParameterGroups"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_groups.serialize_json(
                value["cluster_parameter_groups"]
            )
        )
    if "cluster_public_key" in value:
        out["ClusterPublicKey"] = value["cluster_public_key"]
    if "cluster_revision_number" in value:
        out["ClusterRevisionNumber"] = value["cluster_revision_number"]
    if "cluster_security_groups" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_security_groups

        out["ClusterSecurityGroups"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_security_groups.serialize_json(
                value["cluster_security_groups"]
            )
        )
    if "cluster_snapshot_copy_status" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_snapshot_copy_status

        out["ClusterSnapshotCopyStatus"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_snapshot_copy_status.serialize_json(
                value["cluster_snapshot_copy_status"]
            )
        )
    if "cluster_status" in value:
        out["ClusterStatus"] = value["cluster_status"]
    if "cluster_subnet_group_name" in value:
        out["ClusterSubnetGroupName"] = value["cluster_subnet_group_name"]
    if "cluster_version" in value:
        out["ClusterVersion"] = value["cluster_version"]
    if "db_name" in value:
        out["DBName"] = value["db_name"]
    if "deferred_maintenance_windows" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_deferred_maintenance_windows

        out["DeferredMaintenanceWindows"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_deferred_maintenance_windows.serialize_json(
                value["deferred_maintenance_windows"]
            )
        )
    if "elastic_ip_status" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_elastic_ip_status

        out["ElasticIpStatus"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_elastic_ip_status.serialize_json(
                value["elastic_ip_status"]
            )
        )
    if "elastic_resize_number_of_node_options" in value:
        out["ElasticResizeNumberOfNodeOptions"] = value[
            "elastic_resize_number_of_node_options"
        ]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "endpoint" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_endpoint

        out["Endpoint"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_endpoint.serialize_json(
                value["endpoint"]
            )
        )
    if "enhanced_vpc_routing" in value:
        out["EnhancedVpcRouting"] = value["enhanced_vpc_routing"]
    if "expected_next_snapshot_schedule_time" in value:
        out["ExpectedNextSnapshotScheduleTime"] = value[
            "expected_next_snapshot_schedule_time"
        ]
    if "expected_next_snapshot_schedule_time_status" in value:
        out["ExpectedNextSnapshotScheduleTimeStatus"] = value[
            "expected_next_snapshot_schedule_time_status"
        ]
    if "hsm_status" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_hsm_status

        out["HsmStatus"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_hsm_status.serialize_json(
                value["hsm_status"]
            )
        )
    if "iam_roles" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_iam_roles

        out["IamRoles"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_iam_roles.serialize_json(
                value["iam_roles"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "maintenance_track_name" in value:
        out["MaintenanceTrackName"] = value["maintenance_track_name"]
    if "manual_snapshot_retention_period" in value:
        out["ManualSnapshotRetentionPeriod"] = value["manual_snapshot_retention_period"]
    if "master_username" in value:
        out["MasterUsername"] = value["master_username"]
    if "next_maintenance_window_start_time" in value:
        out["NextMaintenanceWindowStartTime"] = value[
            "next_maintenance_window_start_time"
        ]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "number_of_nodes" in value:
        out["NumberOfNodes"] = value["number_of_nodes"]
    if "pending_actions" in value:
        import aws_sdk_securityhub.types.string_list

        out["PendingActions"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["pending_actions"]
        )
    if "pending_modified_values" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_pending_modified_values

        out["PendingModifiedValues"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_pending_modified_values.serialize_json(
                value["pending_modified_values"]
            )
        )
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "publicly_accessible" in value:
        out["PubliclyAccessible"] = value["publicly_accessible"]
    if "resize_info" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_resize_info

        out["ResizeInfo"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_resize_info.serialize_json(
                value["resize_info"]
            )
        )
    if "restore_status" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_restore_status

        out["RestoreStatus"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_restore_status.serialize_json(
                value["restore_status"]
            )
        )
    if "snapshot_schedule_identifier" in value:
        out["SnapshotScheduleIdentifier"] = value["snapshot_schedule_identifier"]
    if "snapshot_schedule_state" in value:
        out["SnapshotScheduleState"] = value["snapshot_schedule_state"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "vpc_security_groups" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_groups

        out["VpcSecurityGroups"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_groups.serialize_json(
                value["vpc_security_groups"]
            )
        )
    if "logging_status" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_logging_status

        out["LoggingStatus"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_logging_status.serialize_json(
                value["logging_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterDetails:
    out: AwsRedshiftClusterDetails = {}  # type: ignore[typeddict-item]
    if "AllowVersionUpgrade" in data:
        out["allow_version_upgrade"] = data["AllowVersionUpgrade"]
    if "AutomatedSnapshotRetentionPeriod" in data:
        out["automated_snapshot_retention_period"] = data[
            "AutomatedSnapshotRetentionPeriod"
        ]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "ClusterAvailabilityStatus" in data:
        out["cluster_availability_status"] = data["ClusterAvailabilityStatus"]
    if "ClusterCreateTime" in data:
        out["cluster_create_time"] = data["ClusterCreateTime"]
    if "ClusterIdentifier" in data:
        out["cluster_identifier"] = data["ClusterIdentifier"]
    if "ClusterNodes" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_nodes

        out["cluster_nodes"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_nodes.deserialize_json(
                data["ClusterNodes"]
            )
        )
    if "ClusterParameterGroups" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_groups

        out["cluster_parameter_groups"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_groups.deserialize_json(
                data["ClusterParameterGroups"]
            )
        )
    if "ClusterPublicKey" in data:
        out["cluster_public_key"] = data["ClusterPublicKey"]
    if "ClusterRevisionNumber" in data:
        out["cluster_revision_number"] = data["ClusterRevisionNumber"]
    if "ClusterSecurityGroups" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_security_groups

        out["cluster_security_groups"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_security_groups.deserialize_json(
                data["ClusterSecurityGroups"]
            )
        )
    if "ClusterSnapshotCopyStatus" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_snapshot_copy_status

        out["cluster_snapshot_copy_status"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_snapshot_copy_status.deserialize_json(
                data["ClusterSnapshotCopyStatus"]
            )
        )
    if "ClusterStatus" in data:
        out["cluster_status"] = data["ClusterStatus"]
    if "ClusterSubnetGroupName" in data:
        out["cluster_subnet_group_name"] = data["ClusterSubnetGroupName"]
    if "ClusterVersion" in data:
        out["cluster_version"] = data["ClusterVersion"]
    if "DBName" in data:
        out["db_name"] = data["DBName"]
    if "DeferredMaintenanceWindows" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_deferred_maintenance_windows

        out["deferred_maintenance_windows"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_deferred_maintenance_windows.deserialize_json(
                data["DeferredMaintenanceWindows"]
            )
        )
    if "ElasticIpStatus" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_elastic_ip_status

        out["elastic_ip_status"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_elastic_ip_status.deserialize_json(
                data["ElasticIpStatus"]
            )
        )
    if "ElasticResizeNumberOfNodeOptions" in data:
        out["elastic_resize_number_of_node_options"] = data[
            "ElasticResizeNumberOfNodeOptions"
        ]
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    if "Endpoint" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_endpoint

        out["endpoint"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_endpoint.deserialize_json(
                data["Endpoint"]
            )
        )
    if "EnhancedVpcRouting" in data:
        out["enhanced_vpc_routing"] = data["EnhancedVpcRouting"]
    if "ExpectedNextSnapshotScheduleTime" in data:
        out["expected_next_snapshot_schedule_time"] = data[
            "ExpectedNextSnapshotScheduleTime"
        ]
    if "ExpectedNextSnapshotScheduleTimeStatus" in data:
        out["expected_next_snapshot_schedule_time_status"] = data[
            "ExpectedNextSnapshotScheduleTimeStatus"
        ]
    if "HsmStatus" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_hsm_status

        out["hsm_status"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_hsm_status.deserialize_json(
                data["HsmStatus"]
            )
        )
    if "IamRoles" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_iam_roles

        out["iam_roles"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_iam_roles.deserialize_json(
                data["IamRoles"]
            )
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "MaintenanceTrackName" in data:
        out["maintenance_track_name"] = data["MaintenanceTrackName"]
    if "ManualSnapshotRetentionPeriod" in data:
        out["manual_snapshot_retention_period"] = data["ManualSnapshotRetentionPeriod"]
    if "MasterUsername" in data:
        out["master_username"] = data["MasterUsername"]
    if "NextMaintenanceWindowStartTime" in data:
        out["next_maintenance_window_start_time"] = data[
            "NextMaintenanceWindowStartTime"
        ]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "NumberOfNodes" in data:
        out["number_of_nodes"] = data["NumberOfNodes"]
    if "PendingActions" in data:
        import aws_sdk_securityhub.types.string_list

        out["pending_actions"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["PendingActions"]
        )
    if "PendingModifiedValues" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_pending_modified_values

        out["pending_modified_values"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_pending_modified_values.deserialize_json(
                data["PendingModifiedValues"]
            )
        )
    if "PreferredMaintenanceWindow" in data:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if "PubliclyAccessible" in data:
        out["publicly_accessible"] = data["PubliclyAccessible"]
    if "ResizeInfo" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_resize_info

        out["resize_info"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_resize_info.deserialize_json(
                data["ResizeInfo"]
            )
        )
    if "RestoreStatus" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_restore_status

        out["restore_status"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_restore_status.deserialize_json(
                data["RestoreStatus"]
            )
        )
    if "SnapshotScheduleIdentifier" in data:
        out["snapshot_schedule_identifier"] = data["SnapshotScheduleIdentifier"]
    if "SnapshotScheduleState" in data:
        out["snapshot_schedule_state"] = data["SnapshotScheduleState"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "VpcSecurityGroups" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_groups

        out["vpc_security_groups"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_groups.deserialize_json(
                data["VpcSecurityGroups"]
            )
        )
    if "LoggingStatus" in data:
        import aws_sdk_securityhub.types.aws_redshift_cluster_logging_status

        out["logging_status"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_logging_status.deserialize_json(
                data["LoggingStatus"]
            )
        )
    return out
