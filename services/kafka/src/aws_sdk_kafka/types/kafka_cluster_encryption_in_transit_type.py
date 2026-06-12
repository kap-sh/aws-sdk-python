"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterEncryptionInTransitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The type of encryption in transit to the Apache Kafka cluster.</p>"""
KafkaClusterEncryptionInTransitType: TypeAlias = Literal["TLS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TLS",))


def serialize_json(value: KafkaClusterEncryptionInTransitType) -> str:
    return value


def deserialize_json(data: str) -> KafkaClusterEncryptionInTransitType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KafkaClusterEncryptionInTransitType value: {data!r}"
        )
    return cast(KafkaClusterEncryptionInTransitType, data)
