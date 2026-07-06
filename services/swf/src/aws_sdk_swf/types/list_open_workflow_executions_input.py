"""Generated from Smithy shape ``com.amazonaws.swf#ListOpenWorkflowExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.execution_time_filter
    import aws_sdk_swf.types.page_size
    import aws_sdk_swf.types.page_token
    import aws_sdk_swf.types.reverse_order
    import aws_sdk_swf.types.tag_filter
    import aws_sdk_swf.types.workflow_execution_filter
    import aws_sdk_swf.types.workflow_type_filter


class ListOpenWorkflowExecutionsInput(TypedDict, closed=True):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain that contains the workflow executions to list.</p>"""
    start_time_filter: "aws_sdk_swf.types.execution_time_filter.ExecutionTimeFilter"
    """<p>Workflow executions are included in the returned results based on whether their start times are within the range specified by this filter.</p>"""
    type_filter: NotRequired[
        "aws_sdk_swf.types.workflow_type_filter.WorkflowTypeFilter"
    ]
    """<p>If specified, only executions of the type specified in the filter are returned.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    tag_filter: NotRequired["aws_sdk_swf.types.tag_filter.TagFilter"]
    """<p>If specified, only executions that have the matching tag are listed.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    next_page_token: NotRequired["aws_sdk_swf.types.page_token.PageToken"]
    r"""<p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: \"<code>Specified token has exceeded its maximum lifetime</code>\". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>"""
    maximum_page_size: "aws_sdk_swf.types.page_size.PageSize"
    """<p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>"""
    reverse_order: "aws_sdk_swf.types.reverse_order.ReverseOrder"
    """<p>When set to <code>true</code>, returns the results in reverse order. By default the results are returned in descending order of the start time of the executions.</p>"""
    execution_filter: NotRequired[
        "aws_sdk_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
    ]
    """<p>If specified, only workflow executions matching the workflow ID specified in the filter are returned.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOpenWorkflowExecutionsInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_swf.types.execution_time_filter

    out["startTimeFilter"] = (
        aws_sdk_swf.types.execution_time_filter.serialize_aws_json_1_0(
            value["start_time_filter"]
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
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    out["maximumPageSize"] = value.get("maximum_page_size", 0)
    out["reverseOrder"] = value.get("reverse_order", False)
    if "execution_filter" in value:
        import aws_sdk_swf.types.workflow_execution_filter

        out["executionFilter"] = (
            aws_sdk_swf.types.workflow_execution_filter.serialize_aws_json_1_0(
                value["execution_filter"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOpenWorkflowExecutionsInput:
    out: ListOpenWorkflowExecutionsInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("ListOpenWorkflowExecutionsInput.domain required")
    if "startTimeFilter" in data:
        import aws_sdk_swf.types.execution_time_filter

        out["start_time_filter"] = (
            aws_sdk_swf.types.execution_time_filter.deserialize_aws_json_1_0(
                data["startTimeFilter"]
            )
        )
    else:
        raise DeserializationError(
            "ListOpenWorkflowExecutionsInput.start_time_filter required"
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
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    if "maximumPageSize" in data:
        out["maximum_page_size"] = data["maximumPageSize"]
    else:
        out["maximum_page_size"] = 0
    if "reverseOrder" in data:
        out["reverse_order"] = data["reverseOrder"]
    else:
        out["reverse_order"] = False
    if "executionFilter" in data:
        import aws_sdk_swf.types.workflow_execution_filter

        out["execution_filter"] = (
            aws_sdk_swf.types.workflow_execution_filter.deserialize_aws_json_1_0(
                data["executionFilter"]
            )
        )
    return out
