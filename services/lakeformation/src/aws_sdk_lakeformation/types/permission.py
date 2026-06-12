"""Generated from Smithy shape ``com.amazonaws.lakeformation#Permission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

Permission: TypeAlias = Literal[
    "ALL",
    "SELECT",
    "ALTER",
    "DROP",
    "DELETE",
    "INSERT",
    "DESCRIBE",
    "CREATE_DATABASE",
    "CREATE_TABLE",
    "DATA_LOCATION_ACCESS",
    "CREATE_LF_TAG",
    "ASSOCIATE",
    "GRANT_WITH_LF_TAG_EXPRESSION",
    "CREATE_LF_TAG_EXPRESSION",
    "CREATE_CATALOG",
    "SUPER_USER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "SELECT",
        "ALTER",
        "DROP",
        "DELETE",
        "INSERT",
        "DESCRIBE",
        "CREATE_DATABASE",
        "CREATE_TABLE",
        "DATA_LOCATION_ACCESS",
        "CREATE_LF_TAG",
        "ASSOCIATE",
        "GRANT_WITH_LF_TAG_EXPRESSION",
        "CREATE_LF_TAG_EXPRESSION",
        "CREATE_CATALOG",
        "SUPER_USER",
    )
)


def serialize_json(value: Permission) -> str:
    return value


def deserialize_json(data: str) -> Permission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Permission value: {data!r}")
    return cast(Permission, data)
