"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ProposalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

ProposalStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "APPROVED",
    "REJECTED",
    "EXPIRED",
    "ACTION_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "APPROVED",
        "REJECTED",
        "EXPIRED",
        "ACTION_FAILED",
    )
)


def serialize_json(value: ProposalStatus) -> str:
    return value


def deserialize_json(data: str) -> ProposalStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProposalStatus value: {data!r}")
    return cast(ProposalStatus, data)
