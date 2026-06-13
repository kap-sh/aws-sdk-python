"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

DatabaseType: TypeAlias = Literal[
    "SYSTEM",
    "TENANT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYSTEM",
        "TENANT",
    )
)


def serialize_json(value: DatabaseType) -> str:
    return value


def deserialize_json(data: str) -> DatabaseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseType value: {data!r}")
    return cast(DatabaseType, data)
