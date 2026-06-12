"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeMatchmakingOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matchmaking_ticket_list


class DescribeMatchmakingOutput(TypedDict):
    ticket_list: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_ticket_list.MatchmakingTicketList"
    ]
    """<p>A collection of existing matchmaking ticket objects matching the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMatchmakingOutput) -> dict:
    out: dict = {}
    if "ticket_list" in value:
        import aws_sdk_gamelift.types.matchmaking_ticket_list

        out["TicketList"] = (
            aws_sdk_gamelift.types.matchmaking_ticket_list.serialize_aws_json_1_1(
                value["ticket_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMatchmakingOutput:
    out: DescribeMatchmakingOutput = {}  # type: ignore[typeddict-item]
    if "TicketList" in data:
        import aws_sdk_gamelift.types.matchmaking_ticket_list

        out["ticket_list"] = (
            aws_sdk_gamelift.types.matchmaking_ticket_list.deserialize_aws_json_1_1(
                data["TicketList"]
            )
        )
    return out
