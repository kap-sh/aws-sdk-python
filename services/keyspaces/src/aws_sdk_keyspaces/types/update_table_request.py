"""Generated from Smithy shape ``com.amazonaws.keyspaces#UpdateTableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.auto_scaling_specification
    import aws_sdk_keyspaces.types.capacity_specification
    import aws_sdk_keyspaces.types.cdc_specification
    import aws_sdk_keyspaces.types.client_side_timestamps
    import aws_sdk_keyspaces.types.column_definition_list
    import aws_sdk_keyspaces.types.default_time_to_live
    import aws_sdk_keyspaces.types.encryption_specification
    import aws_sdk_keyspaces.types.keyspace_name
    import aws_sdk_keyspaces.types.point_in_time_recovery
    import aws_sdk_keyspaces.types.replica_specification_list
    import aws_sdk_keyspaces.types.table_name
    import aws_sdk_keyspaces.types.time_to_live
    import aws_sdk_keyspaces.types.warm_throughput_specification


class UpdateTableRequest(TypedDict):
    keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace the specified table is stored in.</p>"""
    table_name: "aws_sdk_keyspaces.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    add_columns: NotRequired[
        "aws_sdk_keyspaces.types.column_definition_list.ColumnDefinitionList"
    ]
    r"""<p>For each column to be added to the specified table:</p> <ul> <li> <p> <code>name</code> - The name of the column.</p> </li> <li> <p> <code>type</code> - An Amazon Keyspaces data type. For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types\">Data types</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p> </li> </ul>"""
    capacity_specification: NotRequired[
        "aws_sdk_keyspaces.types.capacity_specification.CapacitySpecification"
    ]
    r"""<p>Modifies the read/write throughput capacity mode for the table. The options are:</p> <ul> <li> <p> <code>throughputMode:PAY_PER_REQUEST</code> and </p> </li> <li> <p> <code>throughputMode:PROVISIONED</code> - Provisioned capacity mode requires <code>readCapacityUnits</code> and <code>writeCapacityUnits</code> as input.</p> </li> </ul> <p>The default is <code>throughput_mode:PAY_PER_REQUEST</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html\">Read/write capacity modes</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    encryption_specification: NotRequired[
        "aws_sdk_keyspaces.types.encryption_specification.EncryptionSpecification"
    ]
    r"""<p>Modifies the encryption settings of the table. You can choose one of the following KMS key (KMS key):</p> <ul> <li> <p> <code>type:AWS_OWNED_KMS_KEY</code> - This key is owned by Amazon Keyspaces. </p> </li> <li> <p> <code>type:CUSTOMER_MANAGED_KMS_KEY</code> - This key is stored in your account and is created, owned, and managed by you. This option requires the <code>kms_key_identifier</code> of the KMS key in Amazon Resource Name (ARN) format as input. </p> </li> </ul> <p>The default is <code>AWS_OWNED_KMS_KEY</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html\">Encryption at rest</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    point_in_time_recovery: NotRequired[
        "aws_sdk_keyspaces.types.point_in_time_recovery.PointInTimeRecovery"
    ]
    r"""<p>Modifies the <code>pointInTimeRecovery</code> settings of the table. The options are:</p> <ul> <li> <p> <code>status=ENABLED</code> </p> </li> <li> <p> <code>status=DISABLED</code> </p> </li> </ul> <p>If it's not specified, the default is <code>status=DISABLED</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html\">Point-in-time recovery</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    ttl: NotRequired["aws_sdk_keyspaces.types.time_to_live.TimeToLive"]
    r"""<p>Modifies Time to Live custom settings for the table. The options are:</p> <ul> <li> <p> <code>status:enabled</code> </p> </li> <li> <p> <code>status:disabled</code> </p> </li> </ul> <p>The default is <code>status:disabled</code>. After <code>ttl</code> is enabled, you can't disable it for the table.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL.html\">Expiring data by using Amazon Keyspaces Time to Live (TTL)</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    default_time_to_live: NotRequired[
        "aws_sdk_keyspaces.types.default_time_to_live.DefaultTimeToLive"
    ]
    r"""<p>The default Time to Live setting in seconds for the table.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html#ttl-howitworks_default_ttl\">Setting the default TTL value for a table</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    client_side_timestamps: NotRequired[
        "aws_sdk_keyspaces.types.client_side_timestamps.ClientSideTimestamps"
    ]
    r"""<p>Enables client-side timestamps for the table. By default, the setting is disabled. You can enable client-side timestamps with the following option:</p> <ul> <li> <p> <code>status: \"enabled\"</code> </p> </li> </ul> <p>Once client-side timestamps are enabled for a table, this setting cannot be disabled.</p>"""
    auto_scaling_specification: NotRequired[
        "aws_sdk_keyspaces.types.auto_scaling_specification.AutoScalingSpecification"
    ]
    r"""<p>The optional auto scaling settings to update for a table in provisioned capacity mode. Specifies if the service can manage throughput capacity of a provisioned table automatically on your behalf. Amazon Keyspaces auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your table's read and write capacity automatically in response to application traffic.</p> <p>If auto scaling is already enabled for the table, you can use <code>UpdateTable</code> to update the minimum and maximum values or the auto scaling policy settings independently.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html\">Managing throughput capacity automatically with Amazon Keyspaces auto scaling</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    replica_specifications: NotRequired[
        "aws_sdk_keyspaces.types.replica_specification_list.ReplicaSpecificationList"
    ]
    """<p>The Region specific settings of a multi-Regional table.</p>"""
    cdc_specification: NotRequired[
        "aws_sdk_keyspaces.types.cdc_specification.CdcSpecification"
    ]
    """<p>The CDC stream settings of the table.</p>"""
    warm_throughput_specification: NotRequired[
        "aws_sdk_keyspaces.types.warm_throughput_specification.WarmThroughputSpecification"
    ]
    """<p>Modifies the warm throughput settings for the table. You can update the read and write capacity units to adjust the pre-provisioned throughput.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTableRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    if "add_columns" in value:
        import aws_sdk_keyspaces.types.column_definition_list

        out["addColumns"] = (
            aws_sdk_keyspaces.types.column_definition_list.serialize_aws_json_1_0(
                value["add_columns"]
            )
        )
    if "capacity_specification" in value:
        import aws_sdk_keyspaces.types.capacity_specification

        out["capacitySpecification"] = (
            aws_sdk_keyspaces.types.capacity_specification.serialize_aws_json_1_0(
                value["capacity_specification"]
            )
        )
    if "encryption_specification" in value:
        import aws_sdk_keyspaces.types.encryption_specification

        out["encryptionSpecification"] = (
            aws_sdk_keyspaces.types.encryption_specification.serialize_aws_json_1_0(
                value["encryption_specification"]
            )
        )
    if "point_in_time_recovery" in value:
        import aws_sdk_keyspaces.types.point_in_time_recovery

        out["pointInTimeRecovery"] = (
            aws_sdk_keyspaces.types.point_in_time_recovery.serialize_aws_json_1_0(
                value["point_in_time_recovery"]
            )
        )
    if "ttl" in value:
        import aws_sdk_keyspaces.types.time_to_live

        out["ttl"] = aws_sdk_keyspaces.types.time_to_live.serialize_aws_json_1_0(
            value["ttl"]
        )
    if "default_time_to_live" in value:
        out["defaultTimeToLive"] = value["default_time_to_live"]
    if "client_side_timestamps" in value:
        import aws_sdk_keyspaces.types.client_side_timestamps

        out["clientSideTimestamps"] = (
            aws_sdk_keyspaces.types.client_side_timestamps.serialize_aws_json_1_0(
                value["client_side_timestamps"]
            )
        )
    if "auto_scaling_specification" in value:
        import aws_sdk_keyspaces.types.auto_scaling_specification

        out["autoScalingSpecification"] = (
            aws_sdk_keyspaces.types.auto_scaling_specification.serialize_aws_json_1_0(
                value["auto_scaling_specification"]
            )
        )
    if "replica_specifications" in value:
        import aws_sdk_keyspaces.types.replica_specification_list

        out["replicaSpecifications"] = (
            aws_sdk_keyspaces.types.replica_specification_list.serialize_aws_json_1_0(
                value["replica_specifications"]
            )
        )
    if "cdc_specification" in value:
        import aws_sdk_keyspaces.types.cdc_specification

        out["cdcSpecification"] = (
            aws_sdk_keyspaces.types.cdc_specification.serialize_aws_json_1_0(
                value["cdc_specification"]
            )
        )
    if "warm_throughput_specification" in value:
        import aws_sdk_keyspaces.types.warm_throughput_specification

        out["warmThroughputSpecification"] = (
            aws_sdk_keyspaces.types.warm_throughput_specification.serialize_aws_json_1_0(
                value["warm_throughput_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTableRequest:
    out: UpdateTableRequest = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("UpdateTableRequest.keyspace_name required")
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("UpdateTableRequest.table_name required")
    if "addColumns" in data:
        import aws_sdk_keyspaces.types.column_definition_list

        out["add_columns"] = (
            aws_sdk_keyspaces.types.column_definition_list.deserialize_aws_json_1_0(
                data["addColumns"]
            )
        )
    if "capacitySpecification" in data:
        import aws_sdk_keyspaces.types.capacity_specification

        out["capacity_specification"] = (
            aws_sdk_keyspaces.types.capacity_specification.deserialize_aws_json_1_0(
                data["capacitySpecification"]
            )
        )
    if "encryptionSpecification" in data:
        import aws_sdk_keyspaces.types.encryption_specification

        out["encryption_specification"] = (
            aws_sdk_keyspaces.types.encryption_specification.deserialize_aws_json_1_0(
                data["encryptionSpecification"]
            )
        )
    if "pointInTimeRecovery" in data:
        import aws_sdk_keyspaces.types.point_in_time_recovery

        out["point_in_time_recovery"] = (
            aws_sdk_keyspaces.types.point_in_time_recovery.deserialize_aws_json_1_0(
                data["pointInTimeRecovery"]
            )
        )
    if "ttl" in data:
        import aws_sdk_keyspaces.types.time_to_live

        out["ttl"] = aws_sdk_keyspaces.types.time_to_live.deserialize_aws_json_1_0(
            data["ttl"]
        )
    if "defaultTimeToLive" in data:
        out["default_time_to_live"] = data["defaultTimeToLive"]
    if "clientSideTimestamps" in data:
        import aws_sdk_keyspaces.types.client_side_timestamps

        out["client_side_timestamps"] = (
            aws_sdk_keyspaces.types.client_side_timestamps.deserialize_aws_json_1_0(
                data["clientSideTimestamps"]
            )
        )
    if "autoScalingSpecification" in data:
        import aws_sdk_keyspaces.types.auto_scaling_specification

        out["auto_scaling_specification"] = (
            aws_sdk_keyspaces.types.auto_scaling_specification.deserialize_aws_json_1_0(
                data["autoScalingSpecification"]
            )
        )
    if "replicaSpecifications" in data:
        import aws_sdk_keyspaces.types.replica_specification_list

        out["replica_specifications"] = (
            aws_sdk_keyspaces.types.replica_specification_list.deserialize_aws_json_1_0(
                data["replicaSpecifications"]
            )
        )
    if "cdcSpecification" in data:
        import aws_sdk_keyspaces.types.cdc_specification

        out["cdc_specification"] = (
            aws_sdk_keyspaces.types.cdc_specification.deserialize_aws_json_1_0(
                data["cdcSpecification"]
            )
        )
    if "warmThroughputSpecification" in data:
        import aws_sdk_keyspaces.types.warm_throughput_specification

        out["warm_throughput_specification"] = (
            aws_sdk_keyspaces.types.warm_throughput_specification.deserialize_aws_json_1_0(
                data["warmThroughputSpecification"]
            )
        )
    return out
