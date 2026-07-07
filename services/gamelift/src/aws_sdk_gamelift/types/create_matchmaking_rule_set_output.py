"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateMatchmakingRuleSetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matchmaking_rule_set


class CreateMatchmakingRuleSetOutput(TypedDict, closed=True):
    rule_set: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_rule_set.MatchmakingRuleSet"
    ]
    """<p>The newly created matchmaking rule set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMatchmakingRuleSetOutput) -> dict:
    out: dict = {}
    if "rule_set" in value:
        import aws_sdk_gamelift.types.matchmaking_rule_set

        out["RuleSet"] = (
            aws_sdk_gamelift.types.matchmaking_rule_set.serialize_aws_json_1_1(
                value["rule_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMatchmakingRuleSetOutput:
    out: CreateMatchmakingRuleSetOutput = {}  # type: ignore[typeddict-item]
    if "RuleSet" in data:
        import aws_sdk_gamelift.types.matchmaking_rule_set

        out["rule_set"] = (
            aws_sdk_gamelift.types.matchmaking_rule_set.deserialize_aws_json_1_1(
                data["RuleSet"]
            )
        )
    return out
