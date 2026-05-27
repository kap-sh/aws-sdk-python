"""Generated from Smithy shape ``com.amazonaws.eks#Category``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

Category: TypeAlias = Literal[
    "UPGRADE_READINESS",
    "MISCONFIGURATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPGRADE_READINESS",
        "MISCONFIGURATION",
    )
)


def serialize_json(value: Category) -> str:
    return value


def deserialize_json(data: str) -> Category:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Category value: {data!r}")
    return cast(Category, data)
