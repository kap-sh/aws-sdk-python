"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ResourceNotFoundExceptionReason``."""

from typing import Literal, TypeAlias, cast

ResourceNotFoundExceptionReason: TypeAlias = Literal[
    "PARTNER_NOT_FOUND",
    "PARTNER_PROFILE_NOT_FOUND",
    "PARTNER_PROFILE_TASK_NOT_FOUND",
    "PARTNER_DOMAIN_NOT_FOUND",
    "SENDER_PROFILE_NOT_FOUND",
    "RECEIVER_PROFILE_NOT_FOUND",
    "CONNECTION_INVITATION_NOT_FOUND",
    "CONNECTION_NOT_FOUND",
    "VERIFICATION_NOT_FOUND",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceNotFoundExceptionReason:
    return cast(ResourceNotFoundExceptionReason, data)
