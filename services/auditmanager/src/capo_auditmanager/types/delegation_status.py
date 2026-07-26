"""Generated from Smithy shape ``com.amazonaws.auditmanager#DelegationStatus``."""

from typing import Literal, TypeAlias, cast

DelegationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "UNDER_REVIEW",
    "COMPLETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DelegationStatus) -> str:
    return value


def deserialize_json(data: str) -> DelegationStatus:
    return cast(DelegationStatus, data)
