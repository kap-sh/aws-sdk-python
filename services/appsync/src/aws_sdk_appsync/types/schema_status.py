"""Generated from Smithy shape ``com.amazonaws.appsync#SchemaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

SchemaStatus: TypeAlias = Literal[
    "PROCESSING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "SUCCESS",
    "NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROCESSING",
        "ACTIVE",
        "DELETING",
        "FAILED",
        "SUCCESS",
        "NOT_APPLICABLE",
    )
)


def serialize_json(value: SchemaStatus) -> str:
    return value


def deserialize_json(data: str) -> SchemaStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaStatus value: {data!r}")
    return cast(SchemaStatus, data)
