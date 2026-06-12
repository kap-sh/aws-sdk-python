"""Generated from Smithy shape ``com.amazonaws.appflow#PathPrefix``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

PathPrefix: TypeAlias = Literal[
    "EXECUTION_ID",
    "SCHEMA_VERSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXECUTION_ID",
        "SCHEMA_VERSION",
    )
)


def serialize_json(value: PathPrefix) -> str:
    return value


def deserialize_json(data: str) -> PathPrefix:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PathPrefix value: {data!r}")
    return cast(PathPrefix, data)
