"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#TunnelStatus``."""

from typing import Literal, TypeAlias, cast

TunnelStatus: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TunnelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TunnelStatus:
    return cast(TunnelStatus, data)
