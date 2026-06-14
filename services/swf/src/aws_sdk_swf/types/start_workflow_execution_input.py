"""Generated from Smithy shape ``com.amazonaws.swf#StartWorkflowExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.arn
    import aws_sdk_swf.types.child_policy
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.duration_in_seconds_optional
    import aws_sdk_swf.types.tag_list
    import aws_sdk_swf.types.task_list
    import aws_sdk_swf.types.task_priority
    import aws_sdk_swf.types.workflow_id
    import aws_sdk_swf.types.workflow_type


class StartWorkflowExecutionInput(TypedDict):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    r"""<p>The name of the domain in which the workflow execution is created.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    workflow_id: "aws_sdk_swf.types.workflow_id.WorkflowId"
    r"""<p>The user defined identifier associated with the workflow execution. You can use this to associate a custom identifier with the workflow execution. You may specify the same identifier if a workflow execution is logically a <i>restart</i> of a previous execution. You cannot have two open workflow executions with the same <code>workflowId</code> at the same time within the same domain.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    workflow_type: "aws_sdk_swf.types.workflow_type.WorkflowType"
    """<p>The type of the workflow to start.</p>"""
    task_list: NotRequired["aws_sdk_swf.types.task_list.TaskList"]
    r"""<p>The task list to use for the decision tasks generated for this workflow execution. This overrides the <code>defaultTaskList</code> specified when registering the workflow type.</p> <note> <p>A task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault is returned.</p> </note> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    task_priority: NotRequired["aws_sdk_swf.types.task_priority.TaskPriority"]
    r"""<p>The task priority to use for this workflow execution. This overrides any default priority that was assigned when the workflow type was registered. If not set, then the default task priority for the workflow type is used. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href=\"https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html\">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    input: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>The input for the workflow execution. This is a free form string which should be meaningful to the workflow you are starting. This <code>input</code> is made available to the new workflow execution in the <code>WorkflowExecutionStarted</code> history event.</p>"""
    execution_start_to_close_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    r"""<p>The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.</p> <p>The duration is specified in seconds; an integer greater than or equal to <code>0</code>. Exceeding this limit causes the workflow execution to time out. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of \"NONE\" for this timeout; there is a one-year max limit on the time that a workflow execution can run.</p> <note> <p>An execution start-to-close timeout must be specified either through this parameter or as a default when the workflow type is registered. If neither this parameter nor a default execution start-to-close timeout is specified, a fault is returned.</p> </note>"""
    tag_list: NotRequired["aws_sdk_swf.types.tag_list.TagList"]
    """<p>The list of tags to associate with the workflow execution. You can specify a maximum of 5 tags. You can list workflow executions with a specific tag by calling <a>ListOpenWorkflowExecutions</a> or <a>ListClosedWorkflowExecutions</a> and specifying a <a>TagFilter</a>.</p>"""
    task_start_to_close_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the <code>defaultTaskStartToCloseTimout</code> specified when registering the workflow type using <a>RegisterWorkflowType</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p> <note> <p>A task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault is returned.</p> </note>"""
    child_policy: NotRequired["aws_sdk_swf.types.child_policy.ChildPolicy"]
    """<p>If set, specifies the policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the <a>TerminateWorkflowExecution</a> action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using <a>RegisterWorkflowType</a>.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul> <note> <p>A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.</p> </note>"""
    lambda_role: NotRequired["aws_sdk_swf.types.arn.Arn"]
    r"""<p>The IAM role to attach to this workflow execution.</p> <note> <p>Executions of this workflow type need IAM roles to invoke Lambda functions. If you don't attach an IAM role, any attempt to schedule a Lambda task fails. This results in a <code>ScheduleLambdaFunctionFailed</code> history event. For more information, see <a href=\"https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html\">https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html</a> in the <i>Amazon SWF Developer Guide</i>.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartWorkflowExecutionInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["workflowId"] = value["workflow_id"]
    import aws_sdk_swf.types.workflow_type

    out["workflowType"] = aws_sdk_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    if "task_list" in value:
        import aws_sdk_swf.types.task_list

        out["taskList"] = aws_sdk_swf.types.task_list.serialize_aws_json_1_0(
            value["task_list"]
        )
    if "task_priority" in value:
        out["taskPriority"] = value["task_priority"]
    if "input" in value:
        out["input"] = value["input"]
    if "execution_start_to_close_timeout" in value:
        out["executionStartToCloseTimeout"] = value["execution_start_to_close_timeout"]
    if "tag_list" in value:
        import aws_sdk_swf.types.tag_list

        out["tagList"] = aws_sdk_swf.types.tag_list.serialize_aws_json_1_0(
            value["tag_list"]
        )
    if "task_start_to_close_timeout" in value:
        out["taskStartToCloseTimeout"] = value["task_start_to_close_timeout"]
    if "child_policy" in value:
        import aws_sdk_swf.types.child_policy

        out["childPolicy"] = aws_sdk_swf.types.child_policy.serialize_aws_json_1_0(
            value["child_policy"]
        )
    if "lambda_role" in value:
        out["lambdaRole"] = value["lambda_role"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartWorkflowExecutionInput:
    out: StartWorkflowExecutionInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("StartWorkflowExecutionInput.domain required")
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("StartWorkflowExecutionInput.workflow_id required")
    if "workflowType" in data:
        import aws_sdk_swf.types.workflow_type

        out["workflow_type"] = aws_sdk_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError("StartWorkflowExecutionInput.workflow_type required")
    if "taskList" in data:
        import aws_sdk_swf.types.task_list

        out["task_list"] = aws_sdk_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    if "taskPriority" in data:
        out["task_priority"] = data["taskPriority"]
    if "input" in data:
        out["input"] = data["input"]
    if "executionStartToCloseTimeout" in data:
        out["execution_start_to_close_timeout"] = data["executionStartToCloseTimeout"]
    if "tagList" in data:
        import aws_sdk_swf.types.tag_list

        out["tag_list"] = aws_sdk_swf.types.tag_list.deserialize_aws_json_1_0(
            data["tagList"]
        )
    if "taskStartToCloseTimeout" in data:
        out["task_start_to_close_timeout"] = data["taskStartToCloseTimeout"]
    if "childPolicy" in data:
        import aws_sdk_swf.types.child_policy

        out["child_policy"] = aws_sdk_swf.types.child_policy.deserialize_aws_json_1_0(
            data["childPolicy"]
        )
    if "lambdaRole" in data:
        out["lambda_role"] = data["lambdaRole"]
    return out
