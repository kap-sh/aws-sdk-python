"""Generated from Smithy shape ``com.amazonaws.chime#CallingNameStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

CallingNameStatus: TypeAlias = Literal[
    "Unassigned",
    "UpdateInProgress",
    "UpdateSucceeded",
    "UpdateFailed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Unassigned",
        "UpdateInProgress",
        "UpdateSucceeded",
        "UpdateFailed",
    )
)


def serialize_json(value: CallingNameStatus) -> str:
    return value


def deserialize_json(data: str) -> CallingNameStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CallingNameStatus value: {data!r}")
    return cast(CallingNameStatus, data)
