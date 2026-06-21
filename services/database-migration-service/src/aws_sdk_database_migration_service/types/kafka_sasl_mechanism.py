"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KafkaSaslMechanism``."""

from typing import Literal, TypeAlias, cast

KafkaSaslMechanism: TypeAlias = Literal[
    "scram-sha-512",
    "plain",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KafkaSaslMechanism) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KafkaSaslMechanism:
    return cast(KafkaSaslMechanism, data)
