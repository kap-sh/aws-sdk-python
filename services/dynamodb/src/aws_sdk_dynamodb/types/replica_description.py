"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.global_table_settings_replication_mode
    import aws_sdk_dynamodb.types.kms_master_key_id
    import aws_sdk_dynamodb.types.on_demand_throughput_override
    import aws_sdk_dynamodb.types.provisioned_throughput_override
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.replica_global_secondary_index_description_list
    import aws_sdk_dynamodb.types.replica_status
    import aws_sdk_dynamodb.types.replica_status_description
    import aws_sdk_dynamodb.types.replica_status_percent_progress
    import aws_sdk_dynamodb.types.string
    import aws_sdk_dynamodb.types.table_class_summary
    import aws_sdk_dynamodb.types.table_warm_throughput_description


class ReplicaDescription(TypedDict):
    region_name: NotRequired["aws_sdk_dynamodb.types.region_name.RegionName"]
    """<p>The name of the Region.</p>"""
    replica_status: NotRequired["aws_sdk_dynamodb.types.replica_status.ReplicaStatus"]
    """<p>The current state of the replica:</p> <ul> <li> <p> <code>CREATING</code> - The replica is being created.</p> </li> <li> <p> <code>UPDATING</code> - The replica is being updated.</p> </li> <li> <p> <code>DELETING</code> - The replica is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The replica is ready for use.</p> </li> <li> <p> <code>REGION_DISABLED</code> - The replica is inaccessible because the Amazon Web Services Region has been disabled.</p> <note> <p>If the Amazon Web Services Region remains inaccessible for more than 20 hours, DynamoDB will remove this replica from the replication group. The replica will not be deleted and replication will stop from and to this region.</p> </note> </li> <li> <p> <code>INACCESSIBLE_ENCRYPTION_CREDENTIALS </code> - The KMS key used to encrypt the table is inaccessible.</p> <note> <p>If the KMS key remains inaccessible for more than 20 hours, DynamoDB will remove this replica from the replication group. The replica will not be deleted and replication will stop from and to this region.</p> </note> </li> </ul>"""
    replica_arn: NotRequired["aws_sdk_dynamodb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the global table replica.</p>"""
    replica_status_description: NotRequired[
        "aws_sdk_dynamodb.types.replica_status_description.ReplicaStatusDescription"
    ]
    """<p>Detailed information about the replica status.</p>"""
    replica_status_percent_progress: NotRequired[
        "aws_sdk_dynamodb.types.replica_status_percent_progress.ReplicaStatusPercentProgress"
    ]
    """<p>Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.</p>"""
    kms_master_key_id: NotRequired[
        "aws_sdk_dynamodb.types.kms_master_key_id.KMSMasterKeyId"
    ]
    """<p>The KMS key of the replica that will be used for KMS encryption.</p>"""
    provisioned_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput_override.ProvisionedThroughputOverride"
    ]
    """<p>Replica-specific provisioned throughput. If not described, uses the source table's provisioned throughput settings.</p>"""
    on_demand_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput_override.OnDemandThroughputOverride"
    ]
    """<p>Overrides the maximum on-demand throughput settings for the specified replica table.</p>"""
    warm_throughput: NotRequired[
        "aws_sdk_dynamodb.types.table_warm_throughput_description.TableWarmThroughputDescription"
    ]
    """<p>Represents the warm throughput value for this replica.</p>"""
    global_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.replica_global_secondary_index_description_list.ReplicaGlobalSecondaryIndexDescriptionList"
    ]
    """<p>Replica-specific global secondary index settings.</p>"""
    replica_inaccessible_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>The time at which the replica was first detected as inaccessible. To determine cause of inaccessibility check the <code>ReplicaStatus</code> property.</p>"""
    replica_table_class_summary: NotRequired[
        "aws_sdk_dynamodb.types.table_class_summary.TableClassSummary"
    ]
    global_table_settings_replication_mode: NotRequired[
        "aws_sdk_dynamodb.types.global_table_settings_replication_mode.GlobalTableSettingsReplicationMode"
    ]
    """<p>Indicates one of the settings synchronization modes for the global table replica:</p> <ul> <li> <p> <code>ENABLED</code>: Indicates that the settings synchronization mode for the global table replica is enabled.</p> </li> <li> <p> <code>DISABLED</code>: Indicates that the settings synchronization mode for the global table replica is disabled.</p> </li> <li> <p> <code>ENABLED_WITH_OVERRIDES</code>: This mode is set by default for a same account global table. Indicates that certain global table settings can be overridden.</p> </li> </ul>"""
