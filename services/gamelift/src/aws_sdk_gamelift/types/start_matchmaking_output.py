"""Generated from Smithy shape ``com.amazonaws.gamelift#StartMatchmakingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matchmaking_ticket


class StartMatchmakingOutput(TypedDict, closed=True):
    matchmaking_ticket: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_ticket.MatchmakingTicket"
    ]
    """<p>Ticket representing the matchmaking request. This object include the information included in the request, ticket status, and match results as generated during the matchmaking process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMatchmakingOutput) -> dict:
    out: dict = {}
    if "matchmaking_ticket" in value:
        import aws_sdk_gamelift.types.matchmaking_ticket

        out["MatchmakingTicket"] = (
            aws_sdk_gamelift.types.matchmaking_ticket.serialize_aws_json_1_1(
                value["matchmaking_ticket"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMatchmakingOutput:
    out: StartMatchmakingOutput = {}  # type: ignore[typeddict-item]
    if "MatchmakingTicket" in data:
        import aws_sdk_gamelift.types.matchmaking_ticket

        out["matchmaking_ticket"] = (
            aws_sdk_gamelift.types.matchmaking_ticket.deserialize_aws_json_1_1(
                data["MatchmakingTicket"]
            )
        )
    return out
