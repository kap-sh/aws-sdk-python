"""Generated from Smithy shape ``com.amazonaws.swf#GetWorkflowExecutionHistoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.page_size
    import aws_sdk_swf.types.page_token
    import aws_sdk_swf.types.reverse_order
    import aws_sdk_swf.types.workflow_execution


class GetWorkflowExecutionHistoryInput(TypedDict, closed=True):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow execution.</p>"""
    execution: "aws_sdk_swf.types.workflow_execution.WorkflowExecution"
    """<p>Specifies the workflow execution for which to return the history.</p>"""
    next_page_token: NotRequired["aws_sdk_swf.types.page_token.PageToken"]
    r"""<p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: \"<code>Specified token has exceeded its maximum lifetime</code>\". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>"""
    maximum_page_size: "aws_sdk_swf.types.page_size.PageSize"
    """<p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>"""
    reverse_order: "aws_sdk_swf.types.reverse_order.ReverseOrder"
    """<p>When set to <code>true</code>, returns the events in reverse order. By default the results are returned in ascending order of the <code>eventTimeStamp</code> of the events.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkflowExecutionHistoryInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_swf.types.workflow_execution

    out["execution"] = aws_sdk_swf.types.workflow_execution.serialize_aws_json_1_0(
        value["execution"]
    )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    out["maximumPageSize"] = value.get("maximum_page_size", 0)
    out["reverseOrder"] = value.get("reverse_order", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkflowExecutionHistoryInput:
    out: GetWorkflowExecutionHistoryInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("GetWorkflowExecutionHistoryInput.domain required")
    if "execution" in data:
        import aws_sdk_swf.types.workflow_execution

        out["execution"] = (
            aws_sdk_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["execution"]
            )
        )
    else:
        raise DeserializationError(
            "GetWorkflowExecutionHistoryInput.execution required"
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
    return out
