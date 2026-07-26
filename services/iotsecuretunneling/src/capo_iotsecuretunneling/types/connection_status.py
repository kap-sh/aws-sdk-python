"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

ConnectionStatus: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionStatus:
    return cast(ConnectionStatus, data)
