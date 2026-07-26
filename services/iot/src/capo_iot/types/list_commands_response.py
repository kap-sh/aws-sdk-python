"""Generated from Smithy shape ``com.amazonaws.iot#ListCommandsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.command_summary_list
    import capo_iot.types.next_token


class ListCommandsResponse(TypedDict, closed=True):
    commands: NotRequired["capo_iot.types.command_summary_list.CommandSummaryList"]
    """<p>The list of commands.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCommandsResponse) -> dict:
    out: dict = {}
    if "commands" in value:
        import capo_iot.types.command_summary_list

        out["commands"] = capo_iot.types.command_summary_list.serialize_json(
            value["commands"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCommandsResponse:
    out: ListCommandsResponse = {}  # type: ignore[typeddict-item]
    if "commands" in data:
        import capo_iot.types.command_summary_list

        out["commands"] = capo_iot.types.command_summary_list.deserialize_json(
            data["commands"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
