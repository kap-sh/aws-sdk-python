"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ParticipantType``."""

from typing import Literal, TypeAlias, cast

ParticipantType: TypeAlias = Literal[
    "SENDER",
    "RECEIVER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParticipantType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ParticipantType:
    return cast(ParticipantType, data)
