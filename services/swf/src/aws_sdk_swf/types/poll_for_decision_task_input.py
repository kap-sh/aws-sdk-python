"""Generated from Smithy shape ``com.amazonaws.swf#PollForDecisionTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.identity
    import aws_sdk_swf.types.page_size
    import aws_sdk_swf.types.page_token
    import aws_sdk_swf.types.reverse_order
    import aws_sdk_swf.types.start_at_previous_started_event
    import aws_sdk_swf.types.task_list


class PollForDecisionTaskInput(TypedDict):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the task lists to poll.</p>"""
    task_list: "aws_sdk_swf.types.task_list.TaskList"
    r"""<p>Specifies the task list to poll for decision tasks.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    identity: NotRequired["aws_sdk_swf.types.identity.Identity"]
    """<p>Identity of the decider making the request, which is recorded in the DecisionTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.</p>"""
    next_page_token: NotRequired["aws_sdk_swf.types.page_token.PageToken"]
    r"""<p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: \"<code>Specified token has exceeded its maximum lifetime</code>\". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p> <note> <p>The <code>nextPageToken</code> returned by this action cannot be used with <a>GetWorkflowExecutionHistory</a> to get the next page. You must call <a>PollForDecisionTask</a> again (with the <code>nextPageToken</code>) to retrieve the next page of history records. Calling <a>PollForDecisionTask</a> with a <code>nextPageToken</code> doesn't return a new decision task.</p> </note>"""
    maximum_page_size: "aws_sdk_swf.types.page_size.PageSize"
    """<p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p> <p>This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.</p>"""
    reverse_order: "aws_sdk_swf.types.reverse_order.ReverseOrder"
    """<p>When set to <code>true</code>, returns the events in reverse order. By default the results are returned in ascending order of the <code>eventTimestamp</code> of the events.</p>"""
    start_at_previous_started_event: (
        "aws_sdk_swf.types.start_at_previous_started_event.StartAtPreviousStartedEvent"
    )
    """<p>When set to <code>true</code>, returns the events with <code>eventTimestamp</code> greater than or equal to <code>eventTimestamp</code> of the most recent <code>DecisionTaskStarted</code> event. By default, this parameter is set to <code>false</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PollForDecisionTaskInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_swf.types.task_list

    out["taskList"] = aws_sdk_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    if "identity" in value:
        out["identity"] = value["identity"]
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    out["maximumPageSize"] = value.get("maximum_page_size", 0)
    out["reverseOrder"] = value.get("reverse_order", False)
    out["startAtPreviousStartedEvent"] = value.get(
        "start_at_previous_started_event", False
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PollForDecisionTaskInput:
    out: PollForDecisionTaskInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("PollForDecisionTaskInput.domain required")
    if "taskList" in data:
        import aws_sdk_swf.types.task_list

        out["task_list"] = aws_sdk_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    else:
        raise DeserializationError("PollForDecisionTaskInput.task_list required")
    if "identity" in data:
        out["identity"] = data["identity"]
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
    if "startAtPreviousStartedEvent" in data:
        out["start_at_previous_started_event"] = data["startAtPreviousStartedEvent"]
    else:
        out["start_at_previous_started_event"] = False
    return out
