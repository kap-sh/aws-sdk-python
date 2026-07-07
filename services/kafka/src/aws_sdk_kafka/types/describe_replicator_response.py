"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeReplicatorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean
    import aws_sdk_kafka.types.__list_of_kafka_cluster_description
    import aws_sdk_kafka.types.__list_of_replication_info_description
    import aws_sdk_kafka.types.__map_of__string
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.__timestamp_iso8601
    import aws_sdk_kafka.types.log_delivery
    import aws_sdk_kafka.types.replication_state_info
    import aws_sdk_kafka.types.replicator_state


class DescribeReplicatorResponse(TypedDict, closed=True):
    creation_time: NotRequired[
        "aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the replicator was created.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The current version number of the replicator.</p>"""
    is_replicator_reference: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>Whether this resource is a replicator reference.</p>"""
    kafka_clusters: NotRequired[
        "aws_sdk_kafka.types.__list_of_kafka_cluster_description.__listOfKafkaClusterDescription"
    ]
    """<p>Kafka Clusters used in setting up sources / targets for replication.</p>"""
    replication_info_list: NotRequired[
        "aws_sdk_kafka.types.__list_of_replication_info_description.__listOfReplicationInfoDescription"
    ]
    """<p>A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow.</p>"""
    replicator_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the replicator.</p>"""
    replicator_description: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The description of the replicator.</p>"""
    replicator_name: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The name of the replicator.</p>"""
    replicator_resource_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the replicator resource in the region where the replicator was created.</p>"""
    replicator_state: NotRequired[
        "aws_sdk_kafka.types.replicator_state.ReplicatorState"
    ]
    """<p>State of the replicator.</p>"""
    service_execution_role_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the IAM role used by the replicator to access resources in the customer's account (e.g source and target clusters)</p>"""
    state_info: NotRequired[
        "aws_sdk_kafka.types.replication_state_info.ReplicationStateInfo"
    ]
    """<p>Details about the state of the replicator.</p>"""
    tags: NotRequired["aws_sdk_kafka.types.__map_of__string.__mapOf__string"]
    """<p>List of tags attached to the Replicator.</p>"""
    log_delivery: NotRequired["aws_sdk_kafka.types.log_delivery.LogDelivery"]
    """<p>Configuration for log delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReplicatorResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creationTime"] = aws_sdk_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "is_replicator_reference" in value:
        out["isReplicatorReference"] = value["is_replicator_reference"]
    if "kafka_clusters" in value:
        import aws_sdk_kafka.types.__list_of_kafka_cluster_description

        out["kafkaClusters"] = (
            aws_sdk_kafka.types.__list_of_kafka_cluster_description.serialize_json(
                value["kafka_clusters"]
            )
        )
    if "replication_info_list" in value:
        import aws_sdk_kafka.types.__list_of_replication_info_description

        out["replicationInfoList"] = (
            aws_sdk_kafka.types.__list_of_replication_info_description.serialize_json(
                value["replication_info_list"]
            )
        )
    if "replicator_arn" in value:
        out["replicatorArn"] = value["replicator_arn"]
    if "replicator_description" in value:
        out["replicatorDescription"] = value["replicator_description"]
    if "replicator_name" in value:
        out["replicatorName"] = value["replicator_name"]
    if "replicator_resource_arn" in value:
        out["replicatorResourceArn"] = value["replicator_resource_arn"]
    if "replicator_state" in value:
        import aws_sdk_kafka.types.replicator_state

        out["replicatorState"] = aws_sdk_kafka.types.replicator_state.serialize_json(
            value["replicator_state"]
        )
    if "service_execution_role_arn" in value:
        out["serviceExecutionRoleArn"] = value["service_execution_role_arn"]
    if "state_info" in value:
        import aws_sdk_kafka.types.replication_state_info

        out["stateInfo"] = aws_sdk_kafka.types.replication_state_info.serialize_json(
            value["state_info"]
        )
    if "tags" in value:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.serialize_json(value["tags"])
    if "log_delivery" in value:
        import aws_sdk_kafka.types.log_delivery

        out["logDelivery"] = aws_sdk_kafka.types.log_delivery.serialize_json(
            value["log_delivery"]
        )
    return out


def deserialize_json(data: dict) -> DescribeReplicatorResponse:
    out: DescribeReplicatorResponse = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creation_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "isReplicatorReference" in data:
        out["is_replicator_reference"] = data["isReplicatorReference"]
    if "kafkaClusters" in data:
        import aws_sdk_kafka.types.__list_of_kafka_cluster_description

        out["kafka_clusters"] = (
            aws_sdk_kafka.types.__list_of_kafka_cluster_description.deserialize_json(
                data["kafkaClusters"]
            )
        )
    if "replicationInfoList" in data:
        import aws_sdk_kafka.types.__list_of_replication_info_description

        out["replication_info_list"] = (
            aws_sdk_kafka.types.__list_of_replication_info_description.deserialize_json(
                data["replicationInfoList"]
            )
        )
    if "replicatorArn" in data:
        out["replicator_arn"] = data["replicatorArn"]
    if "replicatorDescription" in data:
        out["replicator_description"] = data["replicatorDescription"]
    if "replicatorName" in data:
        out["replicator_name"] = data["replicatorName"]
    if "replicatorResourceArn" in data:
        out["replicator_resource_arn"] = data["replicatorResourceArn"]
    if "replicatorState" in data:
        import aws_sdk_kafka.types.replicator_state

        out["replicator_state"] = aws_sdk_kafka.types.replicator_state.deserialize_json(
            data["replicatorState"]
        )
    if "serviceExecutionRoleArn" in data:
        out["service_execution_role_arn"] = data["serviceExecutionRoleArn"]
    if "stateInfo" in data:
        import aws_sdk_kafka.types.replication_state_info

        out["state_info"] = aws_sdk_kafka.types.replication_state_info.deserialize_json(
            data["stateInfo"]
        )
    if "tags" in data:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if "logDelivery" in data:
        import aws_sdk_kafka.types.log_delivery

        out["log_delivery"] = aws_sdk_kafka.types.log_delivery.deserialize_json(
            data["logDelivery"]
        )
    return out
