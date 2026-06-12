"""Generated from Smithy shape ``com.amazonaws.guardduty#TrustedEntitySetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

TrustedEntitySetStatus: TypeAlias = Literal[
    "INACTIVE",
    "ACTIVATING",
    "ACTIVE",
    "DEACTIVATING",
    "ERROR",
    "DELETE_PENDING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INACTIVE",
        "ACTIVATING",
        "ACTIVE",
        "DEACTIVATING",
        "ERROR",
        "DELETE_PENDING",
        "DELETED",
    )
)


def serialize_json(value: TrustedEntitySetStatus) -> str:
    return value


def deserialize_json(data: str) -> TrustedEntitySetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrustedEntitySetStatus value: {data!r}")
    return cast(TrustedEntitySetStatus, data)
