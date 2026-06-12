"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KafkaSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.kafka_sasl_mechanism
    import aws_sdk_database_migration_service.types.kafka_security_protocol
    import aws_sdk_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm
    import aws_sdk_database_migration_service.types.message_format_value
    import aws_sdk_database_migration_service.types.secret_string
    import aws_sdk_database_migration_service.types.string


class KafkaSettings(TypedDict):
    broker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>A comma-separated list of one or more broker locations in your Kafka cluster that host your Kafka instance. Specify each broker location in the form <code> <i>broker-hostname-or-ip</i>:<i>port</i> </code>. For example, <code>\"ec2-12-345-678-901.compute-1.amazonaws.com:2345\"</code>. For more information and examples of specifying a list of broker locations, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html\">Using Apache Kafka as a target for Database Migration Service</a> in the <i>Database Migration Service User Guide</i>. </p>"""
    topic: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The topic to which you migrate the data. If you don't specify a topic, DMS specifies <code>\"kafka-default-topic\"</code> as the migration topic.</p>"""
    message_format: NotRequired[
        "aws_sdk_database_migration_service.types.message_format_value.MessageFormatValue"
    ]
    """<p>The output format for the records created on the endpoint. The message format is <code>JSON</code> (default) or <code>JSON_UNFORMATTED</code> (a single line with no tab).</p>"""
    include_transaction_details: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for <code>transaction_id</code>, previous <code>transaction_id</code>, and <code>transaction_record_id</code> (the record offset within a transaction). The default is <code>false</code>.</p>"""
    include_partition_value: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Shows the partition value within the Kafka message output unless the partition type is <code>schema-table-type</code>. The default is <code>false</code>.</p>"""
    partition_include_schema_table: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Prefixes schema and table names to partition values, when the partition type is <code>primary-key-type</code>. Doing this increases data distribution among Kafka partitions. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same partition, which causes throttling. The default is <code>false</code>.</p>"""
    include_table_alter_operations: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Includes any data definition language (DDL) operations that change the table in the control data, such as <code>rename-table</code>, <code>drop-table</code>, <code>add-column</code>, <code>drop-column</code>, and <code>rename-column</code>. The default is <code>false</code>.</p>"""
    include_control_details: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Shows detailed control information for table definition, column definition, and table and column changes in the Kafka message output. The default is <code>false</code>.</p>"""
    message_max_bytes: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum size in bytes for records created on the endpoint The default is 1,000,000.</p>"""
    include_null_and_empty: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Include NULL and empty columns for records migrated to the endpoint. The default is <code>false</code>.</p>"""
    security_protocol: NotRequired[
        "aws_sdk_database_migration_service.types.kafka_security_protocol.KafkaSecurityProtocol"
    ]
    """<p>Set secure connection to a Kafka target endpoint using Transport Layer Security (TLS). Options include <code>ssl-encryption</code>, <code>ssl-authentication</code>, and <code>sasl-ssl</code>. <code>sasl-ssl</code> requires <code>SaslUsername</code> and <code>SaslPassword</code>.</p>"""
    ssl_client_certificate_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the client certificate used to securely connect to a Kafka target endpoint.</p>"""
    ssl_client_key_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) for the client private key used to securely connect to a Kafka target endpoint.</p>"""
    ssl_client_key_password: NotRequired[
        "aws_sdk_database_migration_service.types.secret_string.SecretString"
    ]
    """<p> The password for the client private key used to securely connect to a Kafka target endpoint.</p>"""
    ssl_ca_certificate_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p> The Amazon Resource Name (ARN) for the private certificate authority (CA) cert that DMS uses to securely connect to your Kafka target endpoint.</p>"""
    sasl_username: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> The secure user name you created when you first set up your MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.</p>"""
    sasl_password: NotRequired[
        "aws_sdk_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>The secure password you created when you first set up your MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.</p>"""
    no_hex_prefix: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this optional parameter to <code>true</code> to avoid adding a '0x' prefix to raw data in hexadecimal format. For example, by default, DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to a Kafka target. Use the <code>NoHexPrefix</code> endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.</p>"""
    sasl_mechanism: NotRequired[
        "aws_sdk_database_migration_service.types.kafka_sasl_mechanism.KafkaSaslMechanism"
    ]
    """<p>For SASL/SSL authentication, DMS supports the <code>SCRAM-SHA-512</code> mechanism by default. DMS versions 3.5.0 and later also support the <code>PLAIN</code> mechanism. To use the <code>PLAIN</code> mechanism, set this parameter to <code>PLAIN.</code> </p>"""
    ssl_endpoint_identification_algorithm: NotRequired[
        "aws_sdk_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm.KafkaSslEndpointIdentificationAlgorithm"
    ]
    """<p>Sets hostname verification for the certificate. This setting is supported in DMS version 3.5.1 and later. </p>"""
    use_large_integer_value: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies using the large integer value with Kafka.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KafkaSettings) -> dict:
    out: dict = {}
    if "broker" in value:
        out["Broker"] = value["broker"]
    if "topic" in value:
        out["Topic"] = value["topic"]
    if "message_format" in value:
        import aws_sdk_database_migration_service.types.message_format_value

        out["MessageFormat"] = (
            aws_sdk_database_migration_service.types.message_format_value.serialize_aws_json_1_1(
                value["message_format"]
            )
        )
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
    if "message_max_bytes" in value:
        out["MessageMaxBytes"] = value["message_max_bytes"]
    if "include_null_and_empty" in value:
        out["IncludeNullAndEmpty"] = value["include_null_and_empty"]
    if "security_protocol" in value:
        import aws_sdk_database_migration_service.types.kafka_security_protocol

        out["SecurityProtocol"] = (
            aws_sdk_database_migration_service.types.kafka_security_protocol.serialize_aws_json_1_1(
                value["security_protocol"]
            )
        )
    if "ssl_client_certificate_arn" in value:
        out["SslClientCertificateArn"] = value["ssl_client_certificate_arn"]
    if "ssl_client_key_arn" in value:
        out["SslClientKeyArn"] = value["ssl_client_key_arn"]
    if "ssl_client_key_password" in value:
        out["SslClientKeyPassword"] = value["ssl_client_key_password"]
    if "ssl_ca_certificate_arn" in value:
        out["SslCaCertificateArn"] = value["ssl_ca_certificate_arn"]
    if "sasl_username" in value:
        out["SaslUsername"] = value["sasl_username"]
    if "sasl_password" in value:
        out["SaslPassword"] = value["sasl_password"]
    if "no_hex_prefix" in value:
        out["NoHexPrefix"] = value["no_hex_prefix"]
    if "sasl_mechanism" in value:
        import aws_sdk_database_migration_service.types.kafka_sasl_mechanism

        out["SaslMechanism"] = (
            aws_sdk_database_migration_service.types.kafka_sasl_mechanism.serialize_aws_json_1_1(
                value["sasl_mechanism"]
            )
        )
    if "ssl_endpoint_identification_algorithm" in value:
        import aws_sdk_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm

        out["SslEndpointIdentificationAlgorithm"] = (
            aws_sdk_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm.serialize_aws_json_1_1(
                value["ssl_endpoint_identification_algorithm"]
            )
        )
    if "use_large_integer_value" in value:
        out["UseLargeIntegerValue"] = value["use_large_integer_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KafkaSettings:
    out: KafkaSettings = {}  # type: ignore[typeddict-item]
    if "Broker" in data:
        out["broker"] = data["Broker"]
    if "Topic" in data:
        out["topic"] = data["Topic"]
    if "MessageFormat" in data:
        import aws_sdk_database_migration_service.types.message_format_value

        out["message_format"] = (
            aws_sdk_database_migration_service.types.message_format_value.deserialize_aws_json_1_1(
                data["MessageFormat"]
            )
        )
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
    if "MessageMaxBytes" in data:
        out["message_max_bytes"] = data["MessageMaxBytes"]
    if "IncludeNullAndEmpty" in data:
        out["include_null_and_empty"] = data["IncludeNullAndEmpty"]
    if "SecurityProtocol" in data:
        import aws_sdk_database_migration_service.types.kafka_security_protocol

        out["security_protocol"] = (
            aws_sdk_database_migration_service.types.kafka_security_protocol.deserialize_aws_json_1_1(
                data["SecurityProtocol"]
            )
        )
    if "SslClientCertificateArn" in data:
        out["ssl_client_certificate_arn"] = data["SslClientCertificateArn"]
    if "SslClientKeyArn" in data:
        out["ssl_client_key_arn"] = data["SslClientKeyArn"]
    if "SslClientKeyPassword" in data:
        out["ssl_client_key_password"] = data["SslClientKeyPassword"]
    if "SslCaCertificateArn" in data:
        out["ssl_ca_certificate_arn"] = data["SslCaCertificateArn"]
    if "SaslUsername" in data:
        out["sasl_username"] = data["SaslUsername"]
    if "SaslPassword" in data:
        out["sasl_password"] = data["SaslPassword"]
    if "NoHexPrefix" in data:
        out["no_hex_prefix"] = data["NoHexPrefix"]
    if "SaslMechanism" in data:
        import aws_sdk_database_migration_service.types.kafka_sasl_mechanism

        out["sasl_mechanism"] = (
            aws_sdk_database_migration_service.types.kafka_sasl_mechanism.deserialize_aws_json_1_1(
                data["SaslMechanism"]
            )
        )
    if "SslEndpointIdentificationAlgorithm" in data:
        import aws_sdk_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm

        out["ssl_endpoint_identification_algorithm"] = (
            aws_sdk_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm.deserialize_aws_json_1_1(
                data["SslEndpointIdentificationAlgorithm"]
            )
        )
    if "UseLargeIntegerValue" in data:
        out["use_large_integer_value"] = data["UseLargeIntegerValue"]
    return out
