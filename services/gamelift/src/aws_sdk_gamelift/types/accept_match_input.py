"""Generated from Smithy shape ``com.amazonaws.gamelift#AcceptMatchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.acceptance_type
    import aws_sdk_gamelift.types.matchmaking_id_string_model
    import aws_sdk_gamelift.types.player_ids_for_accept_match


class AcceptMatchInput(TypedDict, closed=True):
    ticket_id: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
    ]
    """<p>A unique identifier for a matchmaking ticket. The ticket must be in status <code>REQUIRES_ACCEPTANCE</code>; otherwise this request will fail.</p>"""
    player_ids: NotRequired[
        "aws_sdk_gamelift.types.player_ids_for_accept_match.PlayerIdsForAcceptMatch"
    ]
    """<p>A unique identifier for a player delivering the response. This parameter can include one or multiple player IDs.</p>"""
    acceptance_type: NotRequired[
        "aws_sdk_gamelift.types.acceptance_type.AcceptanceType"
    ]
    """<p>Player response to the proposed match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptMatchInput) -> dict:
    out: dict = {}
    if "ticket_id" in value:
        out["TicketId"] = value["ticket_id"]
    if "player_ids" in value:
        import aws_sdk_gamelift.types.player_ids_for_accept_match

        out["PlayerIds"] = (
            aws_sdk_gamelift.types.player_ids_for_accept_match.serialize_aws_json_1_1(
                value["player_ids"]
            )
        )
    if "acceptance_type" in value:
        import aws_sdk_gamelift.types.acceptance_type

        out["AcceptanceType"] = (
            aws_sdk_gamelift.types.acceptance_type.serialize_aws_json_1_1(
                value["acceptance_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptMatchInput:
    out: AcceptMatchInput = {}  # type: ignore[typeddict-item]
    if "TicketId" in data:
        out["ticket_id"] = data["TicketId"]
    if "PlayerIds" in data:
        import aws_sdk_gamelift.types.player_ids_for_accept_match

        out["player_ids"] = (
            aws_sdk_gamelift.types.player_ids_for_accept_match.deserialize_aws_json_1_1(
                data["PlayerIds"]
            )
        )
    if "AcceptanceType" in data:
        import aws_sdk_gamelift.types.acceptance_type

        out["acceptance_type"] = (
            aws_sdk_gamelift.types.acceptance_type.deserialize_aws_json_1_1(
                data["AcceptanceType"]
            )
        )
    return out
