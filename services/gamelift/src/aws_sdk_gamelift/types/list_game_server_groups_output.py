"""Generated from Smithy shape ``com.amazonaws.gamelift#ListGameServerGroupsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_groups
    import aws_sdk_gamelift.types.non_zero_and_max_string


class ListGameServerGroupsOutput(TypedDict):
    game_server_groups: NotRequired[
        "aws_sdk_gamelift.types.game_server_groups.GameServerGroups"
    ]
    """<p>The game server groups' game server groups.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGameServerGroupsOutput) -> dict:
    out: dict = {}
    if "game_server_groups" in value:
        import aws_sdk_gamelift.types.game_server_groups

        out["GameServerGroups"] = (
            aws_sdk_gamelift.types.game_server_groups.serialize_aws_json_1_1(
                value["game_server_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGameServerGroupsOutput:
    out: ListGameServerGroupsOutput = {}  # type: ignore[typeddict-item]
    if "GameServerGroups" in data:
        import aws_sdk_gamelift.types.game_server_groups

        out["game_server_groups"] = (
            aws_sdk_gamelift.types.game_server_groups.deserialize_aws_json_1_1(
                data["GameServerGroups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
