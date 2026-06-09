"""Generated from Smithy shape ``com.amazonaws.eks#TaintEffect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

TaintEffect: TypeAlias = Literal[
    "NO_SCHEDULE",
    "NO_EXECUTE",
    "PREFER_NO_SCHEDULE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_SCHEDULE",
        "NO_EXECUTE",
        "PREFER_NO_SCHEDULE",
    )
)


def serialize_json(value: TaintEffect) -> str:
    return value


def deserialize_json(data: str) -> TaintEffect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaintEffect value: {data!r}")
    return cast(TaintEffect, data)
