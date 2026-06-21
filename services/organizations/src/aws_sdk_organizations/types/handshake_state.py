"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeState``."""

from typing import Literal, TypeAlias, cast

HandshakeState: TypeAlias = Literal[
    "REQUESTED",
    "OPEN",
    "CANCELED",
    "ACCEPTED",
    "DECLINED",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakeState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HandshakeState:
    return cast(HandshakeState, data)
