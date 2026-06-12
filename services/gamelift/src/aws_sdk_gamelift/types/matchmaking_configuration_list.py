"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matchmaking_configuration

MatchmakingConfigurationList: TypeAlias = list[
    "aws_sdk_gamelift.types.matchmaking_configuration.MatchmakingConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingConfigurationList) -> list:
    import aws_sdk_gamelift.types.matchmaking_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.matchmaking_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MatchmakingConfigurationList:
    import aws_sdk_gamelift.types.matchmaking_configuration

    out: MatchmakingConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.matchmaking_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
