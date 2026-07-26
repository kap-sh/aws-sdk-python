"""Generated from Smithy shape ``com.amazonaws.ssm#ListCommandsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.command_filter_list
    import capo_ssm.types.command_id
    import capo_ssm.types.command_max_results
    import capo_ssm.types.instance_id
    import capo_ssm.types.next_token


class ListCommandsRequest(TypedDict, closed=True):
    command_id: NotRequired["capo_ssm.types.command_id.CommandId"]
    """<p>(Optional) If provided, lists only the specified command.</p>"""
    instance_id: NotRequired["capo_ssm.types.instance_id.InstanceId"]
    """<p>(Optional) Lists commands issued against this managed node ID.</p> <note> <p>You can't specify a managed node ID in the same command that you specify <code>Status</code> = <code>Pending</code>. This is because the command hasn't reached the managed node yet.</p> </note>"""
    max_results: NotRequired["capo_ssm.types.command_max_results.CommandMaxResults"]
    """<p>(Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>(Optional) The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    filters: NotRequired["capo_ssm.types.command_filter_list.CommandFilterList"]
    """<p>(Optional) One or more filters. Use a filter to return a more specific list of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommandsRequest) -> dict:
    out: dict = {}
    if "command_id" in value:
        out["CommandId"] = value["command_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_ssm.types.command_filter_list

        out["Filters"] = capo_ssm.types.command_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommandsRequest:
    out: ListCommandsRequest = {}  # type: ignore[typeddict-item]
    if "CommandId" in data:
        out["command_id"] = data["CommandId"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import capo_ssm.types.command_filter_list

        out["filters"] = capo_ssm.types.command_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    return out
