"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateReplicationGroupMemberAction``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.kms_master_key_id
    import aws_sdk_dynamodb.types.on_demand_throughput_override
    import aws_sdk_dynamodb.types.provisioned_throughput_override
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.replica_global_secondary_index_list
    import aws_sdk_dynamodb.types.table_class


class CreateReplicationGroupMemberAction(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region where the new replica will be created.</p>"""
    kms_master_key_id: NotRequired[
        "aws_sdk_dynamodb.types.kms_master_key_id.KMSMasterKeyId"
    ]
    """<p>The KMS key that should be used for KMS encryption in the new replica. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS key <code>alias/aws/dynamodb</code>.</p>"""
    provisioned_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput_override.ProvisionedThroughputOverride"
    ]
    """<p>Replica-specific provisioned throughput. If not specified, uses the source table's provisioned throughput settings.</p>"""
    on_demand_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput_override.OnDemandThroughputOverride"
    ]
    """<p>The maximum on-demand throughput settings for the specified replica table being created. You can only modify <code>MaxReadRequestUnits</code>, because you can't modify <code>MaxWriteRequestUnits</code> for individual replica tables. </p>"""
    global_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.replica_global_secondary_index_list.ReplicaGlobalSecondaryIndexList"
    ]
    """<p>Replica-specific global secondary index settings.</p>"""
    table_class_override: NotRequired["aws_sdk_dynamodb.types.table_class.TableClass"]
    """<p>Replica-specific table class. If not specified, uses the source table's table class.</p>"""
