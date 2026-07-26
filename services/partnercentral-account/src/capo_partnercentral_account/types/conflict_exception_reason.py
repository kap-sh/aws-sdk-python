"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

ConflictExceptionReason: TypeAlias = Literal[
    "CONFLICT_CLIENT_TOKEN",
    "DUPLICATE_PARTNER",
    "INCOMPATIBLE_PROFILE_STATE",
    "INCOMPATIBLE_PARTNER_PROFILE_TASK_STATE",
    "DUPLICATE_CONNECTION_INVITATION",
    "INCOMPATIBLE_CONNECTION_INVITATION_STATE",
    "INCOMPATIBLE_CONNECTION_INVITATION_RECEIVER",
    "DUPLICATE_CONNECTION",
    "INCOMPATIBLE_CONNECTION_STATE",
    "INCOMPATIBLE_CONNECTION_PREFERENCES_REVISION",
    "ACCOUNT_ALREADY_VERIFIED",
    "VERIFICATION_ALREADY_IN_PROGRESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConflictExceptionReason:
    return cast(ConflictExceptionReason, data)
