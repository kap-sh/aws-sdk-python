"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SslSecurityProtocolValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

SslSecurityProtocolValue: TypeAlias = Literal[
    "plaintext",
    "ssl-encryption",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "plaintext",
        "ssl-encryption",
    )
)


def serialize_aws_json_1_1(value: SslSecurityProtocolValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SslSecurityProtocolValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SslSecurityProtocolValue value: {data!r}")
    return cast(SslSecurityProtocolValue, data)
