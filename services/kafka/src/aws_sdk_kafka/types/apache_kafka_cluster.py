"""Generated from Smithy shape ``com.amazonaws.kafka#ApacheKafkaCluster``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class ApacheKafkaCluster(TypedDict):
    apache_kafka_cluster_id: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The ID of the Apache Kafka cluster.</p>"""
    bootstrap_broker_string: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The bootstrap broker string of the Apache Kafka cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApacheKafkaCluster) -> dict:
    out: dict = {}
    if "apache_kafka_cluster_id" in value:
        out["apacheKafkaClusterId"] = value["apache_kafka_cluster_id"]
    if "bootstrap_broker_string" in value:
        out["bootstrapBrokerString"] = value["bootstrap_broker_string"]
    return out


def deserialize_json(data: dict) -> ApacheKafkaCluster:
    out: ApacheKafkaCluster = {}  # type: ignore[typeddict-item]
    if "apacheKafkaClusterId" in data:
        out["apache_kafka_cluster_id"] = data["apacheKafkaClusterId"]
    if "bootstrapBrokerString" in data:
        out["bootstrap_broker_string"] = data["bootstrapBrokerString"]
    return out
