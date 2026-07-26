"""Generated from Smithy shape ``com.amazonaws.directconnect#BGPStatus``."""

from typing import Literal, TypeAlias, cast

BGPStatus: TypeAlias = Literal[
    "up",
    "down",
    "unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BGPStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BGPStatus:
    return cast(BGPStatus, data)
