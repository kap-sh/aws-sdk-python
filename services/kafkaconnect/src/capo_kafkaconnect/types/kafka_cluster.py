"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#KafkaCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kafkaconnect.types.apache_kafka_cluster


class KafkaCluster(TypedDict, closed=True):
    apache_kafka_cluster: (
        "capo_kafkaconnect.types.apache_kafka_cluster.ApacheKafkaCluster"
    )
    """<p>The Apache Kafka cluster to which the connector is connected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaCluster) -> dict:
    out: dict = {}
    import capo_kafkaconnect.types.apache_kafka_cluster

    out["apacheKafkaCluster"] = (
        capo_kafkaconnect.types.apache_kafka_cluster.serialize_json(
            value["apache_kafka_cluster"]
        )
    )
    return out


def deserialize_json(data: dict) -> KafkaCluster:
    out: KafkaCluster = {}  # type: ignore[typeddict-item]
    if "apacheKafkaCluster" in data:
        import capo_kafkaconnect.types.apache_kafka_cluster

        out["apache_kafka_cluster"] = (
            capo_kafkaconnect.types.apache_kafka_cluster.deserialize_json(
                data["apacheKafkaCluster"]
            )
        )
    else:
        raise DeserializationError("KafkaCluster.apache_kafka_cluster required")
    return out
