"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EndpointSettingTypeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

EndpointSettingTypeValue: TypeAlias = Literal[
    "string",
    "boolean",
    "integer",
    "enum",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "string",
        "boolean",
        "integer",
        "enum",
    )
)


def serialize_aws_json_1_1(value: EndpointSettingTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointSettingTypeValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointSettingTypeValue value: {data!r}")
    return cast(EndpointSettingTypeValue, data)
