"""Generated from Smithy shape ``com.amazonaws.eks#SupportType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

SupportType: TypeAlias = Literal[
    "STANDARD",
    "EXTENDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "EXTENDED",
    )
)


def serialize_json(value: SupportType) -> str:
    return value


def deserialize_json(data: str) -> SupportType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SupportType value: {data!r}")
    return cast(SupportType, data)
