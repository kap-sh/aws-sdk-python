"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.arn
    import aws_sdk_keyspaces.types.capacity_specification_summary
    import aws_sdk_keyspaces.types.cdc_specification_summary
    import aws_sdk_keyspaces.types.client_side_timestamps
    import aws_sdk_keyspaces.types.comment
    import aws_sdk_keyspaces.types.default_time_to_live
    import aws_sdk_keyspaces.types.encryption_specification
    import aws_sdk_keyspaces.types.keyspace_name
    import aws_sdk_keyspaces.types.point_in_time_recovery_summary
    import aws_sdk_keyspaces.types.replica_specification_summary_list
    import aws_sdk_keyspaces.types.schema_definition
    import aws_sdk_keyspaces.types.stream_arn
    import aws_sdk_keyspaces.types.table_name
    import aws_sdk_keyspaces.types.table_status
    import aws_sdk_keyspaces.types.time_to_live
    import aws_sdk_keyspaces.types.timestamp
    import aws_sdk_keyspaces.types.warm_throughput_specification_summary


class GetTableResponse(TypedDict, closed=True):
    keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace that the specified table is stored in.</p>"""
    table_name: "aws_sdk_keyspaces.types.table_name.TableName"
    """<p>The name of the specified table.</p>"""
    resource_arn: "aws_sdk_keyspaces.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the specified table.</p>"""
    creation_timestamp: NotRequired["aws_sdk_keyspaces.types.timestamp.Timestamp"]
    """<p>The creation timestamp of the specified table.</p>"""
    status: NotRequired["aws_sdk_keyspaces.types.table_status.TableStatus"]
    """<p>The current status of the specified table.</p>"""
    schema_definition: NotRequired[
        "aws_sdk_keyspaces.types.schema_definition.SchemaDefinition"
    ]
    """<p>The schema definition of the specified table.</p>"""
    capacity_specification: NotRequired[
        "aws_sdk_keyspaces.types.capacity_specification_summary.CapacitySpecificationSummary"
    ]
    """<p>The read/write throughput capacity mode for a table. The options are:</p> <ul> <li> <p> <code>throughputMode:PAY_PER_REQUEST</code> </p> </li> <li> <p> <code>throughputMode:PROVISIONED</code> </p> </li> </ul>"""
    encryption_specification: NotRequired[
        "aws_sdk_keyspaces.types.encryption_specification.EncryptionSpecification"
    ]
    """<p>The encryption settings of the specified table.</p>"""
    point_in_time_recovery: NotRequired[
        "aws_sdk_keyspaces.types.point_in_time_recovery_summary.PointInTimeRecoverySummary"
    ]
    """<p>The point-in-time recovery status of the specified table.</p>"""
    ttl: NotRequired["aws_sdk_keyspaces.types.time_to_live.TimeToLive"]
    """<p>The custom Time to Live settings of the specified table.</p>"""
    default_time_to_live: NotRequired[
        "aws_sdk_keyspaces.types.default_time_to_live.DefaultTimeToLive"
    ]
    """<p>The default Time to Live settings in seconds of the specified table.</p>"""
    comment: NotRequired["aws_sdk_keyspaces.types.comment.Comment"]
    """<p>The the description of the specified table.</p>"""
    client_side_timestamps: NotRequired[
        "aws_sdk_keyspaces.types.client_side_timestamps.ClientSideTimestamps"
    ]
    """<p> The client-side timestamps setting of the table.</p>"""
    replica_specifications: NotRequired[
        "aws_sdk_keyspaces.types.replica_specification_summary_list.ReplicaSpecificationSummaryList"
    ]
    """<p>Returns the Amazon Web Services Region specific settings of all Regions a multi-Region table is replicated in.</p>"""
    latest_stream_arn: NotRequired["aws_sdk_keyspaces.types.stream_arn.StreamArn"]
    """<p>The Amazon Resource Name (ARN) of the stream.</p>"""
    cdc_specification: NotRequired[
        "aws_sdk_keyspaces.types.cdc_specification_summary.CdcSpecificationSummary"
    ]
    """<p>The CDC stream settings of the table.</p>"""
    warm_throughput_specification: NotRequired[
        "aws_sdk_keyspaces.types.warm_throughput_specification_summary.WarmThroughputSpecificationSummary"
    ]
    """<p>The warm throughput settings for the table, including the current status and configured read and write capacity units.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTableResponse) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    out["resourceArn"] = value["resource_arn"]
    if "creation_timestamp" in value:
        import aws_sdk_keyspaces.types.timestamp

        out["creationTimestamp"] = (
            aws_sdk_keyspaces.types.timestamp.serialize_aws_json_1_0(
                value["creation_timestamp"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "schema_definition" in value:
        import aws_sdk_keyspaces.types.schema_definition

        out["schemaDefinition"] = (
            aws_sdk_keyspaces.types.schema_definition.serialize_aws_json_1_0(
                value["schema_definition"]
            )
        )
    if "capacity_specification" in value:
        import aws_sdk_keyspaces.types.capacity_specification_summary

        out["capacitySpecification"] = (
            aws_sdk_keyspaces.types.capacity_specification_summary.serialize_aws_json_1_0(
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
        import aws_sdk_keyspaces.types.point_in_time_recovery_summary

        out["pointInTimeRecovery"] = (
            aws_sdk_keyspaces.types.point_in_time_recovery_summary.serialize_aws_json_1_0(
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
    if "comment" in value:
        import aws_sdk_keyspaces.types.comment

        out["comment"] = aws_sdk_keyspaces.types.comment.serialize_aws_json_1_0(
            value["comment"]
        )
    if "client_side_timestamps" in value:
        import aws_sdk_keyspaces.types.client_side_timestamps

        out["clientSideTimestamps"] = (
            aws_sdk_keyspaces.types.client_side_timestamps.serialize_aws_json_1_0(
                value["client_side_timestamps"]
            )
        )
    if "replica_specifications" in value:
        import aws_sdk_keyspaces.types.replica_specification_summary_list

        out["replicaSpecifications"] = (
            aws_sdk_keyspaces.types.replica_specification_summary_list.serialize_aws_json_1_0(
                value["replica_specifications"]
            )
        )
    if "latest_stream_arn" in value:
        out["latestStreamArn"] = value["latest_stream_arn"]
    if "cdc_specification" in value:
        import aws_sdk_keyspaces.types.cdc_specification_summary

        out["cdcSpecification"] = (
            aws_sdk_keyspaces.types.cdc_specification_summary.serialize_aws_json_1_0(
                value["cdc_specification"]
            )
        )
    if "warm_throughput_specification" in value:
        import aws_sdk_keyspaces.types.warm_throughput_specification_summary

        out["warmThroughputSpecification"] = (
            aws_sdk_keyspaces.types.warm_throughput_specification_summary.serialize_aws_json_1_0(
                value["warm_throughput_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTableResponse:
    out: GetTableResponse = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("GetTableResponse.keyspace_name required")
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("GetTableResponse.table_name required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("GetTableResponse.resource_arn required")
    if "creationTimestamp" in data:
        import aws_sdk_keyspaces.types.timestamp

        out["creation_timestamp"] = (
            aws_sdk_keyspaces.types.timestamp.deserialize_aws_json_1_0(
                data["creationTimestamp"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "schemaDefinition" in data:
        import aws_sdk_keyspaces.types.schema_definition

        out["schema_definition"] = (
            aws_sdk_keyspaces.types.schema_definition.deserialize_aws_json_1_0(
                data["schemaDefinition"]
            )
        )
    if "capacitySpecification" in data:
        import aws_sdk_keyspaces.types.capacity_specification_summary

        out["capacity_specification"] = (
            aws_sdk_keyspaces.types.capacity_specification_summary.deserialize_aws_json_1_0(
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
        import aws_sdk_keyspaces.types.point_in_time_recovery_summary

        out["point_in_time_recovery"] = (
            aws_sdk_keyspaces.types.point_in_time_recovery_summary.deserialize_aws_json_1_0(
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
    if "comment" in data:
        import aws_sdk_keyspaces.types.comment

        out["comment"] = aws_sdk_keyspaces.types.comment.deserialize_aws_json_1_0(
            data["comment"]
        )
    if "clientSideTimestamps" in data:
        import aws_sdk_keyspaces.types.client_side_timestamps

        out["client_side_timestamps"] = (
            aws_sdk_keyspaces.types.client_side_timestamps.deserialize_aws_json_1_0(
                data["clientSideTimestamps"]
            )
        )
    if "replicaSpecifications" in data:
        import aws_sdk_keyspaces.types.replica_specification_summary_list

        out["replica_specifications"] = (
            aws_sdk_keyspaces.types.replica_specification_summary_list.deserialize_aws_json_1_0(
                data["replicaSpecifications"]
            )
        )
    if "latestStreamArn" in data:
        out["latest_stream_arn"] = data["latestStreamArn"]
    if "cdcSpecification" in data:
        import aws_sdk_keyspaces.types.cdc_specification_summary

        out["cdc_specification"] = (
            aws_sdk_keyspaces.types.cdc_specification_summary.deserialize_aws_json_1_0(
                data["cdcSpecification"]
            )
        )
    if "warmThroughputSpecification" in data:
        import aws_sdk_keyspaces.types.warm_throughput_specification_summary

        out["warm_throughput_specification"] = (
            aws_sdk_keyspaces.types.warm_throughput_specification_summary.deserialize_aws_json_1_0(
                data["warmThroughputSpecification"]
            )
        )
    return out
