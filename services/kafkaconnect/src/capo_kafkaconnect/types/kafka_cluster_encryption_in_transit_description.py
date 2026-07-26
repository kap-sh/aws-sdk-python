"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#KafkaClusterEncryptionInTransitDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.kafka_cluster_encryption_in_transit_type


class KafkaClusterEncryptionInTransitDescription(TypedDict, closed=True):
    encryption_type: NotRequired[
        "capo_kafkaconnect.types.kafka_cluster_encryption_in_transit_type.KafkaClusterEncryptionInTransitType"
    ]
    """<p>The type of encryption in transit to the Apache Kafka cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterEncryptionInTransitDescription) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        out["encryptionType"] = value["encryption_type"]
    return out


def deserialize_json(data: dict) -> KafkaClusterEncryptionInTransitDescription:
    out: KafkaClusterEncryptionInTransitDescription = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        out["encryption_type"] = data["encryptionType"]
    return out
