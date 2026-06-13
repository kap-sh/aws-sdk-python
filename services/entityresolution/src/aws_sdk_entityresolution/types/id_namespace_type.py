"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

IdNamespaceType: TypeAlias = Literal[
    "SOURCE",
    "TARGET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOURCE",
        "TARGET",
    )
)


def serialize_json(value: IdNamespaceType) -> str:
    return value


def deserialize_json(data: str) -> IdNamespaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdNamespaceType value: {data!r}")
    return cast(IdNamespaceType, data)
