"""Generated from Smithy shape ``com.amazonaws.gamelift#GamePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.game_property

GamePropertyList: TypeAlias = list["capo_gamelift.types.game_property.GameProperty"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GamePropertyList) -> list:
    import capo_gamelift.types.game_property

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.game_property.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GamePropertyList:
    import capo_gamelift.types.game_property

    out: GamePropertyList = []
    for item in data:
        out.append(capo_gamelift.types.game_property.deserialize_aws_json_1_1(item))
    return out
