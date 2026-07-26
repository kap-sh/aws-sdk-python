"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakePartyType``."""

from typing import Literal, TypeAlias, cast

HandshakePartyType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATION",
    "EMAIL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakePartyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HandshakePartyType:
    return cast(HandshakePartyType, data)
