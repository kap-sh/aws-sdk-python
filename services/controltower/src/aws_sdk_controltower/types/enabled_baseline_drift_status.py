"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineDriftStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

EnabledBaselineDriftStatus: TypeAlias = Literal[
    "IN_SYNC",
    "DRIFTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_SYNC",
        "DRIFTED",
    )
)


def serialize_json(value: EnabledBaselineDriftStatus) -> str:
    return value


def deserialize_json(data: str) -> EnabledBaselineDriftStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EnabledBaselineDriftStatus value: {data!r}"
        )
    return cast(EnabledBaselineDriftStatus, data)
