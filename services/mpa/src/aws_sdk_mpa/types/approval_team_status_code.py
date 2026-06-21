"""Generated from Smithy shape ``com.amazonaws.mpa#ApprovalTeamStatusCode``."""

from typing import Literal, TypeAlias, cast

ApprovalTeamStatusCode: TypeAlias = Literal[
    "VALIDATING",
    "PENDING_ACTIVATION",
    "FAILED_VALIDATION",
    "FAILED_ACTIVATION",
    "UPDATE_PENDING_APPROVAL",
    "UPDATE_PENDING_ACTIVATION",
    "UPDATE_FAILED_APPROVAL",
    "UPDATE_FAILED_ACTIVATION",
    "UPDATE_FAILED_VALIDATION",
    "DELETE_PENDING_APPROVAL",
    "DELETE_FAILED_APPROVAL",
    "DELETE_FAILED_VALIDATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalTeamStatusCode) -> str:
    return value


def deserialize_json(data: str) -> ApprovalTeamStatusCode:
    return cast(ApprovalTeamStatusCode, data)
