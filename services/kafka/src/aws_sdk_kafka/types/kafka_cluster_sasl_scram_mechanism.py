"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterSaslScramMechanism``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The SASL/SCRAM authentication mechanism.</p>"""
KafkaClusterSaslScramMechanism: TypeAlias = Literal[
    "SHA256",
    "SHA512",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHA256",
        "SHA512",
    )
)


def serialize_json(value: KafkaClusterSaslScramMechanism) -> str:
    return value


def deserialize_json(data: str) -> KafkaClusterSaslScramMechanism:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KafkaClusterSaslScramMechanism value: {data!r}"
        )
    return cast(KafkaClusterSaslScramMechanism, data)
