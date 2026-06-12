"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#KafkaClusterDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.apache_kafka_cluster_description


class KafkaClusterDescription(TypedDict):
    apache_kafka_cluster: NotRequired[
        "aws_sdk_kafkaconnect.types.apache_kafka_cluster_description.ApacheKafkaClusterDescription"
    ]
    """<p>The Apache Kafka cluster to which the connector is connected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterDescription) -> dict:
    out: dict = {}
    if "apache_kafka_cluster" in value:
        import aws_sdk_kafkaconnect.types.apache_kafka_cluster_description

        out["apacheKafkaCluster"] = (
            aws_sdk_kafkaconnect.types.apache_kafka_cluster_description.serialize_json(
                value["apache_kafka_cluster"]
            )
        )
    return out


def deserialize_json(data: dict) -> KafkaClusterDescription:
    out: KafkaClusterDescription = {}  # type: ignore[typeddict-item]
    if "apacheKafkaCluster" in data:
        import aws_sdk_kafkaconnect.types.apache_kafka_cluster_description

        out["apache_kafka_cluster"] = (
            aws_sdk_kafkaconnect.types.apache_kafka_cluster_description.deserialize_json(
                data["apacheKafkaCluster"]
            )
        )
    return out
