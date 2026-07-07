"""Generated from Smithy shape ``com.amazonaws.iot#ListCommandExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_execution_summary_list
    import aws_sdk_iot.types.next_token


class ListCommandExecutionsResponse(TypedDict, closed=True):
    command_executions: NotRequired[
        "aws_sdk_iot.types.command_execution_summary_list.CommandExecutionSummaryList"
    ]
    """<p>The list of command executions.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCommandExecutionsResponse) -> dict:
    out: dict = {}
    if "command_executions" in value:
        import aws_sdk_iot.types.command_execution_summary_list

        out["commandExecutions"] = (
            aws_sdk_iot.types.command_execution_summary_list.serialize_json(
                value["command_executions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCommandExecutionsResponse:
    out: ListCommandExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "commandExecutions" in data:
        import aws_sdk_iot.types.command_execution_summary_list

        out["command_executions"] = (
            aws_sdk_iot.types.command_execution_summary_list.deserialize_json(
                data["commandExecutions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
