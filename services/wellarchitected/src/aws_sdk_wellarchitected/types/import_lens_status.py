"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ImportLensStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

ImportLensStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETE",
        "ERROR",
    )
)


def serialize_json(value: ImportLensStatus) -> str:
    return value


def deserialize_json(data: str) -> ImportLensStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportLensStatus value: {data!r}")
    return cast(ImportLensStatus, data)
