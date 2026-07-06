"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.amazon_msk_cluster
    import aws_sdk_kafka.types.apache_kafka_cluster


class KafkaClusterSummary(TypedDict, closed=True):
    amazon_msk_cluster: NotRequired[
        "aws_sdk_kafka.types.amazon_msk_cluster.AmazonMskCluster"
    ]
    """<p>Details of an Amazon MSK Cluster.</p>"""
    apache_kafka_cluster: NotRequired[
        "aws_sdk_kafka.types.apache_kafka_cluster.ApacheKafkaCluster"
    ]
    """<p>Details of an Apache Kafka Cluster.</p>"""
    kafka_cluster_alias: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The alias of the Kafka cluster. Used to prefix names of replicated topics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterSummary) -> dict:
    out: dict = {}
    if "amazon_msk_cluster" in value:
        import aws_sdk_kafka.types.amazon_msk_cluster

        out["amazonMskCluster"] = aws_sdk_kafka.types.amazon_msk_cluster.serialize_json(
            value["amazon_msk_cluster"]
        )
    if "apache_kafka_cluster" in value:
        import aws_sdk_kafka.types.apache_kafka_cluster

        out["apacheKafkaCluster"] = (
            aws_sdk_kafka.types.apache_kafka_cluster.serialize_json(
                value["apache_kafka_cluster"]
            )
        )
    if "kafka_cluster_alias" in value:
        out["kafkaClusterAlias"] = value["kafka_cluster_alias"]
    return out


def deserialize_json(data: dict) -> KafkaClusterSummary:
    out: KafkaClusterSummary = {}  # type: ignore[typeddict-item]
    if "amazonMskCluster" in data:
        import aws_sdk_kafka.types.amazon_msk_cluster

        out["amazon_msk_cluster"] = (
            aws_sdk_kafka.types.amazon_msk_cluster.deserialize_json(
                data["amazonMskCluster"]
            )
        )
    if "apacheKafkaCluster" in data:
        import aws_sdk_kafka.types.apache_kafka_cluster

        out["apache_kafka_cluster"] = (
            aws_sdk_kafka.types.apache_kafka_cluster.deserialize_json(
                data["apacheKafkaCluster"]
            )
        )
    if "kafkaClusterAlias" in data:
        out["kafka_cluster_alias"] = data["kafkaClusterAlias"]
    return out
