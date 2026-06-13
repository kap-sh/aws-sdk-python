"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ApprovalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ApprovalStatus: TypeAlias = Literal[
    "APPROVED",
    "DENIED",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVED",
        "DENIED",
        "PENDING",
    )
)


def serialize_json(value: ApprovalStatus) -> str:
    return value


def deserialize_json(data: str) -> ApprovalStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApprovalStatus value: {data!r}")
    return cast(ApprovalStatus, data)
