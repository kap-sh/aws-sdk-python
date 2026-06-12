"""Generated from Smithy shape ``com.amazonaws.glue#Permission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

Permission: TypeAlias = Literal[
    "ALL",
    "SELECT",
    "ALTER",
    "DROP",
    "DELETE",
    "INSERT",
    "CREATE_DATABASE",
    "CREATE_TABLE",
    "DATA_LOCATION_ACCESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "SELECT",
        "ALTER",
        "DROP",
        "DELETE",
        "INSERT",
        "CREATE_DATABASE",
        "CREATE_TABLE",
        "DATA_LOCATION_ACCESS",
    )
)


def serialize_aws_json_1_1(value: Permission) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Permission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Permission value: {data!r}")
    return cast(Permission, data)
