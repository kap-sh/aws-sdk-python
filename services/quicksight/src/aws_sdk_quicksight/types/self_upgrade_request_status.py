"""Generated from Smithy shape ``com.amazonaws.quicksight#SelfUpgradeRequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SelfUpgradeRequestStatus: TypeAlias = Literal[
    "PENDING",
    "APPROVED",
    "DENIED",
    "UPDATE_FAILED",
    "VERIFY_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "APPROVED",
        "DENIED",
        "UPDATE_FAILED",
        "VERIFY_FAILED",
    )
)


def serialize_json(value: SelfUpgradeRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> SelfUpgradeRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelfUpgradeRequestStatus value: {data!r}")
    return cast(SelfUpgradeRequestStatus, data)
