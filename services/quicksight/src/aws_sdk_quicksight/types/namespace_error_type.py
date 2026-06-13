"""Generated from Smithy shape ``com.amazonaws.quicksight#NamespaceErrorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NamespaceErrorType: TypeAlias = Literal[
    "PERMISSION_DENIED",
    "INTERNAL_SERVICE_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERMISSION_DENIED",
        "INTERNAL_SERVICE_ERROR",
    )
)


def serialize_json(value: NamespaceErrorType) -> str:
    return value


def deserialize_json(data: str) -> NamespaceErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NamespaceErrorType value: {data!r}")
    return cast(NamespaceErrorType, data)
