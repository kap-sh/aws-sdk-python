"""Generated from Smithy shape ``com.amazonaws.gamelift#ResumeGameServerGroupInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_group_actions
    import aws_sdk_gamelift.types.game_server_group_name_or_arn


class ResumeGameServerGroupInput(TypedDict):
    game_server_group_name: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>A unique identifier for the game server group. Use either the name or ARN value.</p>"""
    resume_actions: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_actions.GameServerGroupActions"
    ]
    """<p>The activity to resume for this game server group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResumeGameServerGroupInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "resume_actions" in value:
        import aws_sdk_gamelift.types.game_server_group_actions

        out["ResumeActions"] = (
            aws_sdk_gamelift.types.game_server_group_actions.serialize_aws_json_1_1(
                value["resume_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResumeGameServerGroupInput:
    out: ResumeGameServerGroupInput = {}  # type: ignore[typeddict-item]
    if "GameServerGroupName" in data:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if "ResumeActions" in data:
        import aws_sdk_gamelift.types.game_server_group_actions

        out["resume_actions"] = (
            aws_sdk_gamelift.types.game_server_group_actions.deserialize_aws_json_1_1(
                data["ResumeActions"]
            )
        )
    return out
