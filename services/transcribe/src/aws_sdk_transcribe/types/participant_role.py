"""Generated from Smithy shape ``com.amazonaws.transcribe#ParticipantRole``."""

from typing import Literal, TypeAlias, cast

ParticipantRole: TypeAlias = Literal[
    "AGENT",
    "CUSTOMER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParticipantRole) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParticipantRole:
    return cast(ParticipantRole, data)
