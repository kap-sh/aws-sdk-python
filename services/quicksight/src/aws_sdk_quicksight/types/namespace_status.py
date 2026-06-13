"""Generated from Smithy shape ``com.amazonaws.quicksight#NamespaceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NamespaceStatus: TypeAlias = Literal[
    "CREATED",
    "CREATING",
    "DELETING",
    "RETRYABLE_FAILURE",
    "NON_RETRYABLE_FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "CREATING",
        "DELETING",
        "RETRYABLE_FAILURE",
        "NON_RETRYABLE_FAILURE",
    )
)


def serialize_json(value: NamespaceStatus) -> str:
    return value


def deserialize_json(data: str) -> NamespaceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NamespaceStatus value: {data!r}")
    return cast(NamespaceStatus, data)
