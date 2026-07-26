"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#InvitationStatus``."""

from typing import Literal, TypeAlias, cast

InvitationStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "REJECTED",
    "CANCELED",
    "EXPIRED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvitationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InvitationStatus:
    return cast(InvitationStatus, data)
