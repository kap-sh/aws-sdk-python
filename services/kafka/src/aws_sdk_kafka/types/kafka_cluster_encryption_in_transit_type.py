"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterEncryptionInTransitType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of encryption in transit to the Apache Kafka cluster.</p>"""
KafkaClusterEncryptionInTransitType: TypeAlias = Literal["TLS",]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterEncryptionInTransitType) -> str:
    return value


def deserialize_json(data: str) -> KafkaClusterEncryptionInTransitType:
    return cast(KafkaClusterEncryptionInTransitType, data)
