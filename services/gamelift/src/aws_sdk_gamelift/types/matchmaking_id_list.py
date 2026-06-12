"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matchmaking_id_string_model

MatchmakingIdList: TypeAlias = list[
    "aws_sdk_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MatchmakingIdList:
    return list(data)
