"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#GameLaunchArgList``."""

from typing import TypeAlias

GameLaunchArgList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: GameLaunchArgList) -> list:
    return list(value)


def deserialize_json(data: list) -> GameLaunchArgList:
    return list(data)
