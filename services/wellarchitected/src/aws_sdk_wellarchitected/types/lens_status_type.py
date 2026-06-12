"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

LensStatusType: TypeAlias = Literal[
    "ALL",
    "DRAFT",
    "PUBLISHED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "DRAFT",
        "PUBLISHED",
    )
)


def serialize_json(value: LensStatusType) -> str:
    return value


def deserialize_json(data: str) -> LensStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LensStatusType value: {data!r}")
    return cast(LensStatusType, data)
