"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

LensStatus: TypeAlias = Literal[
    "CURRENT",
    "NOT_CURRENT",
    "DEPRECATED",
    "DELETED",
    "UNSHARED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CURRENT",
        "NOT_CURRENT",
        "DEPRECATED",
        "DELETED",
        "UNSHARED",
    )
)


def serialize_json(value: LensStatus) -> str:
    return value


def deserialize_json(data: str) -> LensStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LensStatus value: {data!r}")
    return cast(LensStatus, data)
