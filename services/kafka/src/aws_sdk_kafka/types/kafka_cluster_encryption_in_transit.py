"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterEncryptionInTransit``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.kafka_cluster_encryption_in_transit_type


class KafkaClusterEncryptionInTransit(TypedDict):
    encryption_type: NotRequired[
        "aws_sdk_kafka.types.kafka_cluster_encryption_in_transit_type.KafkaClusterEncryptionInTransitType"
    ]
    """<p>The type of encryption in transit to the Apache Kafka cluster.</p>"""
    root_ca_certificate: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The root CA certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterEncryptionInTransit) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        import aws_sdk_kafka.types.kafka_cluster_encryption_in_transit_type

        out["encryptionType"] = (
            aws_sdk_kafka.types.kafka_cluster_encryption_in_transit_type.serialize_json(
                value["encryption_type"]
            )
        )
    if "root_ca_certificate" in value:
        out["rootCaCertificate"] = value["root_ca_certificate"]
    return out


def deserialize_json(data: dict) -> KafkaClusterEncryptionInTransit:
    out: KafkaClusterEncryptionInTransit = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import aws_sdk_kafka.types.kafka_cluster_encryption_in_transit_type

        out["encryption_type"] = (
            aws_sdk_kafka.types.kafka_cluster_encryption_in_transit_type.deserialize_json(
                data["encryptionType"]
            )
        )
    if "rootCaCertificate" in data:
        out["root_ca_certificate"] = data["rootCaCertificate"]
    return out
