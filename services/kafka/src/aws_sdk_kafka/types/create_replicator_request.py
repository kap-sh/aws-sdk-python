"""Generated from Smithy shape ``com.amazonaws.kafka#CreateReplicatorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_kafka_cluster
    import aws_sdk_kafka.types.__list_of_replication_info
    import aws_sdk_kafka.types.__map_of__string
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.__string_max1024
    import aws_sdk_kafka.types.__string_min1_max128_pattern09_a_za_z09_a_za_z0
    import aws_sdk_kafka.types.log_delivery


class CreateReplicatorRequest(TypedDict):
    description: NotRequired["aws_sdk_kafka.types.__string_max1024.__stringMax1024"]
    """<p>A summary description of the replicator.</p>"""
    kafka_clusters: NotRequired[
        "aws_sdk_kafka.types.__list_of_kafka_cluster.__listOfKafkaCluster"
    ]
    """<p>Kafka Clusters to use in setting up sources / targets for replication.</p>"""
    replication_info_list: NotRequired[
        "aws_sdk_kafka.types.__list_of_replication_info.__listOfReplicationInfo"
    ]
    """<p>A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow.</p>"""
    replicator_name: NotRequired[
        "aws_sdk_kafka.types.__string_min1_max128_pattern09_a_za_z09_a_za_z0.__stringMin1Max128Pattern09AZaZ09AZaZ0"
    ]
    """<p>The name of the replicator. Alpha-numeric characters with '-' are allowed.</p>"""
    service_execution_role_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The ARN of the IAM role used by the replicator to access resources in the customer's account (e.g source and target clusters)</p>"""
    tags: NotRequired["aws_sdk_kafka.types.__map_of__string.__mapOf__string"]
    """<p>List of tags to attach to created Replicator.</p>"""
    log_delivery: NotRequired["aws_sdk_kafka.types.log_delivery.LogDelivery"]
    """<p>Configuration for delivering replicator logs to customer destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReplicatorRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "kafka_clusters" in value:
        import aws_sdk_kafka.types.__list_of_kafka_cluster

        out["kafkaClusters"] = (
            aws_sdk_kafka.types.__list_of_kafka_cluster.serialize_json(
                value["kafka_clusters"]
            )
        )
    if "replication_info_list" in value:
        import aws_sdk_kafka.types.__list_of_replication_info

        out["replicationInfoList"] = (
            aws_sdk_kafka.types.__list_of_replication_info.serialize_json(
                value["replication_info_list"]
            )
        )
    if "replicator_name" in value:
        out["replicatorName"] = value["replicator_name"]
    if "service_execution_role_arn" in value:
        out["serviceExecutionRoleArn"] = value["service_execution_role_arn"]
    if "tags" in value:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.serialize_json(value["tags"])
    if "log_delivery" in value:
        import aws_sdk_kafka.types.log_delivery

        out["logDelivery"] = aws_sdk_kafka.types.log_delivery.serialize_json(
            value["log_delivery"]
        )
    return out


def deserialize_json(data: dict) -> CreateReplicatorRequest:
    out: CreateReplicatorRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "kafkaClusters" in data:
        import aws_sdk_kafka.types.__list_of_kafka_cluster

        out["kafka_clusters"] = (
            aws_sdk_kafka.types.__list_of_kafka_cluster.deserialize_json(
                data["kafkaClusters"]
            )
        )
    if "replicationInfoList" in data:
        import aws_sdk_kafka.types.__list_of_replication_info

        out["replication_info_list"] = (
            aws_sdk_kafka.types.__list_of_replication_info.deserialize_json(
                data["replicationInfoList"]
            )
        )
    if "replicatorName" in data:
        out["replicator_name"] = data["replicatorName"]
    if "serviceExecutionRoleArn" in data:
        out["service_execution_role_arn"] = data["serviceExecutionRoleArn"]
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
