"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingTicket``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session_connection_info
    import aws_sdk_gamelift.types.matchmaking_configuration_arn
    import aws_sdk_gamelift.types.matchmaking_configuration_status
    import aws_sdk_gamelift.types.matchmaking_id_string_model
    import aws_sdk_gamelift.types.player_list
    import aws_sdk_gamelift.types.string_model
    import aws_sdk_gamelift.types.timestamp
    import aws_sdk_gamelift.types.whole_number


class MatchmakingTicket(TypedDict, closed=True):
    ticket_id: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
    ]
    """<p>A unique identifier for a matchmaking ticket.</p>"""
    configuration_name: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
    ]
    """<p>Name of the matchmaking configuration that is used with this ticket. Matchmaking configurations determine how players are grouped into a match and how a new game session is created for the match.</p>"""
    configuration_arn: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_configuration_arn.MatchmakingConfigurationArn"
    ]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) associated with the GameLift matchmaking configuration resource that is used with this ticket.</p>"""
    status: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_configuration_status.MatchmakingConfigurationStatus"
    ]
    """<p>Current status of the matchmaking request.</p> <ul> <li> <p> <b>QUEUED</b> -- The matchmaking request has been received and is currently waiting to be processed.</p> </li> <li> <p> <b>SEARCHING</b> -- The matchmaking request is currently being processed. </p> </li> <li> <p> <b>REQUIRES_ACCEPTANCE</b> -- A match has been proposed and the players must accept the match. This status is used only with requests that use a matchmaking configuration with a player acceptance requirement.</p> </li> <li> <p> <b>PLACING</b> -- The FlexMatch engine has matched players and is in the process of placing a new game session for the match.</p> </li> <li> <p> <b>COMPLETED</b> -- Players have been matched and a game session is ready to host the players. A ticket in this state contains the necessary connection information for players.</p> </li> <li> <p> <b>FAILED</b> -- The matchmaking request was not completed.</p> </li> <li> <p> <b>CANCELLED</b> -- The matchmaking request was canceled. This may be the result of a <code>StopMatchmaking</code> operation or a proposed match that one or more players failed to accept.</p> </li> <li> <p> <b>TIMED_OUT</b> -- The matchmaking request was not successful within the duration specified in the matchmaking configuration. </p> </li> </ul> <note> <p>Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED, TIMED_OUT) can be resubmitted as new requests with new ticket IDs.</p> </note>"""
    status_reason: NotRequired["aws_sdk_gamelift.types.string_model.StringModel"]
    """<p>Code to explain the current status. For example, a status reason may indicate when a ticket has returned to <code>SEARCHING</code> status after a proposed match fails to receive player acceptances.</p>"""
    status_message: NotRequired["aws_sdk_gamelift.types.string_model.StringModel"]
    """<p>Additional information about the current status.</p>"""
    start_time: NotRequired["aws_sdk_gamelift.types.timestamp.Timestamp"]
    r"""<p>Time stamp indicating when this matchmaking request was received. Format is a number expressed in Unix time as milliseconds (for example <code>\"1469498468.057\"</code>).</p>"""
    end_time: NotRequired["aws_sdk_gamelift.types.timestamp.Timestamp"]
    r"""<p>Time stamp indicating when the matchmaking request stopped being processed due to successful completion, timeout, or cancellation. Format is a number expressed in Unix time as milliseconds (for example <code>\"1469498468.057\"</code>).</p>"""
    players: NotRequired["aws_sdk_gamelift.types.player_list.PlayerList"]
    """<p>A set of <code>Player</code> objects, each representing a player to find matches for. Players are identified by a unique player ID and may include latency data for use during matchmaking. If the ticket is in status <code>COMPLETED</code>, the <code>Player</code> objects include the team the players were assigned to in the resulting match.</p>"""
    game_session_connection_info: NotRequired[
        "aws_sdk_gamelift.types.game_session_connection_info.GameSessionConnectionInfo"
    ]
    r"""<p>Connection information for a new game session. Once a match is made, the FlexMatch engine creates a new game session for it. This information is added to the matchmaking ticket, which you can be retrieve by calling <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeMatchmaking.html\">DescribeMatchmaking</a> .</p>"""
    estimated_wait_time: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>Average amount of time (in seconds) that players are currently waiting for a match. If there is not enough recent data, this property may be empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingTicket) -> dict:
    out: dict = {}
    if "ticket_id" in value:
        out["TicketId"] = value["ticket_id"]
    if "configuration_name" in value:
        out["ConfigurationName"] = value["configuration_name"]
    if "configuration_arn" in value:
        out["ConfigurationArn"] = value["configuration_arn"]
    if "status" in value:
        import aws_sdk_gamelift.types.matchmaking_configuration_status

        out["Status"] = (
            aws_sdk_gamelift.types.matchmaking_configuration_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "start_time" in value:
        import aws_sdk_gamelift.types.timestamp

        out["StartTime"] = aws_sdk_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_gamelift.types.timestamp

        out["EndTime"] = aws_sdk_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "players" in value:
        import aws_sdk_gamelift.types.player_list

        out["Players"] = aws_sdk_gamelift.types.player_list.serialize_aws_json_1_1(
            value["players"]
        )
    if "game_session_connection_info" in value:
        import aws_sdk_gamelift.types.game_session_connection_info

        out["GameSessionConnectionInfo"] = (
            aws_sdk_gamelift.types.game_session_connection_info.serialize_aws_json_1_1(
                value["game_session_connection_info"]
            )
        )
    if "estimated_wait_time" in value:
        out["EstimatedWaitTime"] = value["estimated_wait_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MatchmakingTicket:
    out: MatchmakingTicket = {}  # type: ignore[typeddict-item]
    if "TicketId" in data:
        out["ticket_id"] = data["TicketId"]
    if "ConfigurationName" in data:
        out["configuration_name"] = data["ConfigurationName"]
    if "ConfigurationArn" in data:
        out["configuration_arn"] = data["ConfigurationArn"]
    if "Status" in data:
        import aws_sdk_gamelift.types.matchmaking_configuration_status

        out["status"] = (
            aws_sdk_gamelift.types.matchmaking_configuration_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "StartTime" in data:
        import aws_sdk_gamelift.types.timestamp

        out["start_time"] = aws_sdk_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_gamelift.types.timestamp

        out["end_time"] = aws_sdk_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Players" in data:
        import aws_sdk_gamelift.types.player_list

        out["players"] = aws_sdk_gamelift.types.player_list.deserialize_aws_json_1_1(
            data["Players"]
        )
    if "GameSessionConnectionInfo" in data:
        import aws_sdk_gamelift.types.game_session_connection_info

        out["game_session_connection_info"] = (
            aws_sdk_gamelift.types.game_session_connection_info.deserialize_aws_json_1_1(
                data["GameSessionConnectionInfo"]
            )
        )
    if "EstimatedWaitTime" in data:
        out["estimated_wait_time"] = data["EstimatedWaitTime"]
    return out
