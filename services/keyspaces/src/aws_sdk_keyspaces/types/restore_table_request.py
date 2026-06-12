"""Generated from Smithy shape ``com.amazonaws.keyspaces#RestoreTableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.auto_scaling_specification
    import aws_sdk_keyspaces.types.capacity_specification
    import aws_sdk_keyspaces.types.encryption_specification
    import aws_sdk_keyspaces.types.keyspace_name
    import aws_sdk_keyspaces.types.point_in_time_recovery
    import aws_sdk_keyspaces.types.replica_specification_list
    import aws_sdk_keyspaces.types.table_name
    import aws_sdk_keyspaces.types.tag_list
    import aws_sdk_keyspaces.types.timestamp


class RestoreTableRequest(TypedDict):
    source_keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The keyspace name of the source table.</p>"""
    source_table_name: "aws_sdk_keyspaces.types.table_name.TableName"
    """<p>The name of the source table.</p>"""
    target_keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the target keyspace.</p>"""
    target_table_name: "aws_sdk_keyspaces.types.table_name.TableName"
    """<p>The name of the target table.</p>"""
    restore_timestamp: NotRequired["aws_sdk_keyspaces.types.timestamp.Timestamp"]
    """<p>The restore timestamp in ISO 8601 format.</p>"""
    capacity_specification_override: NotRequired[
        "aws_sdk_keyspaces.types.capacity_specification.CapacitySpecification"
    ]
    """<p>Specifies the read/write throughput capacity mode for the target table. The options are:</p> <ul> <li> <p> <code>throughputMode:PAY_PER_REQUEST</code> </p> </li> <li> <p> <code>throughputMode:PROVISIONED</code> - Provisioned capacity mode requires <code>readCapacityUnits</code> and <code>writeCapacityUnits</code> as input.</p> </li> </ul> <p>The default is <code>throughput_mode:PAY_PER_REQUEST</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html\">Read/write capacity modes</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    encryption_specification_override: NotRequired[
        "aws_sdk_keyspaces.types.encryption_specification.EncryptionSpecification"
    ]
    """<p>Specifies the encryption settings for the target table. You can choose one of the following KMS key (KMS key):</p> <ul> <li> <p> <code>type:AWS_OWNED_KMS_KEY</code> - This key is owned by Amazon Keyspaces. </p> </li> <li> <p> <code>type:CUSTOMER_MANAGED_KMS_KEY</code> - This key is stored in your account and is created, owned, and managed by you. This option requires the <code>kms_key_identifier</code> of the KMS key in Amazon Resource Name (ARN) format as input. </p> </li> </ul> <p>The default is <code>type:AWS_OWNED_KMS_KEY</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html\">Encryption at rest</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    point_in_time_recovery_override: NotRequired[
        "aws_sdk_keyspaces.types.point_in_time_recovery.PointInTimeRecovery"
    ]
    """<p>Specifies the <code>pointInTimeRecovery</code> settings for the target table. The options are:</p> <ul> <li> <p> <code>status=ENABLED</code> </p> </li> <li> <p> <code>status=DISABLED</code> </p> </li> </ul> <p>If it's not specified, the default is <code>status=DISABLED</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html\">Point-in-time recovery</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    tags_override: NotRequired["aws_sdk_keyspaces.types.tag_list.TagList"]
    """<p>A list of key-value pair tags to be attached to the restored table. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html\">Adding tags and labels to Amazon Keyspaces resources</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    auto_scaling_specification: NotRequired[
        "aws_sdk_keyspaces.types.auto_scaling_specification.AutoScalingSpecification"
    ]
    """<p>The optional auto scaling settings for the restored table in provisioned capacity mode. Specifies if the service can manage throughput capacity of a provisioned table automatically on your behalf. Amazon Keyspaces auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your table's read and write capacity automatically in response to application traffic.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html\">Managing throughput capacity automatically with Amazon Keyspaces auto scaling</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    replica_specifications: NotRequired[
        "aws_sdk_keyspaces.types.replica_specification_list.ReplicaSpecificationList"
    ]
    """<p>The optional Region specific settings of a multi-Regional table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreTableRequest) -> dict:
    out: dict = {}
    out["sourceKeyspaceName"] = value["source_keyspace_name"]
    out["sourceTableName"] = value["source_table_name"]
    out["targetKeyspaceName"] = value["target_keyspace_name"]
    out["targetTableName"] = value["target_table_name"]
    if "restore_timestamp" in value:
        import aws_sdk_keyspaces.types.timestamp

        out["restoreTimestamp"] = (
            aws_sdk_keyspaces.types.timestamp.serialize_aws_json_1_0(
                value["restore_timestamp"]
            )
        )
    if "capacity_specification_override" in value:
        import aws_sdk_keyspaces.types.capacity_specification

        out["capacitySpecificationOverride"] = (
            aws_sdk_keyspaces.types.capacity_specification.serialize_aws_json_1_0(
                value["capacity_specification_override"]
            )
        )
    if "encryption_specification_override" in value:
        import aws_sdk_keyspaces.types.encryption_specification

        out["encryptionSpecificationOverride"] = (
            aws_sdk_keyspaces.types.encryption_specification.serialize_aws_json_1_0(
                value["encryption_specification_override"]
            )
        )
    if "point_in_time_recovery_override" in value:
        import aws_sdk_keyspaces.types.point_in_time_recovery

        out["pointInTimeRecoveryOverride"] = (
            aws_sdk_keyspaces.types.point_in_time_recovery.serialize_aws_json_1_0(
                value["point_in_time_recovery_override"]
            )
        )
    if "tags_override" in value:
        import aws_sdk_keyspaces.types.tag_list

        out["tagsOverride"] = aws_sdk_keyspaces.types.tag_list.serialize_aws_json_1_0(
            value["tags_override"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreTableRequest:
    out: RestoreTableRequest = {}  # type: ignore[typeddict-item]
    if "sourceKeyspaceName" in data:
        out["source_keyspace_name"] = data["sourceKeyspaceName"]
    else:
        raise DeserializationError("RestoreTableRequest.source_keyspace_name required")
    if "sourceTableName" in data:
        out["source_table_name"] = data["sourceTableName"]
    else:
        raise DeserializationError("RestoreTableRequest.source_table_name required")
    if "targetKeyspaceName" in data:
        out["target_keyspace_name"] = data["targetKeyspaceName"]
    else:
        raise DeserializationError("RestoreTableRequest.target_keyspace_name required")
    if "targetTableName" in data:
        out["target_table_name"] = data["targetTableName"]
    else:
        raise DeserializationError("RestoreTableRequest.target_table_name required")
    if "restoreTimestamp" in data:
        import aws_sdk_keyspaces.types.timestamp

        out["restore_timestamp"] = (
            aws_sdk_keyspaces.types.timestamp.deserialize_aws_json_1_0(
                data["restoreTimestamp"]
            )
        )
    if "capacitySpecificationOverride" in data:
        import aws_sdk_keyspaces.types.capacity_specification

        out["capacity_specification_override"] = (
            aws_sdk_keyspaces.types.capacity_specification.deserialize_aws_json_1_0(
                data["capacitySpecificationOverride"]
            )
        )
    if "encryptionSpecificationOverride" in data:
        import aws_sdk_keyspaces.types.encryption_specification

        out["encryption_specification_override"] = (
            aws_sdk_keyspaces.types.encryption_specification.deserialize_aws_json_1_0(
                data["encryptionSpecificationOverride"]
            )
        )
    if "pointInTimeRecoveryOverride" in data:
        import aws_sdk_keyspaces.types.point_in_time_recovery

        out["point_in_time_recovery_override"] = (
            aws_sdk_keyspaces.types.point_in_time_recovery.deserialize_aws_json_1_0(
                data["pointInTimeRecoveryOverride"]
            )
        )
    if "tagsOverride" in data:
        import aws_sdk_keyspaces.types.tag_list

        out["tags_override"] = (
            aws_sdk_keyspaces.types.tag_list.deserialize_aws_json_1_0(
                data["tagsOverride"]
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
    return out
