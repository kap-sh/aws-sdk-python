"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeMatchmakingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_id_list


class DescribeMatchmakingInput(TypedDict, closed=True):
    ticket_ids: NotRequired["capo_gamelift.types.matchmaking_id_list.MatchmakingIdList"]
    """<p>A unique identifier for a matchmaking ticket. You can include up to 10 ID values. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMatchmakingInput) -> dict:
    out: dict = {}
    if "ticket_ids" in value:
        import capo_gamelift.types.matchmaking_id_list

        out["TicketIds"] = (
            capo_gamelift.types.matchmaking_id_list.serialize_aws_json_1_1(
                value["ticket_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMatchmakingInput:
    out: DescribeMatchmakingInput = {}  # type: ignore[typeddict-item]
    if "TicketIds" in data:
        import capo_gamelift.types.matchmaking_id_list

        out["ticket_ids"] = (
            capo_gamelift.types.matchmaking_id_list.deserialize_aws_json_1_1(
                data["TicketIds"]
            )
        )
    return out
