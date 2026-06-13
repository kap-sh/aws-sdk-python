"""Generated from Smithy shape ``com.amazonaws.neptunedata#Action``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptunedata.errors import DeserializationError

Action: TypeAlias = Literal[
    "initiateDatabaseReset",
    "performDatabaseReset",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "initiateDatabaseReset",
        "performDatabaseReset",
    )
)


def serialize_json(value: Action) -> str:
    return value


def deserialize_json(data: str) -> Action:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Action value: {data!r}")
    return cast(Action, data)
