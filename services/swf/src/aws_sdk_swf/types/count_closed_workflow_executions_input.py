"""Generated from Smithy shape ``com.amazonaws.swf#CountClosedWorkflowExecutionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.close_status_filter
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.execution_time_filter
    import aws_sdk_swf.types.tag_filter
    import aws_sdk_swf.types.workflow_execution_filter
    import aws_sdk_swf.types.workflow_type_filter


class CountClosedWorkflowExecutionsInput(TypedDict):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow executions to count.</p>"""
    start_time_filter: NotRequired[
        "aws_sdk_swf.types.execution_time_filter.ExecutionTimeFilter"
    ]
    """<p>If specified, only workflow executions that meet the start time criteria of the filter are counted.</p> <note> <p> <code>startTimeFilter</code> and <code>closeTimeFilter</code> are mutually exclusive. You must specify one of these in a request but not both.</p> </note>"""
    close_time_filter: NotRequired[
        "aws_sdk_swf.types.execution_time_filter.ExecutionTimeFilter"
    ]
    """<p>If specified, only workflow executions that meet the close time criteria of the filter are counted.</p> <note> <p> <code>startTimeFilter</code> and <code>closeTimeFilter</code> are mutually exclusive. You must specify one of these in a request but not both.</p> </note>"""
    execution_filter: NotRequired[
        "aws_sdk_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
    ]
    """<p>If specified, only workflow executions matching the <code>WorkflowId</code> in the filter are counted.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    type_filter: NotRequired[
        "aws_sdk_swf.types.workflow_type_filter.WorkflowTypeFilter"
    ]
    """<p>If specified, indicates the type of the workflow executions to be counted.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    tag_filter: NotRequired["aws_sdk_swf.types.tag_filter.TagFilter"]
    """<p>If specified, only executions that have a tag that matches the filter are counted.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    close_status_filter: NotRequired[
        "aws_sdk_swf.types.close_status_filter.CloseStatusFilter"
    ]
    """<p>If specified, only workflow executions that match this close status are counted. This filter has an affect only if <code>executionStatus</code> is specified as <code>CLOSED</code>.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountClosedWorkflowExecutionsInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    if "start_time_filter" in value:
        import aws_sdk_swf.types.execution_time_filter

        out["startTimeFilter"] = (
            aws_sdk_swf.types.execution_time_filter.serialize_aws_json_1_0(
                value["start_time_filter"]
            )
        )
    if "close_time_filter" in value:
        import aws_sdk_swf.types.execution_time_filter

        out["closeTimeFilter"] = (
            aws_sdk_swf.types.execution_time_filter.serialize_aws_json_1_0(
                value["close_time_filter"]
            )
        )
    if "execution_filter" in value:
        import aws_sdk_swf.types.workflow_execution_filter

        out["executionFilter"] = (
            aws_sdk_swf.types.workflow_execution_filter.serialize_aws_json_1_0(
                value["execution_filter"]
            )
        )
    if "type_filter" in value:
        import aws_sdk_swf.types.workflow_type_filter

        out["typeFilter"] = (
            aws_sdk_swf.types.workflow_type_filter.serialize_aws_json_1_0(
                value["type_filter"]
            )
        )
    if "tag_filter" in value:
        import aws_sdk_swf.types.tag_filter

        out["tagFilter"] = aws_sdk_swf.types.tag_filter.serialize_aws_json_1_0(
            value["tag_filter"]
        )
    if "close_status_filter" in value:
        import aws_sdk_swf.types.close_status_filter

        out["closeStatusFilter"] = (
            aws_sdk_swf.types.close_status_filter.serialize_aws_json_1_0(
                value["close_status_filter"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CountClosedWorkflowExecutionsInput:
    out: CountClosedWorkflowExecutionsInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("CountClosedWorkflowExecutionsInput.domain required")
    if "startTimeFilter" in data:
        import aws_sdk_swf.types.execution_time_filter

        out["start_time_filter"] = (
            aws_sdk_swf.types.execution_time_filter.deserialize_aws_json_1_0(
                data["startTimeFilter"]
            )
        )
    if "closeTimeFilter" in data:
        import aws_sdk_swf.types.execution_time_filter

        out["close_time_filter"] = (
            aws_sdk_swf.types.execution_time_filter.deserialize_aws_json_1_0(
                data["closeTimeFilter"]
            )
        )
    if "executionFilter" in data:
        import aws_sdk_swf.types.workflow_execution_filter

        out["execution_filter"] = (
            aws_sdk_swf.types.workflow_execution_filter.deserialize_aws_json_1_0(
                data["executionFilter"]
            )
        )
    if "typeFilter" in data:
        import aws_sdk_swf.types.workflow_type_filter

        out["type_filter"] = (
            aws_sdk_swf.types.workflow_type_filter.deserialize_aws_json_1_0(
                data["typeFilter"]
            )
        )
    if "tagFilter" in data:
        import aws_sdk_swf.types.tag_filter

        out["tag_filter"] = aws_sdk_swf.types.tag_filter.deserialize_aws_json_1_0(
            data["tagFilter"]
        )
    if "closeStatusFilter" in data:
        import aws_sdk_swf.types.close_status_filter

        out["close_status_filter"] = (
            aws_sdk_swf.types.close_status_filter.deserialize_aws_json_1_0(
                data["closeStatusFilter"]
            )
        )
    return out
