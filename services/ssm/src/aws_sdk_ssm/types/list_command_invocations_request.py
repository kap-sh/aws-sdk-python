"""Generated from Smithy shape ``com.amazonaws.ssm#ListCommandInvocationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.boolean
    import aws_sdk_ssm.types.command_filter_list
    import aws_sdk_ssm.types.command_id
    import aws_sdk_ssm.types.command_max_results
    import aws_sdk_ssm.types.instance_id
    import aws_sdk_ssm.types.next_token


class ListCommandInvocationsRequest(TypedDict):
    command_id: NotRequired["aws_sdk_ssm.types.command_id.CommandId"]
    """<p>(Optional) The invocations for a specific command ID.</p>"""
    instance_id: NotRequired["aws_sdk_ssm.types.instance_id.InstanceId"]
    """<p>(Optional) The command execution details for a specific managed node ID.</p>"""
    max_results: NotRequired["aws_sdk_ssm.types.command_max_results.CommandMaxResults"]
    """<p>(Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>(Optional) The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    filters: NotRequired["aws_sdk_ssm.types.command_filter_list.CommandFilterList"]
    """<p>(Optional) One or more filters. Use a filter to return a more specific list of results.</p>"""
    details: "aws_sdk_ssm.types.boolean.Boolean"
    """<p>(Optional) If set this returns the response of the command executions and any command output. The default value is <code>false</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommandInvocationsRequest) -> dict:
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
        import aws_sdk_ssm.types.command_filter_list

        out["Filters"] = aws_sdk_ssm.types.command_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    out["Details"] = value.get("details", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommandInvocationsRequest:
    out: ListCommandInvocationsRequest = {}  # type: ignore[typeddict-item]
    if "CommandId" in data:
        out["command_id"] = data["CommandId"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_ssm.types.command_filter_list

        out["filters"] = aws_sdk_ssm.types.command_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "Details" in data:
        out["details"] = data["Details"]
    else:
        out["details"] = False
    return out
