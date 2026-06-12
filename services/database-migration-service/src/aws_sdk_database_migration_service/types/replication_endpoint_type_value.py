"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationEndpointTypeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

ReplicationEndpointTypeValue: TypeAlias = Literal[
    "source",
    "target",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "source",
        "target",
    )
)


def serialize_aws_json_1_1(value: ReplicationEndpointTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicationEndpointTypeValue:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReplicationEndpointTypeValue value: {data!r}"
        )
    return cast(ReplicationEndpointTypeValue, data)
