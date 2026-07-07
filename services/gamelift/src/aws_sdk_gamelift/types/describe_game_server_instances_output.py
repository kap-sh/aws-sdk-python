"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameServerInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_instances
    import aws_sdk_gamelift.types.non_zero_and_max_string


class DescribeGameServerInstancesOutput(TypedDict, closed=True):
    game_server_instances: NotRequired[
        "aws_sdk_gamelift.types.game_server_instances.GameServerInstances"
    ]
    """<p>The collection of requested game server instances.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameServerInstancesOutput) -> dict:
    out: dict = {}
    if "game_server_instances" in value:
        import aws_sdk_gamelift.types.game_server_instances

        out["GameServerInstances"] = (
            aws_sdk_gamelift.types.game_server_instances.serialize_aws_json_1_1(
                value["game_server_instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameServerInstancesOutput:
    out: DescribeGameServerInstancesOutput = {}  # type: ignore[typeddict-item]
    if "GameServerInstances" in data:
        import aws_sdk_gamelift.types.game_server_instances

        out["game_server_instances"] = (
            aws_sdk_gamelift.types.game_server_instances.deserialize_aws_json_1_1(
                data["GameServerInstances"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
