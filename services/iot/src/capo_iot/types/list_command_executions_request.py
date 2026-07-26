"""Generated from Smithy shape ``com.amazonaws.iot#ListCommandExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.command_arn
    import capo_iot.types.command_execution_status
    import capo_iot.types.command_max_results
    import capo_iot.types.command_namespace
    import capo_iot.types.next_token
    import capo_iot.types.sort_order
    import capo_iot.types.target_arn
    import capo_iot.types.time_filter


class ListCommandExecutionsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_iot.types.command_max_results.CommandMaxResults"]
    """<p>The maximum number of results to return in this operation.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.</p>"""
    namespace: NotRequired["capo_iot.types.command_namespace.CommandNamespace"]
    """<p>The namespace of the command.</p>"""
    status: NotRequired[
        "capo_iot.types.command_execution_status.CommandExecutionStatus"
    ]
    """<p>List all command executions for the device that have a particular status. For example, you can filter the list to display only command executions that have failed or timed out.</p>"""
    sort_order: NotRequired["capo_iot.types.sort_order.SortOrder"]
    """<p>Specify whether to list the command executions that were created in the ascending or descending order. By default, the API returns all commands in the descending order based on the start time or completion time of the executions, that are determined by the <code>startTimeFilter</code> and <code>completeTimeFilter</code> parameters.</p>"""
    started_time_filter: NotRequired["capo_iot.types.time_filter.TimeFilter"]
    """<p>List all command executions that started any time before or after the date and time that you specify. The date and time uses the format <code>yyyy-MM-dd'T'HH:mm</code>.</p>"""
    completed_time_filter: NotRequired["capo_iot.types.time_filter.TimeFilter"]
    """<p>List all command executions that completed any time before or after the date and time that you specify. The date and time uses the format <code>yyyy-MM-dd'T'HH:mm</code>.</p>"""
    target_arn: NotRequired["capo_iot.types.target_arn.TargetArn"]
    """<p>The Amazon Resource Number (ARN) of the target device. You can use this information to list all command executions for a particular device.</p>"""
    command_arn: NotRequired["capo_iot.types.command_arn.CommandArn"]
    """<p>The Amazon Resource Number (ARN) of the command. You can use this information to list all command executions for a particular command.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCommandExecutionsRequest) -> dict:
    out: dict = {}
    if "namespace" in value:
        import capo_iot.types.command_namespace

        out["namespace"] = capo_iot.types.command_namespace.serialize_json(
            value["namespace"]
        )
    if "status" in value:
        import capo_iot.types.command_execution_status

        out["status"] = capo_iot.types.command_execution_status.serialize_json(
            value["status"]
        )
    if "sort_order" in value:
        import capo_iot.types.sort_order

        out["sortOrder"] = capo_iot.types.sort_order.serialize_json(value["sort_order"])
    if "started_time_filter" in value:
        import capo_iot.types.time_filter

        out["startedTimeFilter"] = capo_iot.types.time_filter.serialize_json(
            value["started_time_filter"]
        )
    if "completed_time_filter" in value:
        import capo_iot.types.time_filter

        out["completedTimeFilter"] = capo_iot.types.time_filter.serialize_json(
            value["completed_time_filter"]
        )
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "command_arn" in value:
        out["commandArn"] = value["command_arn"]
    return out


def deserialize_json(data: dict) -> ListCommandExecutionsRequest:
    out: ListCommandExecutionsRequest = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        import capo_iot.types.command_namespace

        out["namespace"] = capo_iot.types.command_namespace.deserialize_json(
            data["namespace"]
        )
    if "status" in data:
        import capo_iot.types.command_execution_status

        out["status"] = capo_iot.types.command_execution_status.deserialize_json(
            data["status"]
        )
    if "sortOrder" in data:
        import capo_iot.types.sort_order

        out["sort_order"] = capo_iot.types.sort_order.deserialize_json(
            data["sortOrder"]
        )
    if "startedTimeFilter" in data:
        import capo_iot.types.time_filter

        out["started_time_filter"] = capo_iot.types.time_filter.deserialize_json(
            data["startedTimeFilter"]
        )
    if "completedTimeFilter" in data:
        import capo_iot.types.time_filter

        out["completed_time_filter"] = capo_iot.types.time_filter.deserialize_json(
            data["completedTimeFilter"]
        )
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    if "commandArn" in data:
        out["command_arn"] = data["commandArn"]
    return out
