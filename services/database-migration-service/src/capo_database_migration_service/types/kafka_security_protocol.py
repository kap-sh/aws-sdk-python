"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KafkaSecurityProtocol``."""

from typing import Literal, TypeAlias, cast

KafkaSecurityProtocol: TypeAlias = Literal[
    "plaintext",
    "ssl-authentication",
    "ssl-encryption",
    "sasl-ssl",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KafkaSecurityProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KafkaSecurityProtocol:
    return cast(KafkaSecurityProtocol, data)
