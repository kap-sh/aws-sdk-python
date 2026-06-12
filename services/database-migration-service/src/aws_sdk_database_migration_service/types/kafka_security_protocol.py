"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KafkaSecurityProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

KafkaSecurityProtocol: TypeAlias = Literal[
    "plaintext",
    "ssl-authentication",
    "ssl-encryption",
    "sasl-ssl",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "plaintext",
        "ssl-authentication",
        "ssl-encryption",
        "sasl-ssl",
    )
)


def serialize_aws_json_1_1(value: KafkaSecurityProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KafkaSecurityProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KafkaSecurityProtocol value: {data!r}")
    return cast(KafkaSecurityProtocol, data)
