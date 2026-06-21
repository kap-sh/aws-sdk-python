"""Generated from Smithy shape ``com.amazonaws.ssm#PingStatus``."""

from typing import Literal, TypeAlias, cast

PingStatus: TypeAlias = Literal[
    "Online",
    "ConnectionLost",
    "Inactive",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PingStatus:
    return cast(PingStatus, data)
