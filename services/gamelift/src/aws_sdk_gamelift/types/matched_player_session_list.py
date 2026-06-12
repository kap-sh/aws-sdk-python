"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchedPlayerSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matched_player_session

MatchedPlayerSessionList: TypeAlias = list[
    "aws_sdk_gamelift.types.matched_player_session.MatchedPlayerSession"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchedPlayerSessionList) -> list:
    import aws_sdk_gamelift.types.matched_player_session

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.matched_player_session.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MatchedPlayerSessionList:
    import aws_sdk_gamelift.types.matched_player_session

    out: MatchedPlayerSessionList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.matched_player_session.deserialize_aws_json_1_1(item)
        )
    return out
