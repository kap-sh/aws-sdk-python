"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingConfigurationNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_configuration_name

MatchmakingConfigurationNameList: TypeAlias = list[
    "capo_gamelift.types.matchmaking_configuration_name.MatchmakingConfigurationName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingConfigurationNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MatchmakingConfigurationNameList:
    return list(data)
