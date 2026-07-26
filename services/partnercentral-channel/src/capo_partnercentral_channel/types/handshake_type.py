"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#HandshakeType``."""

from typing import Literal, TypeAlias, cast

HandshakeType: TypeAlias = Literal[
    "START_SERVICE_PERIOD",
    "REVOKE_SERVICE_PERIOD",
    "PROGRAM_MANAGEMENT_ACCOUNT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HandshakeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HandshakeType:
    return cast(HandshakeType, data)
