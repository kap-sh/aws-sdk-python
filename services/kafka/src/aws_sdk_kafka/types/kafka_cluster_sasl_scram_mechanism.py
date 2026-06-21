"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterSaslScramMechanism``."""

from typing import Literal, TypeAlias, cast

"""<p>The SASL/SCRAM authentication mechanism.</p>"""
KafkaClusterSaslScramMechanism: TypeAlias = Literal[
    "SHA256",
    "SHA512",
]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterSaslScramMechanism) -> str:
    return value


def deserialize_json(data: str) -> KafkaClusterSaslScramMechanism:
    return cast(KafkaClusterSaslScramMechanism, data)
