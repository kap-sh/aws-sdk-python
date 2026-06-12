"""Generated from Smithy shape ``com.amazonaws.gamelift#ResourceCreationLimitPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.whole_number


class ResourceCreationLimitPolicy(TypedDict):
    new_game_sessions_per_creator: NotRequired[
        "aws_sdk_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources.</p> <p>The policy is evaluated when a player tries to create a new game session. On receiving a <code>CreateGameSession</code> request, Amazon GameLift Servers checks that the player (identified by <code>CreatorId</code>) has created fewer than game session limit in the specified time period.</p>"""
    policy_period_in_minutes: NotRequired[
        "aws_sdk_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The time span used in evaluating the resource creation limit policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCreationLimitPolicy) -> dict:
    out: dict = {}
    if "new_game_sessions_per_creator" in value:
        out["NewGameSessionsPerCreator"] = value["new_game_sessions_per_creator"]
    if "policy_period_in_minutes" in value:
        out["PolicyPeriodInMinutes"] = value["policy_period_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceCreationLimitPolicy:
    out: ResourceCreationLimitPolicy = {}  # type: ignore[typeddict-item]
    if "NewGameSessionsPerCreator" in data:
        out["new_game_sessions_per_creator"] = data["NewGameSessionsPerCreator"]
    if "PolicyPeriodInMinutes" in data:
        out["policy_period_in_minutes"] = data["PolicyPeriodInMinutes"]
    return out
