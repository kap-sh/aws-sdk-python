"""Generated from Smithy shape ``com.amazonaws.fis#SafetyLeverStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fis.errors import DeserializationError

SafetyLeverStatus: TypeAlias = Literal[
    "disengaged",
    "engaged",
    "engaging",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disengaged",
        "engaged",
        "engaging",
    )
)


def serialize_json(value: SafetyLeverStatus) -> str:
    return value


def deserialize_json(data: str) -> SafetyLeverStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SafetyLeverStatus value: {data!r}")
    return cast(SafetyLeverStatus, data)
