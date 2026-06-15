"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition_list
    import aws_sdk_securityhub.types.aws_dynamo_db_table_billing_mode_summary
    import aws_sdk_securityhub.types.aws_dynamo_db_table_global_secondary_index_list
    import aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list
    import aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index_list
    import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput
    import aws_sdk_securityhub.types.aws_dynamo_db_table_replica_list
    import aws_sdk_securityhub.types.aws_dynamo_db_table_restore_summary
    import aws_sdk_securityhub.types.aws_dynamo_db_table_sse_description
    import aws_sdk_securityhub.types.aws_dynamo_db_table_stream_specification
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.size_bytes


class AwsDynamoDbTableDetails(TypedDict):
    attribute_definitions: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition_list.AwsDynamoDbTableAttributeDefinitionList"
    ]
    """<p>A list of attribute definitions for the table.</p>"""
    billing_mode_summary: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_billing_mode_summary.AwsDynamoDbTableBillingModeSummary"
    ]
    """<p>Information about the billing for read/write capacity on the table.</p>"""
    creation_date_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the table was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    global_secondary_indexes: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_global_secondary_index_list.AwsDynamoDbTableGlobalSecondaryIndexList"
    ]
    """<p>List of global secondary indexes for the table.</p>"""
    global_table_version: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of global tables being used.</p>"""
    item_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of items in the table.</p>"""
    key_schema: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list.AwsDynamoDbTableKeySchemaList"
    ]
    """<p>The primary key structure for the table.</p>"""
    latest_stream_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the latest stream for the table.</p>"""
    latest_stream_label: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The label of the latest stream. The label is not a unique identifier.</p>"""
    local_secondary_indexes: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index_list.AwsDynamoDbTableLocalSecondaryIndexList"
    ]
    """<p>The list of local secondary indexes for the table.</p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput.AwsDynamoDbTableProvisionedThroughput"
    ]
    """<p>Information about the provisioned throughput for the table.</p>"""
    replicas: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_replica_list.AwsDynamoDbTableReplicaList"
    ]
    """<p>The list of replicas of this table.</p>"""
    restore_summary: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_restore_summary.AwsDynamoDbTableRestoreSummary"
    ]
    """<p>Information about the restore for the table.</p>"""
    sse_description: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_sse_description.AwsDynamoDbTableSseDescription"
    ]
    """<p>Information about the server-side encryption for the table.</p>"""
    stream_specification: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_stream_specification.AwsDynamoDbTableStreamSpecification"
    ]
    """<p>The current DynamoDB Streams configuration for the table.</p>"""
    table_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the table.</p>"""
    table_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the table.</p>"""
    table_size_bytes: NotRequired["aws_sdk_securityhub.types.size_bytes.SizeBytes"]
    """<p>The total size of the table in bytes.</p>"""
    table_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The current status of the table. Valid values are as follows:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>ARCHIVED</code> </p> </li> <li> <p> <code>ARCHIVING</code> </p> </li> <li> <p> <code>CREATING</code> </p> </li> <li> <p> <code>DELETING</code> </p> </li> <li> <p> <code>INACCESSIBLE_ENCRYPTION_CREDENTIALS</code> </p> </li> <li> <p> <code>UPDATING</code> </p> </li> </ul>"""
    deletion_protection_enabled: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p> Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableDetails) -> dict:
    out: dict = {}
    if "attribute_definitions" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition_list

        out["AttributeDefinitions"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition_list.serialize_json(
                value["attribute_definitions"]
            )
        )
    if "billing_mode_summary" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_billing_mode_summary

        out["BillingModeSummary"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_billing_mode_summary.serialize_json(
                value["billing_mode_summary"]
            )
        )
    if "creation_date_time" in value:
        out["CreationDateTime"] = value["creation_date_time"]
    if "global_secondary_indexes" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_global_secondary_index_list

        out["GlobalSecondaryIndexes"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_global_secondary_index_list.serialize_json(
                value["global_secondary_indexes"]
            )
        )
    if "global_table_version" in value:
        out["GlobalTableVersion"] = value["global_table_version"]
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "key_schema" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list

        out["KeySchema"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list.serialize_json(
                value["key_schema"]
            )
        )
    if "latest_stream_arn" in value:
        out["LatestStreamArn"] = value["latest_stream_arn"]
    if "latest_stream_label" in value:
        out["LatestStreamLabel"] = value["latest_stream_label"]
    if "local_secondary_indexes" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index_list

        out["LocalSecondaryIndexes"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index_list.serialize_json(
                value["local_secondary_indexes"]
            )
        )
    if "provisioned_throughput" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput

        out["ProvisionedThroughput"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput.serialize_json(
                value["provisioned_throughput"]
            )
        )
    if "replicas" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_replica_list

        out["Replicas"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_replica_list.serialize_json(
                value["replicas"]
            )
        )
    if "restore_summary" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_restore_summary

        out["RestoreSummary"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_restore_summary.serialize_json(
                value["restore_summary"]
            )
        )
    if "sse_description" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_sse_description

        out["SseDescription"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_sse_description.serialize_json(
                value["sse_description"]
            )
        )
    if "stream_specification" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_stream_specification

        out["StreamSpecification"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_stream_specification.serialize_json(
                value["stream_specification"]
            )
        )
    if "table_id" in value:
        out["TableId"] = value["table_id"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "table_size_bytes" in value:
        out["TableSizeBytes"] = value["table_size_bytes"]
    if "table_status" in value:
        out["TableStatus"] = value["table_status"]
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableDetails:
    out: AwsDynamoDbTableDetails = {}  # type: ignore[typeddict-item]
    if "AttributeDefinitions" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition_list

        out["attribute_definitions"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition_list.deserialize_json(
                data["AttributeDefinitions"]
            )
        )
    if "BillingModeSummary" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_billing_mode_summary

        out["billing_mode_summary"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_billing_mode_summary.deserialize_json(
                data["BillingModeSummary"]
            )
        )
    if "CreationDateTime" in data:
        out["creation_date_time"] = data["CreationDateTime"]
    if "GlobalSecondaryIndexes" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_global_secondary_index_list

        out["global_secondary_indexes"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_global_secondary_index_list.deserialize_json(
                data["GlobalSecondaryIndexes"]
            )
        )
    if "GlobalTableVersion" in data:
        out["global_table_version"] = data["GlobalTableVersion"]
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    if "KeySchema" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list

        out["key_schema"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list.deserialize_json(
                data["KeySchema"]
            )
        )
    if "LatestStreamArn" in data:
        out["latest_stream_arn"] = data["LatestStreamArn"]
    if "LatestStreamLabel" in data:
        out["latest_stream_label"] = data["LatestStreamLabel"]
    if "LocalSecondaryIndexes" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index_list

        out["local_secondary_indexes"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index_list.deserialize_json(
                data["LocalSecondaryIndexes"]
            )
        )
    if "ProvisionedThroughput" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput

        out["provisioned_throughput"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput.deserialize_json(
                data["ProvisionedThroughput"]
            )
        )
    if "Replicas" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_replica_list

        out["replicas"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_replica_list.deserialize_json(
                data["Replicas"]
            )
        )
    if "RestoreSummary" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_restore_summary

        out["restore_summary"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_restore_summary.deserialize_json(
                data["RestoreSummary"]
            )
        )
    if "SseDescription" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_sse_description

        out["sse_description"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_sse_description.deserialize_json(
                data["SseDescription"]
            )
        )
    if "StreamSpecification" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_stream_specification

        out["stream_specification"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_stream_specification.deserialize_json(
                data["StreamSpecification"]
            )
        )
    if "TableId" in data:
        out["table_id"] = data["TableId"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "TableSizeBytes" in data:
        out["table_size_bytes"] = data["TableSizeBytes"]
    if "TableStatus" in data:
        out["table_status"] = data["TableStatus"]
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    return out
