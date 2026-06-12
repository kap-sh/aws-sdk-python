"""Generated from Smithy shape ``com.amazonaws.batch#CEState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

CEState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: CEState) -> str:
    return value


def deserialize_json(data: str) -> CEState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CEState value: {data!r}")
    return cast(CEState, data)
