"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.player_session

PlayerSessionList: TypeAlias = list[
    "aws_sdk_gamelift.types.player_session.PlayerSession"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerSessionList) -> list:
    import aws_sdk_gamelift.types.player_session

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.player_session.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PlayerSessionList:
    import aws_sdk_gamelift.types.player_session

    out: PlayerSessionList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.player_session.deserialize_aws_json_1_1(item))
    return out
