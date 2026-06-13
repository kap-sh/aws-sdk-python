"""Generated from Smithy shape ``com.amazonaws.quicksight#CommitMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

CommitMode: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "MANUAL",
    )
)


def serialize_json(value: CommitMode) -> str:
    return value


def deserialize_json(data: str) -> CommitMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommitMode value: {data!r}")
    return cast(CommitMode, data)
