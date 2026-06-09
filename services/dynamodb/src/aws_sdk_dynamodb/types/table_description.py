"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.archival_summary
    import aws_sdk_dynamodb.types.attribute_definitions
    import aws_sdk_dynamodb.types.billing_mode_summary
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.deletion_protection_enabled
    import aws_sdk_dynamodb.types.global_secondary_index_description_list
    import aws_sdk_dynamodb.types.global_table_settings_replication_mode
    import aws_sdk_dynamodb.types.global_table_witness_description_list
    import aws_sdk_dynamodb.types.key_schema
    import aws_sdk_dynamodb.types.local_secondary_index_description_list
    import aws_sdk_dynamodb.types.long_object
    import aws_sdk_dynamodb.types.multi_region_consistency
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.provisioned_throughput_description
    import aws_sdk_dynamodb.types.replica_description_list
    import aws_sdk_dynamodb.types.restore_summary
    import aws_sdk_dynamodb.types.sse_description
    import aws_sdk_dynamodb.types.stream_arn
    import aws_sdk_dynamodb.types.stream_specification
    import aws_sdk_dynamodb.types.string
    import aws_sdk_dynamodb.types.table_class_summary
    import aws_sdk_dynamodb.types.table_id
    import aws_sdk_dynamodb.types.table_name
    import aws_sdk_dynamodb.types.table_status
    import aws_sdk_dynamodb.types.table_warm_throughput_description


class TableDescription(TypedDict):
    attribute_definitions: NotRequired[
        "aws_sdk_dynamodb.types.attribute_definitions.AttributeDefinitions"
    ]
    """<p>An array of <code>AttributeDefinition</code> objects. Each of these objects describes one attribute in the table and index key schema.</p> <p>Each <code>AttributeDefinition</code> object in this array is composed of:</p> <ul> <li> <p> <code>AttributeName</code> - The name of the attribute.</p> </li> <li> <p> <code>AttributeType</code> - The data type for the attribute.</p> </li> </ul>"""
    table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>The name of the table.</p>"""
    key_schema: NotRequired["aws_sdk_dynamodb.types.key_schema.KeySchema"]
    """<p>The primary key structure for the table. Each <code>KeySchemaElement</code> consists of:</p> <ul> <li> <p> <code>AttributeName</code> - The name of the attribute.</p> </li> <li> <p> <code>KeyType</code> - The role of the attribute:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term \"hash attribute\" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term \"range attribute\" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note> </li> </ul> <p>For more information about primary keys, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html#DataModelPrimaryKey\">Primary Key</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    table_status: NotRequired["aws_sdk_dynamodb.types.table_status.TableStatus"]
    """<p>The current state of the table:</p> <ul> <li> <p> <code>CREATING</code> - The table is being created.</p> </li> <li> <p> <code>UPDATING</code> - The table/index configuration is being updated. The table/index remains available for data operations when <code>UPDATING</code>.</p> </li> <li> <p> <code>DELETING</code> - The table is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The table is ready for use.</p> </li> <li> <p> <code>INACCESSIBLE_ENCRYPTION_CREDENTIALS</code> - The KMS key used to encrypt the table in inaccessible. Table operations may fail due to failure to use the KMS key. DynamoDB will initiate the table archival process when a table's KMS key remains inaccessible for more than seven days. </p> </li> <li> <p> <code>ARCHIVING</code> - The table is being archived. Operations are not allowed until archival is complete. </p> </li> <li> <p> <code>ARCHIVED</code> - The table has been archived. See the ArchivalReason for more information. </p> </li> </ul>"""
    creation_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>The date and time when the table was created, in <a href=\"http://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput_description.ProvisionedThroughputDescription"
    ]
    """<p>The provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.</p>"""
    table_size_bytes: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>The total size of the specified table, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p>"""
    item_count: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>The number of items in the specified table. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p>"""
    table_arn: NotRequired["aws_sdk_dynamodb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the table.</p>"""
    table_id: NotRequired["aws_sdk_dynamodb.types.table_id.TableId"]
    """<p>Unique identifier for the table for which the backup was created. </p>"""
    billing_mode_summary: NotRequired[
        "aws_sdk_dynamodb.types.billing_mode_summary.BillingModeSummary"
    ]
    """<p>Contains the details for the read/write capacity mode.</p>"""
    local_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.local_secondary_index_description_list.LocalSecondaryIndexDescriptionList"
    ]
    """<p>Represents one or more local secondary indexes on the table. Each index is scoped to a given partition key value. Tables with one or more local secondary indexes are subject to an item collection size limit, where the amount of data within a given item collection cannot exceed 10 GB. Each element is composed of:</p> <ul> <li> <p> <code>IndexName</code> - The name of the local secondary index.</p> </li> <li> <p> <code>KeySchema</code> - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.</p> </li> <li> <p> <code>Projection</code> - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:</p> <ul> <li> <p> <code>ProjectionType</code> - One of the following:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the index and primary keys are projected into the index.</p> </li> <li> <p> <code>INCLUDE</code> - Only the specified table attributes are projected into the index. The list of projected attributes is in <code>NonKeyAttributes</code>.</p> </li> <li> <p> <code>ALL</code> - All of the table attributes are projected into the index.</p> </li> </ul> </li> <li> <p> <code>NonKeyAttributes</code> - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in <code>NonKeyAttributes</code>, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of <code>INCLUDE</code>. You still can specify the ProjectionType of <code>ALL</code> to project all attributes from the source table, even if the table has more than 100 attributes.</p> </li> </ul> </li> <li> <p> <code>IndexSizeBytes</code> - Represents the total size of the index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p> </li> <li> <p> <code>ItemCount</code> - Represents the number of items in the index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p> </li> </ul> <p>If the table is in the <code>DELETING</code> state, no information about indexes will be returned.</p>"""
    global_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.global_secondary_index_description_list.GlobalSecondaryIndexDescriptionList"
    ]
    """<p>The global secondary indexes, if any, on the table. Each index is scoped to a given partition key value. Each element is composed of:</p> <ul> <li> <p> <code>Backfilling</code> - If true, then the index is currently in the backfilling phase. Backfilling occurs only when a new global secondary index is added to the table. It is the process by which DynamoDB populates the new index with data from the table. (This attribute does not appear for indexes that were created during a <code>CreateTable</code> operation.) </p> <p> You can delete an index that is being created during the <code>Backfilling</code> phase when <code>IndexStatus</code> is set to CREATING and <code>Backfilling</code> is true. You can't delete the index that is being created when <code>IndexStatus</code> is set to CREATING and <code>Backfilling</code> is false. (This attribute does not appear for indexes that were created during a <code>CreateTable</code> operation.)</p> </li> <li> <p> <code>IndexName</code> - The name of the global secondary index.</p> </li> <li> <p> <code>IndexSizeBytes</code> - The total size of the global secondary index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value. </p> </li> <li> <p> <code>IndexStatus</code> - The current status of the global secondary index:</p> <ul> <li> <p> <code>CREATING</code> - The index is being created.</p> </li> <li> <p> <code>UPDATING</code> - The index is being updated.</p> </li> <li> <p> <code>DELETING</code> - The index is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The index is ready for use.</p> </li> </ul> </li> <li> <p> <code>ItemCount</code> - The number of items in the global secondary index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value. </p> </li> <li> <p> <code>KeySchema</code> - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.</p> </li> <li> <p> <code>Projection</code> - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:</p> <ul> <li> <p> <code>ProjectionType</code> - One of the following:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the index and primary keys are projected into the index.</p> </li> <li> <p> <code>INCLUDE</code> - In addition to the attributes described in <code>KEYS_ONLY</code>, the secondary index will include other non-key attributes that you specify.</p> </li> <li> <p> <code>ALL</code> - All of the table attributes are projected into the index.</p> </li> </ul> </li> <li> <p> <code>NonKeyAttributes</code> - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in <code>NonKeyAttributes</code>, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of <code>INCLUDE</code>. You still can specify the ProjectionType of <code>ALL</code> to project all attributes from the source table, even if the table has more than 100 attributes.</p> </li> </ul> </li> <li> <p> <code>ProvisionedThroughput</code> - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units, along with data about increases and decreases. </p> </li> </ul> <p>If the table is in the <code>DELETING</code> state, no information about indexes will be returned.</p>"""
    stream_specification: NotRequired[
        "aws_sdk_dynamodb.types.stream_specification.StreamSpecification"
    ]
    """<p>The current DynamoDB Streams configuration for the table.</p>"""
    latest_stream_label: NotRequired["aws_sdk_dynamodb.types.string.String"]
    """<p>A timestamp, in ISO 8601 format, for this stream.</p> <p>Note that <code>LatestStreamLabel</code> is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:</p> <ul> <li> <p>Amazon Web Services customer ID</p> </li> <li> <p>Table name</p> </li> <li> <p> <code>StreamLabel</code> </p> </li> </ul>"""
    latest_stream_arn: NotRequired["aws_sdk_dynamodb.types.stream_arn.StreamArn"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the latest stream for this table.</p>"""
    global_table_version: NotRequired["aws_sdk_dynamodb.types.string.String"]
    """<p>Represents the version of <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html\">global tables</a> in use, if the table is replicated across Amazon Web Services Regions.</p>"""
    replicas: NotRequired[
        "aws_sdk_dynamodb.types.replica_description_list.ReplicaDescriptionList"
    ]
    """<p>Represents replicas of the table.</p>"""
    global_table_witnesses: NotRequired[
        "aws_sdk_dynamodb.types.global_table_witness_description_list.GlobalTableWitnessDescriptionList"
    ]
    """<p>The witness Region and its current status in the MRSC global table. Only one witness Region can be configured per MRSC global table.</p>"""
    global_table_settings_replication_mode: NotRequired[
        "aws_sdk_dynamodb.types.global_table_settings_replication_mode.GlobalTableSettingsReplicationMode"
    ]
    """<p>Indicates one of the settings synchronization modes for the global table:</p> <ul> <li> <p> <code>ENABLED</code>: Indicates that the settings synchronization mode for the global table is enabled.</p> </li> <li> <p> <code>DISABLED</code>: Indicates that the settings synchronization mode for the global table is disabled.</p> </li> <li> <p> <code>ENABLED_WITH_OVERRIDES</code>: This mode is set by default for a same account global table. Indicates that certain global table settings can be overridden.</p> </li> </ul>"""
    restore_summary: NotRequired[
        "aws_sdk_dynamodb.types.restore_summary.RestoreSummary"
    ]
    """<p>Contains details for the restore.</p>"""
    sse_description: NotRequired[
        "aws_sdk_dynamodb.types.sse_description.SSEDescription"
    ]
    """<p>The description of the server-side encryption status on the specified table.</p>"""
    archival_summary: NotRequired[
        "aws_sdk_dynamodb.types.archival_summary.ArchivalSummary"
    ]
    """<p>Contains information about the table archive.</p>"""
    table_class_summary: NotRequired[
        "aws_sdk_dynamodb.types.table_class_summary.TableClassSummary"
    ]
    """<p>Contains details of the table class.</p>"""
    deletion_protection_enabled: NotRequired[
        "aws_sdk_dynamodb.types.deletion_protection_enabled.DeletionProtectionEnabled"
    ]
    """<p>Indicates whether deletion protection is enabled (true) or disabled (false) on the table.</p>"""
    on_demand_throughput: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    """<p>The maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both.</p>"""
    warm_throughput: NotRequired[
        "aws_sdk_dynamodb.types.table_warm_throughput_description.TableWarmThroughputDescription"
    ]
    """<p>Describes the warm throughput value of the base table.</p>"""
    multi_region_consistency: NotRequired[
        "aws_sdk_dynamodb.types.multi_region_consistency.MultiRegionConsistency"
    ]
    """<p>Indicates one of the following consistency modes for a global table:</p> <ul> <li> <p> <code>EVENTUAL</code>: Indicates that the global table is configured for multi-Region eventual consistency (MREC).</p> </li> <li> <p> <code>STRONG</code>: Indicates that the global table is configured for multi-Region strong consistency (MRSC).</p> </li> </ul> <p>If you don't specify this field, the global table consistency mode defaults to <code>EVENTUAL</code>. For more information about global tables consistency modes, see <a href=\"https://docs.aws.amazon.com/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes\"> Consistency modes</a> in DynamoDB developer guide. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableDescription) -> dict:
    out: dict = {}
    if "attribute_definitions" in value:
        import aws_sdk_dynamodb.types.attribute_definitions

        out["AttributeDefinitions"] = (
            aws_sdk_dynamodb.types.attribute_definitions.serialize_aws_json_1_0(
                value["attribute_definitions"]
            )
        )
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "key_schema" in value:
        import aws_sdk_dynamodb.types.key_schema

        out["KeySchema"] = aws_sdk_dynamodb.types.key_schema.serialize_aws_json_1_0(
            value["key_schema"]
        )
    if "table_status" in value:
        import aws_sdk_dynamodb.types.table_status

        out["TableStatus"] = aws_sdk_dynamodb.types.table_status.serialize_aws_json_1_0(
            value["table_status"]
        )
    if "creation_date_time" in value:
        import aws_sdk_dynamodb.types.date

        out["CreationDateTime"] = aws_sdk_dynamodb.types.date.serialize_aws_json_1_0(
            value["creation_date_time"]
        )
    if "provisioned_throughput" in value:
        import aws_sdk_dynamodb.types.provisioned_throughput_description

        out["ProvisionedThroughput"] = (
            aws_sdk_dynamodb.types.provisioned_throughput_description.serialize_aws_json_1_0(
                value["provisioned_throughput"]
            )
        )
    if "table_size_bytes" in value:
        out["TableSizeBytes"] = value["table_size_bytes"]
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "table_arn" in value:
        out["TableArn"] = value["table_arn"]
    if "table_id" in value:
        out["TableId"] = value["table_id"]
    if "billing_mode_summary" in value:
        import aws_sdk_dynamodb.types.billing_mode_summary

        out["BillingModeSummary"] = (
            aws_sdk_dynamodb.types.billing_mode_summary.serialize_aws_json_1_0(
                value["billing_mode_summary"]
            )
        )
    if "local_secondary_indexes" in value:
        import aws_sdk_dynamodb.types.local_secondary_index_description_list

        out["LocalSecondaryIndexes"] = (
            aws_sdk_dynamodb.types.local_secondary_index_description_list.serialize_aws_json_1_0(
                value["local_secondary_indexes"]
            )
        )
    if "global_secondary_indexes" in value:
        import aws_sdk_dynamodb.types.global_secondary_index_description_list

        out["GlobalSecondaryIndexes"] = (
            aws_sdk_dynamodb.types.global_secondary_index_description_list.serialize_aws_json_1_0(
                value["global_secondary_indexes"]
            )
        )
    if "stream_specification" in value:
        import aws_sdk_dynamodb.types.stream_specification

        out["StreamSpecification"] = (
            aws_sdk_dynamodb.types.stream_specification.serialize_aws_json_1_0(
                value["stream_specification"]
            )
        )
    if "latest_stream_label" in value:
        out["LatestStreamLabel"] = value["latest_stream_label"]
    if "latest_stream_arn" in value:
        out["LatestStreamArn"] = value["latest_stream_arn"]
    if "global_table_version" in value:
        out["GlobalTableVersion"] = value["global_table_version"]
    if "replicas" in value:
        import aws_sdk_dynamodb.types.replica_description_list

        out["Replicas"] = (
            aws_sdk_dynamodb.types.replica_description_list.serialize_aws_json_1_0(
                value["replicas"]
            )
        )
    if "global_table_witnesses" in value:
        import aws_sdk_dynamodb.types.global_table_witness_description_list

        out["GlobalTableWitnesses"] = (
            aws_sdk_dynamodb.types.global_table_witness_description_list.serialize_aws_json_1_0(
                value["global_table_witnesses"]
            )
        )
    if "global_table_settings_replication_mode" in value:
        import aws_sdk_dynamodb.types.global_table_settings_replication_mode

        out["GlobalTableSettingsReplicationMode"] = (
            aws_sdk_dynamodb.types.global_table_settings_replication_mode.serialize_aws_json_1_0(
                value["global_table_settings_replication_mode"]
            )
        )
    if "restore_summary" in value:
        import aws_sdk_dynamodb.types.restore_summary

        out["RestoreSummary"] = (
            aws_sdk_dynamodb.types.restore_summary.serialize_aws_json_1_0(
                value["restore_summary"]
            )
        )
    if "sse_description" in value:
        import aws_sdk_dynamodb.types.sse_description

        out["SSEDescription"] = (
            aws_sdk_dynamodb.types.sse_description.serialize_aws_json_1_0(
                value["sse_description"]
            )
        )
    if "archival_summary" in value:
        import aws_sdk_dynamodb.types.archival_summary

        out["ArchivalSummary"] = (
            aws_sdk_dynamodb.types.archival_summary.serialize_aws_json_1_0(
                value["archival_summary"]
            )
        )
    if "table_class_summary" in value:
        import aws_sdk_dynamodb.types.table_class_summary

        out["TableClassSummary"] = (
            aws_sdk_dynamodb.types.table_class_summary.serialize_aws_json_1_0(
                value["table_class_summary"]
            )
        )
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "on_demand_throughput" in value:
        import aws_sdk_dynamodb.types.on_demand_throughput

        out["OnDemandThroughput"] = (
            aws_sdk_dynamodb.types.on_demand_throughput.serialize_aws_json_1_0(
                value["on_demand_throughput"]
            )
        )
    if "warm_throughput" in value:
        import aws_sdk_dynamodb.types.table_warm_throughput_description

        out["WarmThroughput"] = (
            aws_sdk_dynamodb.types.table_warm_throughput_description.serialize_aws_json_1_0(
                value["warm_throughput"]
            )
        )
    if "multi_region_consistency" in value:
        import aws_sdk_dynamodb.types.multi_region_consistency

        out["MultiRegionConsistency"] = (
            aws_sdk_dynamodb.types.multi_region_consistency.serialize_aws_json_1_0(
                value["multi_region_consistency"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TableDescription:
    out: TableDescription = {}  # type: ignore[typeddict-item]
    if "AttributeDefinitions" in data:
        import aws_sdk_dynamodb.types.attribute_definitions

        out["attribute_definitions"] = (
            aws_sdk_dynamodb.types.attribute_definitions.deserialize_aws_json_1_0(
                data["AttributeDefinitions"]
            )
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "KeySchema" in data:
        import aws_sdk_dynamodb.types.key_schema

        out["key_schema"] = aws_sdk_dynamodb.types.key_schema.deserialize_aws_json_1_0(
            data["KeySchema"]
        )
    if "TableStatus" in data:
        import aws_sdk_dynamodb.types.table_status

        out["table_status"] = (
            aws_sdk_dynamodb.types.table_status.deserialize_aws_json_1_0(
                data["TableStatus"]
            )
        )
    if "CreationDateTime" in data:
        import aws_sdk_dynamodb.types.date

        out["creation_date_time"] = (
            aws_sdk_dynamodb.types.date.deserialize_aws_json_1_0(
                data["CreationDateTime"]
            )
        )
    if "ProvisionedThroughput" in data:
        import aws_sdk_dynamodb.types.provisioned_throughput_description

        out["provisioned_throughput"] = (
            aws_sdk_dynamodb.types.provisioned_throughput_description.deserialize_aws_json_1_0(
                data["ProvisionedThroughput"]
            )
        )
    if "TableSizeBytes" in data:
        out["table_size_bytes"] = data["TableSizeBytes"]
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    if "TableArn" in data:
        out["table_arn"] = data["TableArn"]
    if "TableId" in data:
        out["table_id"] = data["TableId"]
    if "BillingModeSummary" in data:
        import aws_sdk_dynamodb.types.billing_mode_summary

        out["billing_mode_summary"] = (
            aws_sdk_dynamodb.types.billing_mode_summary.deserialize_aws_json_1_0(
                data["BillingModeSummary"]
            )
        )
    if "LocalSecondaryIndexes" in data:
        import aws_sdk_dynamodb.types.local_secondary_index_description_list

        out["local_secondary_indexes"] = (
            aws_sdk_dynamodb.types.local_secondary_index_description_list.deserialize_aws_json_1_0(
                data["LocalSecondaryIndexes"]
            )
        )
    if "GlobalSecondaryIndexes" in data:
        import aws_sdk_dynamodb.types.global_secondary_index_description_list

        out["global_secondary_indexes"] = (
            aws_sdk_dynamodb.types.global_secondary_index_description_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexes"]
            )
        )
    if "StreamSpecification" in data:
        import aws_sdk_dynamodb.types.stream_specification

        out["stream_specification"] = (
            aws_sdk_dynamodb.types.stream_specification.deserialize_aws_json_1_0(
                data["StreamSpecification"]
            )
        )
    if "LatestStreamLabel" in data:
        out["latest_stream_label"] = data["LatestStreamLabel"]
    if "LatestStreamArn" in data:
        out["latest_stream_arn"] = data["LatestStreamArn"]
    if "GlobalTableVersion" in data:
        out["global_table_version"] = data["GlobalTableVersion"]
    if "Replicas" in data:
        import aws_sdk_dynamodb.types.replica_description_list

        out["replicas"] = (
            aws_sdk_dynamodb.types.replica_description_list.deserialize_aws_json_1_0(
                data["Replicas"]
            )
        )
    if "GlobalTableWitnesses" in data:
        import aws_sdk_dynamodb.types.global_table_witness_description_list

        out["global_table_witnesses"] = (
            aws_sdk_dynamodb.types.global_table_witness_description_list.deserialize_aws_json_1_0(
                data["GlobalTableWitnesses"]
            )
        )
    if "GlobalTableSettingsReplicationMode" in data:
        import aws_sdk_dynamodb.types.global_table_settings_replication_mode

        out["global_table_settings_replication_mode"] = (
            aws_sdk_dynamodb.types.global_table_settings_replication_mode.deserialize_aws_json_1_0(
                data["GlobalTableSettingsReplicationMode"]
            )
        )
    if "RestoreSummary" in data:
        import aws_sdk_dynamodb.types.restore_summary

        out["restore_summary"] = (
            aws_sdk_dynamodb.types.restore_summary.deserialize_aws_json_1_0(
                data["RestoreSummary"]
            )
        )
    if "SSEDescription" in data:
        import aws_sdk_dynamodb.types.sse_description

        out["sse_description"] = (
            aws_sdk_dynamodb.types.sse_description.deserialize_aws_json_1_0(
                data["SSEDescription"]
            )
        )
    if "ArchivalSummary" in data:
        import aws_sdk_dynamodb.types.archival_summary

        out["archival_summary"] = (
            aws_sdk_dynamodb.types.archival_summary.deserialize_aws_json_1_0(
                data["ArchivalSummary"]
            )
        )
    if "TableClassSummary" in data:
        import aws_sdk_dynamodb.types.table_class_summary

        out["table_class_summary"] = (
            aws_sdk_dynamodb.types.table_class_summary.deserialize_aws_json_1_0(
                data["TableClassSummary"]
            )
        )
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if "OnDemandThroughput" in data:
        import aws_sdk_dynamodb.types.on_demand_throughput

        out["on_demand_throughput"] = (
            aws_sdk_dynamodb.types.on_demand_throughput.deserialize_aws_json_1_0(
                data["OnDemandThroughput"]
            )
        )
    if "WarmThroughput" in data:
        import aws_sdk_dynamodb.types.table_warm_throughput_description

        out["warm_throughput"] = (
            aws_sdk_dynamodb.types.table_warm_throughput_description.deserialize_aws_json_1_0(
                data["WarmThroughput"]
            )
        )
    if "MultiRegionConsistency" in data:
        import aws_sdk_dynamodb.types.multi_region_consistency

        out["multi_region_consistency"] = (
            aws_sdk_dynamodb.types.multi_region_consistency.deserialize_aws_json_1_0(
                data["MultiRegionConsistency"]
            )
        )
    return out
