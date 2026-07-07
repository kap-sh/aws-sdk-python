"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KinesisSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.message_format_value
    import aws_sdk_database_migration_service.types.string


class KinesisSettings(TypedDict, closed=True):
    stream_arn: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.</p>"""
    message_format: NotRequired[
        "aws_sdk_database_migration_service.types.message_format_value.MessageFormatValue"
    ]
    """<p>The output format for the records created on the endpoint. The message format is <code>JSON</code> (default) or <code>JSON_UNFORMATTED</code> (a single line with no tab).</p>"""
    service_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Kinesis data stream. The role must allow the <code>iam:PassRole</code> action.</p>"""
    include_transaction_details: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for <code>transaction_id</code>, previous <code>transaction_id</code>, and <code>transaction_record_id</code> (the record offset within a transaction). The default is <code>false</code>.</p>"""
    include_partition_value: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Shows the partition value within the Kinesis message output, unless the partition type is <code>schema-table-type</code>. The default is <code>false</code>.</p>"""
    partition_include_schema_table: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Prefixes schema and table names to partition values, when the partition type is <code>primary-key-type</code>. Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is <code>false</code>.</p>"""
    include_table_alter_operations: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Includes any data definition language (DDL) operations that change the table in the control data, such as <code>rename-table</code>, <code>drop-table</code>, <code>add-column</code>, <code>drop-column</code>, and <code>rename-column</code>. The default is <code>false</code>.</p>"""
    include_control_details: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is <code>false</code>.</p>"""
    include_null_and_empty: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Include NULL and empty columns for records migrated to the endpoint. The default is <code>false</code>.</p>"""
    no_hex_prefix: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this optional parameter to <code>true</code> to avoid adding a '0x' prefix to raw data in hexadecimal format. For example, by default, DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to an Amazon Kinesis target. Use the <code>NoHexPrefix</code> endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.</p>"""
    use_large_integer_value: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies using the large integer value with Kinesis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisSettings) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamArn"] = value["stream_arn"]
    if "message_format" in value:
        import aws_sdk_database_migration_service.types.message_format_value

        out["MessageFormat"] = (
            aws_sdk_database_migration_service.types.message_format_value.serialize_aws_json_1_1(
                value["message_format"]
            )
        )
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "include_transaction_details" in value:
        out["IncludeTransactionDetails"] = value["include_transaction_details"]
    if "include_partition_value" in value:
        out["IncludePartitionValue"] = value["include_partition_value"]
    if "partition_include_schema_table" in value:
        out["PartitionIncludeSchemaTable"] = value["partition_include_schema_table"]
    if "include_table_alter_operations" in value:
        out["IncludeTableAlterOperations"] = value["include_table_alter_operations"]
    if "include_control_details" in value:
        out["IncludeControlDetails"] = value["include_control_details"]
    if "include_null_and_empty" in value:
        out["IncludeNullAndEmpty"] = value["include_null_and_empty"]
    if "no_hex_prefix" in value:
        out["NoHexPrefix"] = value["no_hex_prefix"]
    if "use_large_integer_value" in value:
        out["UseLargeIntegerValue"] = value["use_large_integer_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisSettings:
    out: KinesisSettings = {}  # type: ignore[typeddict-item]
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    if "MessageFormat" in data:
        import aws_sdk_database_migration_service.types.message_format_value

        out["message_format"] = (
            aws_sdk_database_migration_service.types.message_format_value.deserialize_aws_json_1_1(
                data["MessageFormat"]
            )
        )
    if "ServiceAccessRoleArn" in data:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if "IncludeTransactionDetails" in data:
        out["include_transaction_details"] = data["IncludeTransactionDetails"]
    if "IncludePartitionValue" in data:
        out["include_partition_value"] = data["IncludePartitionValue"]
    if "PartitionIncludeSchemaTable" in data:
        out["partition_include_schema_table"] = data["PartitionIncludeSchemaTable"]
    if "IncludeTableAlterOperations" in data:
        out["include_table_alter_operations"] = data["IncludeTableAlterOperations"]
    if "IncludeControlDetails" in data:
        out["include_control_details"] = data["IncludeControlDetails"]
    if "IncludeNullAndEmpty" in data:
        out["include_null_and_empty"] = data["IncludeNullAndEmpty"]
    if "NoHexPrefix" in data:
        out["no_hex_prefix"] = data["NoHexPrefix"]
    if "UseLargeIntegerValue" in data:
        out["use_large_integer_value"] = data["UseLargeIntegerValue"]
    return out
