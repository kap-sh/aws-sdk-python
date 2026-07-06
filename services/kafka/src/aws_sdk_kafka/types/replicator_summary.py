"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicatorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean
    import aws_sdk_kafka.types.__list_of_kafka_cluster_summary
    import aws_sdk_kafka.types.__list_of_replication_info_summary
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.__timestamp_iso8601
    import aws_sdk_kafka.types.replicator_state


class ReplicatorSummary(TypedDict, closed=True):
    creation_time: NotRequired[
        "aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time the replicator was created.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The current version of the replicator.</p>"""
    is_replicator_reference: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>Whether this resource is a replicator reference.</p>"""
    kafka_clusters_summary: NotRequired[
        "aws_sdk_kafka.types.__list_of_kafka_cluster_summary.__listOfKafkaClusterSummary"
    ]
    """<p>Kafka Clusters used in setting up sources / targets for replication.</p>"""
    replication_info_summary_list: NotRequired[
        "aws_sdk_kafka.types.__list_of_replication_info_summary.__listOfReplicationInfoSummary"
    ]
    """<p>A list of summarized information of replications between clusters.</p>"""
    replicator_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the replicator.</p>"""
    replicator_name: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The name of the replicator.</p>"""
    replicator_resource_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the replicator resource in the region where the replicator was created.</p>"""
    replicator_state: NotRequired[
        "aws_sdk_kafka.types.replicator_state.ReplicatorState"
    ]
    """<p>State of the replicator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicatorSummary) -> dict:
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
    if "kafka_clusters_summary" in value:
        import aws_sdk_kafka.types.__list_of_kafka_cluster_summary

        out["kafkaClustersSummary"] = (
            aws_sdk_kafka.types.__list_of_kafka_cluster_summary.serialize_json(
                value["kafka_clusters_summary"]
            )
        )
    if "replication_info_summary_list" in value:
        import aws_sdk_kafka.types.__list_of_replication_info_summary

        out["replicationInfoSummaryList"] = (
            aws_sdk_kafka.types.__list_of_replication_info_summary.serialize_json(
                value["replication_info_summary_list"]
            )
        )
    if "replicator_arn" in value:
        out["replicatorArn"] = value["replicator_arn"]
    if "replicator_name" in value:
        out["replicatorName"] = value["replicator_name"]
    if "replicator_resource_arn" in value:
        out["replicatorResourceArn"] = value["replicator_resource_arn"]
    if "replicator_state" in value:
        import aws_sdk_kafka.types.replicator_state

        out["replicatorState"] = aws_sdk_kafka.types.replicator_state.serialize_json(
            value["replicator_state"]
        )
    return out


def deserialize_json(data: dict) -> ReplicatorSummary:
    out: ReplicatorSummary = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creation_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "isReplicatorReference" in data:
        out["is_replicator_reference"] = data["isReplicatorReference"]
    if "kafkaClustersSummary" in data:
        import aws_sdk_kafka.types.__list_of_kafka_cluster_summary

        out["kafka_clusters_summary"] = (
            aws_sdk_kafka.types.__list_of_kafka_cluster_summary.deserialize_json(
                data["kafkaClustersSummary"]
            )
        )
    if "replicationInfoSummaryList" in data:
        import aws_sdk_kafka.types.__list_of_replication_info_summary

        out["replication_info_summary_list"] = (
            aws_sdk_kafka.types.__list_of_replication_info_summary.deserialize_json(
                data["replicationInfoSummaryList"]
            )
        )
    if "replicatorArn" in data:
        out["replicator_arn"] = data["replicatorArn"]
    if "replicatorName" in data:
        out["replicator_name"] = data["replicatorName"]
    if "replicatorResourceArn" in data:
        out["replicator_resource_arn"] = data["replicatorResourceArn"]
    if "replicatorState" in data:
        import aws_sdk_kafka.types.replicator_state

        out["replicator_state"] = aws_sdk_kafka.types.replicator_state.deserialize_json(
            data["replicatorState"]
        )
    return out
