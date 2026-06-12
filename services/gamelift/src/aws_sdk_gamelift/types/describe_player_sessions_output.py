"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribePlayerSessionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.player_session_list


class DescribePlayerSessionsOutput(TypedDict):
    player_sessions: NotRequired[
        "aws_sdk_gamelift.types.player_session_list.PlayerSessionList"
    ]
    """<p>A collection of objects containing properties for each player session that matches the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePlayerSessionsOutput) -> dict:
    out: dict = {}
    if "player_sessions" in value:
        import aws_sdk_gamelift.types.player_session_list

        out["PlayerSessions"] = (
            aws_sdk_gamelift.types.player_session_list.serialize_aws_json_1_1(
                value["player_sessions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePlayerSessionsOutput:
    out: DescribePlayerSessionsOutput = {}  # type: ignore[typeddict-item]
    if "PlayerSessions" in data:
        import aws_sdk_gamelift.types.player_session_list

        out["player_sessions"] = (
            aws_sdk_gamelift.types.player_session_list.deserialize_aws_json_1_1(
                data["PlayerSessions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
