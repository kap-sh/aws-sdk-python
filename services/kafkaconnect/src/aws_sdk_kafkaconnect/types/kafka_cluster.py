"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#KafkaCluster``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.apache_kafka_cluster


class KafkaCluster(TypedDict):
    apache_kafka_cluster: (
        "aws_sdk_kafkaconnect.types.apache_kafka_cluster.ApacheKafkaCluster"
    )
    """<p>The Apache Kafka cluster to which the connector is connected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaCluster) -> dict:
    out: dict = {}
    import aws_sdk_kafkaconnect.types.apache_kafka_cluster

    out["apacheKafkaCluster"] = (
        aws_sdk_kafkaconnect.types.apache_kafka_cluster.serialize_json(
            value["apache_kafka_cluster"]
        )
    )
    return out


def deserialize_json(data: dict) -> KafkaCluster:
    out: KafkaCluster = {}  # type: ignore[typeddict-item]
    if "apacheKafkaCluster" in data:
        import aws_sdk_kafkaconnect.types.apache_kafka_cluster

        out["apache_kafka_cluster"] = (
            aws_sdk_kafkaconnect.types.apache_kafka_cluster.deserialize_json(
                data["apacheKafkaCluster"]
            )
        )
    else:
        raise DeserializationError("KafkaCluster.apache_kafka_cluster required")
    return out
