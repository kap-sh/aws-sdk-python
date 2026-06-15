"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.boolean_object
    import aws_sdk_kinesis.types.encryption_type
    import aws_sdk_kinesis.types.enhanced_monitoring_list
    import aws_sdk_kinesis.types.key_id
    import aws_sdk_kinesis.types.retention_period_hours
    import aws_sdk_kinesis.types.shard_list
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_mode_details
    import aws_sdk_kinesis.types.stream_name
    import aws_sdk_kinesis.types.stream_status
    import aws_sdk_kinesis.types.timestamp


class StreamDescription(TypedDict):
    stream_name: "aws_sdk_kinesis.types.stream_name.StreamName"
    """<p>The name of the stream being described.</p>"""
    stream_arn: "aws_sdk_kinesis.types.stream_arn.StreamARN"
    """<p>The Amazon Resource Name (ARN) for the stream being described.</p>"""
    stream_status: "aws_sdk_kinesis.types.stream_status.StreamStatus"
    """<p>The current status of the stream being described. The stream status is one of the following states:</p> <ul> <li> <p> <code>CREATING</code> - The stream is being created. Kinesis Data Streams immediately returns and sets <code>StreamStatus</code> to <code>CREATING</code>.</p> </li> <li> <p> <code>DELETING</code> - The stream is being deleted. The specified stream is in the <code>DELETING</code> state until Kinesis Data Streams completes the deletion.</p> </li> <li> <p> <code>ACTIVE</code> - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an <code>ACTIVE</code> stream.</p> </li> <li> <p> <code>UPDATING</code> - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the <code>UPDATING</code> state.</p> </li> </ul>"""
    stream_mode_details: NotRequired[
        "aws_sdk_kinesis.types.stream_mode_details.StreamModeDetails"
    ]
    """<p> Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an <b>on-demand</b> capacity mode and a <b>provisioned</b> capacity mode for your data streams. </p>"""
    shards: "aws_sdk_kinesis.types.shard_list.ShardList"
    """<p>The shards that comprise the stream.</p>"""
    has_more_shards: "aws_sdk_kinesis.types.boolean_object.BooleanObject"
    """<p>If set to <code>true</code>, more shards in the stream are available to describe.</p>"""
    retention_period_hours: (
        "aws_sdk_kinesis.types.retention_period_hours.RetentionPeriodHours"
    )
    """<p>The current retention period, in hours. Minimum value of 24. Maximum value of 168.</p>"""
    stream_creation_timestamp: "aws_sdk_kinesis.types.timestamp.Timestamp"
    """<p>The approximate time that the stream was created.</p>"""
    enhanced_monitoring: (
        "aws_sdk_kinesis.types.enhanced_monitoring_list.EnhancedMonitoringList"
    )
    """<p>Represents the current enhanced monitoring settings of the stream.</p>"""
    encryption_type: NotRequired["aws_sdk_kinesis.types.encryption_type.EncryptionType"]
    """<p>The server-side encryption type used on the stream. This parameter can be one of the following values:</p> <ul> <li> <p> <code>NONE</code>: Do not encrypt the records in the stream.</p> </li> <li> <p> <code>KMS</code>: Use server-side encryption on the records in the stream using a customer-managed Amazon Web Services KMS key.</p> </li> </ul>"""
    key_id: NotRequired["aws_sdk_kinesis.types.key_id.KeyId"]
    r"""<p>The GUID for the customer-managed Amazon Web Services KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by \"alias/\".You can also use a master key owned by Kinesis Data Streams by specifying the alias <code>aws/kinesis</code>.</p> <ul> <li> <p>Key ARN example: <code>arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias ARN example: <code>arn:aws:kms:us-east-1:123456789012:alias/MyAliasName</code> </p> </li> <li> <p>Globally unique key ID example: <code>12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias name example: <code>alias/MyAliasName</code> </p> </li> <li> <p>Master key owned by Kinesis Data Streams: <code>alias/aws/kinesis</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamDescription) -> dict:
    out: dict = {}
    out["StreamName"] = value["stream_name"]
    out["StreamARN"] = value["stream_arn"]
    import aws_sdk_kinesis.types.stream_status

    out["StreamStatus"] = aws_sdk_kinesis.types.stream_status.serialize_aws_json_1_1(
        value["stream_status"]
    )
    if "stream_mode_details" in value:
        import aws_sdk_kinesis.types.stream_mode_details

        out["StreamModeDetails"] = (
            aws_sdk_kinesis.types.stream_mode_details.serialize_aws_json_1_1(
                value["stream_mode_details"]
            )
        )
    import aws_sdk_kinesis.types.shard_list

    out["Shards"] = aws_sdk_kinesis.types.shard_list.serialize_aws_json_1_1(
        value["shards"]
    )
    out["HasMoreShards"] = value["has_more_shards"]
    out["RetentionPeriodHours"] = value["retention_period_hours"]
    import aws_sdk_kinesis.types.timestamp

    out["StreamCreationTimestamp"] = (
        aws_sdk_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["stream_creation_timestamp"]
        )
    )
    import aws_sdk_kinesis.types.enhanced_monitoring_list

    out["EnhancedMonitoring"] = (
        aws_sdk_kinesis.types.enhanced_monitoring_list.serialize_aws_json_1_1(
            value["enhanced_monitoring"]
        )
    )
    if "encryption_type" in value:
        import aws_sdk_kinesis.types.encryption_type

        out["EncryptionType"] = (
            aws_sdk_kinesis.types.encryption_type.serialize_aws_json_1_1(
                value["encryption_type"]
            )
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamDescription:
    out: StreamDescription = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    else:
        raise DeserializationError("StreamDescription.stream_name required")
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    else:
        raise DeserializationError("StreamDescription.stream_arn required")
    if "StreamStatus" in data:
        import aws_sdk_kinesis.types.stream_status

        out["stream_status"] = (
            aws_sdk_kinesis.types.stream_status.deserialize_aws_json_1_1(
                data["StreamStatus"]
            )
        )
    else:
        raise DeserializationError("StreamDescription.stream_status required")
    if "StreamModeDetails" in data:
        import aws_sdk_kinesis.types.stream_mode_details

        out["stream_mode_details"] = (
            aws_sdk_kinesis.types.stream_mode_details.deserialize_aws_json_1_1(
                data["StreamModeDetails"]
            )
        )
    if "Shards" in data:
        import aws_sdk_kinesis.types.shard_list

        out["shards"] = aws_sdk_kinesis.types.shard_list.deserialize_aws_json_1_1(
            data["Shards"]
        )
    else:
        raise DeserializationError("StreamDescription.shards required")
    if "HasMoreShards" in data:
        out["has_more_shards"] = data["HasMoreShards"]
    else:
        raise DeserializationError("StreamDescription.has_more_shards required")
    if "RetentionPeriodHours" in data:
        out["retention_period_hours"] = data["RetentionPeriodHours"]
    else:
        raise DeserializationError("StreamDescription.retention_period_hours required")
    if "StreamCreationTimestamp" in data:
        import aws_sdk_kinesis.types.timestamp

        out["stream_creation_timestamp"] = (
            aws_sdk_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["StreamCreationTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "StreamDescription.stream_creation_timestamp required"
        )
    if "EnhancedMonitoring" in data:
        import aws_sdk_kinesis.types.enhanced_monitoring_list

        out["enhanced_monitoring"] = (
            aws_sdk_kinesis.types.enhanced_monitoring_list.deserialize_aws_json_1_1(
                data["EnhancedMonitoring"]
            )
        )
    else:
        raise DeserializationError("StreamDescription.enhanced_monitoring required")
    if "EncryptionType" in data:
        import aws_sdk_kinesis.types.encryption_type

        out["encryption_type"] = (
            aws_sdk_kinesis.types.encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    return out
