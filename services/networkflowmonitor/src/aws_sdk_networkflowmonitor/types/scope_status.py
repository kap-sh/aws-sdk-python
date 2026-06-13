"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ScopeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkflowmonitor.errors import DeserializationError

ScopeStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "IN_PROGRESS",
    "FAILED",
    "DEACTIVATING",
    "DEACTIVATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "IN_PROGRESS",
        "FAILED",
        "DEACTIVATING",
        "DEACTIVATED",
    )
)


def serialize_json(value: ScopeStatus) -> str:
    return value


def deserialize_json(data: str) -> ScopeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScopeStatus value: {data!r}")
    return cast(ScopeStatus, data)
