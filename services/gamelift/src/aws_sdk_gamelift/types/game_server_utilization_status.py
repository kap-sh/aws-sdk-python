"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerUtilizationStatus``."""

from typing import Literal, TypeAlias, cast

GameServerUtilizationStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UTILIZED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerUtilizationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerUtilizationStatus:
    return cast(GameServerUtilizationStatus, data)
