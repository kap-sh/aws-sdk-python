"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RefreshSchemasStatusTypeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

RefreshSchemasStatusTypeValue: TypeAlias = Literal[
    "successful",
    "failed",
    "refreshing",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "successful",
        "failed",
        "refreshing",
    )
)


def serialize_aws_json_1_1(value: RefreshSchemasStatusTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RefreshSchemasStatusTypeValue:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RefreshSchemasStatusTypeValue value: {data!r}"
        )
    return cast(RefreshSchemasStatusTypeValue, data)
