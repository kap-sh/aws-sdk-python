"""Generated from Smithy shape ``com.amazonaws.gamelift#PlacedPlayerSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.placed_player_session

PlacedPlayerSessionList: TypeAlias = list[
    "aws_sdk_gamelift.types.placed_player_session.PlacedPlayerSession"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacedPlayerSessionList) -> list:
    import aws_sdk_gamelift.types.placed_player_session

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.placed_player_session.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PlacedPlayerSessionList:
    import aws_sdk_gamelift.types.placed_player_session

    out: PlacedPlayerSessionList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.placed_player_session.deserialize_aws_json_1_1(item)
        )
    return out
