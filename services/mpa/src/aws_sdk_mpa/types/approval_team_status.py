"""Generated from Smithy shape ``com.amazonaws.mpa#ApprovalTeamStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

ApprovalTeamStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DELETING",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "DELETING",
        "PENDING",
    )
)


def serialize_json(value: ApprovalTeamStatus) -> str:
    return value


def deserialize_json(data: str) -> ApprovalTeamStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApprovalTeamStatus value: {data!r}")
    return cast(ApprovalTeamStatus, data)
