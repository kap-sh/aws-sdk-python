"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameSessionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session_list
    import aws_sdk_gamelift.types.non_zero_and_max_string


class DescribeGameSessionsOutput(TypedDict):
    game_sessions: NotRequired[
        "aws_sdk_gamelift.types.game_session_list.GameSessionList"
    ]
    """<p>A collection of properties for each game session that matches the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameSessionsOutput) -> dict:
    out: dict = {}
    if "game_sessions" in value:
        import aws_sdk_gamelift.types.game_session_list

        out["GameSessions"] = (
            aws_sdk_gamelift.types.game_session_list.serialize_aws_json_1_1(
                value["game_sessions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameSessionsOutput:
    out: DescribeGameSessionsOutput = {}  # type: ignore[typeddict-item]
    if "GameSessions" in data:
        import aws_sdk_gamelift.types.game_session_list

        out["game_sessions"] = (
            aws_sdk_gamelift.types.game_session_list.deserialize_aws_json_1_1(
                data["GameSessions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
