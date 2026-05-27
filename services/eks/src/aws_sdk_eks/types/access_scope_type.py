"""Generated from Smithy shape ``com.amazonaws.eks#AccessScopeType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

AccessScopeType: TypeAlias = Literal[
    "cluster",
    "namespace",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "cluster",
        "namespace",
    )
)


def serialize_json(value: AccessScopeType) -> str:
    return value


def deserialize_json(data: str) -> AccessScopeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessScopeType value: {data!r}")
    return cast(AccessScopeType, data)
