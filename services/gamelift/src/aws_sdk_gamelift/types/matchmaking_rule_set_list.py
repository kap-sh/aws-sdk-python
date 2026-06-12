"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingRuleSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matchmaking_rule_set

MatchmakingRuleSetList: TypeAlias = list[
    "aws_sdk_gamelift.types.matchmaking_rule_set.MatchmakingRuleSet"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingRuleSetList) -> list:
    import aws_sdk_gamelift.types.matchmaking_rule_set

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.matchmaking_rule_set.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MatchmakingRuleSetList:
    import aws_sdk_gamelift.types.matchmaking_rule_set

    out: MatchmakingRuleSetList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.matchmaking_rule_set.deserialize_aws_json_1_1(item)
        )
    return out
