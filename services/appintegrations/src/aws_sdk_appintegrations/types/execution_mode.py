"""Generated from Smithy shape ``com.amazonaws.appintegrations#ExecutionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appintegrations.errors import DeserializationError

ExecutionMode: TypeAlias = Literal[
    "ON_DEMAND",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND",
        "SCHEDULED",
    )
)


def serialize_json(value: ExecutionMode) -> str:
    return value


def deserialize_json(data: str) -> ExecutionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionMode value: {data!r}")
    return cast(ExecutionMode, data)
