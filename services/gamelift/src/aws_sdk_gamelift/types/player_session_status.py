"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerSessionStatus``."""

from typing import Literal, TypeAlias, cast

PlayerSessionStatus: TypeAlias = Literal[
    "RESERVED",
    "ACTIVE",
    "COMPLETED",
    "TIMEDOUT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerSessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlayerSessionStatus:
    return cast(PlayerSessionStatus, data)
