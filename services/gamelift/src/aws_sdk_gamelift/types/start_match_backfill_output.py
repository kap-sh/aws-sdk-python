"""Generated from Smithy shape ``com.amazonaws.gamelift#StartMatchBackfillOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matchmaking_ticket


class StartMatchBackfillOutput(TypedDict):
    matchmaking_ticket: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_ticket.MatchmakingTicket"
    ]
    """<p>Ticket representing the backfill matchmaking request. This object includes the information in the request, ticket status, and match results as generated during the matchmaking process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMatchBackfillOutput) -> dict:
    out: dict = {}
    if "matchmaking_ticket" in value:
        import aws_sdk_gamelift.types.matchmaking_ticket

        out["MatchmakingTicket"] = (
            aws_sdk_gamelift.types.matchmaking_ticket.serialize_aws_json_1_1(
                value["matchmaking_ticket"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMatchBackfillOutput:
    out: StartMatchBackfillOutput = {}  # type: ignore[typeddict-item]
    if "MatchmakingTicket" in data:
        import aws_sdk_gamelift.types.matchmaking_ticket

        out["matchmaking_ticket"] = (
            aws_sdk_gamelift.types.matchmaking_ticket.deserialize_aws_json_1_1(
                data["MatchmakingTicket"]
            )
        )
    return out
