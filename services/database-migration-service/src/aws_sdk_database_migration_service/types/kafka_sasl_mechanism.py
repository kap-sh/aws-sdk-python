"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KafkaSaslMechanism``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

KafkaSaslMechanism: TypeAlias = Literal[
    "scram-sha-512",
    "plain",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "scram-sha-512",
        "plain",
    )
)


def serialize_aws_json_1_1(value: KafkaSaslMechanism) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KafkaSaslMechanism:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KafkaSaslMechanism value: {data!r}")
    return cast(KafkaSaslMechanism, data)
