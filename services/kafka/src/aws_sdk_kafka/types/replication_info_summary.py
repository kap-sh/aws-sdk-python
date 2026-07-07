"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationInfoSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class ReplicationInfoSummary(TypedDict, closed=True):
    source_kafka_cluster_alias: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The alias of the source Kafka cluster.</p>"""
    target_kafka_cluster_alias: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The alias of the target Kafka cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationInfoSummary) -> dict:
    out: dict = {}
    if "source_kafka_cluster_alias" in value:
        out["sourceKafkaClusterAlias"] = value["source_kafka_cluster_alias"]
    if "target_kafka_cluster_alias" in value:
        out["targetKafkaClusterAlias"] = value["target_kafka_cluster_alias"]
    return out


def deserialize_json(data: dict) -> ReplicationInfoSummary:
    out: ReplicationInfoSummary = {}  # type: ignore[typeddict-item]
    if "sourceKafkaClusterAlias" in data:
        out["source_kafka_cluster_alias"] = data["sourceKafkaClusterAlias"]
    if "targetKafkaClusterAlias" in data:
        out["target_kafka_cluster_alias"] = data["targetKafkaClusterAlias"]
    return out
