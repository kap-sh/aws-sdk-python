"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#KafkaClusterDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.apache_kafka_cluster_description


class KafkaClusterDescription(TypedDict, closed=True):
    apache_kafka_cluster: NotRequired[
        "capo_kafkaconnect.types.apache_kafka_cluster_description.ApacheKafkaClusterDescription"
    ]
    """<p>The Apache Kafka cluster to which the connector is connected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterDescription) -> dict:
    out: dict = {}
    if "apache_kafka_cluster" in value:
        import capo_kafkaconnect.types.apache_kafka_cluster_description

        out["apacheKafkaCluster"] = (
            capo_kafkaconnect.types.apache_kafka_cluster_description.serialize_json(
                value["apache_kafka_cluster"]
            )
        )
    return out


def deserialize_json(data: dict) -> KafkaClusterDescription:
    out: KafkaClusterDescription = {}  # type: ignore[typeddict-item]
    if "apacheKafkaCluster" in data:
        import capo_kafkaconnect.types.apache_kafka_cluster_description

        out["apache_kafka_cluster"] = (
            capo_kafkaconnect.types.apache_kafka_cluster_description.deserialize_json(
                data["apacheKafkaCluster"]
            )
        )
    return out
