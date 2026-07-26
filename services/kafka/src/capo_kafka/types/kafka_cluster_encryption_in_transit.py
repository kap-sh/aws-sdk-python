"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterEncryptionInTransit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.kafka_cluster_encryption_in_transit_type


class KafkaClusterEncryptionInTransit(TypedDict, closed=True):
    encryption_type: NotRequired[
        "capo_kafka.types.kafka_cluster_encryption_in_transit_type.KafkaClusterEncryptionInTransitType"
    ]
    """<p>The type of encryption in transit to the Apache Kafka cluster.</p>"""
    root_ca_certificate: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The root CA certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterEncryptionInTransit) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        import capo_kafka.types.kafka_cluster_encryption_in_transit_type

        out["encryptionType"] = (
            capo_kafka.types.kafka_cluster_encryption_in_transit_type.serialize_json(
                value["encryption_type"]
            )
        )
    if "root_ca_certificate" in value:
        out["rootCaCertificate"] = value["root_ca_certificate"]
    return out


def deserialize_json(data: dict) -> KafkaClusterEncryptionInTransit:
    out: KafkaClusterEncryptionInTransit = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import capo_kafka.types.kafka_cluster_encryption_in_transit_type

        out["encryption_type"] = (
            capo_kafka.types.kafka_cluster_encryption_in_transit_type.deserialize_json(
                data["encryptionType"]
            )
        )
    if "rootCaCertificate" in data:
        out["root_ca_certificate"] = data["rootCaCertificate"]
    return out
