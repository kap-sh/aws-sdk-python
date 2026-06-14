"""Generated from Smithy shape ``com.amazonaws.swf#ContinueAsNewWorkflowExecutionDecisionAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_swf.types.arn
    import aws_sdk_swf.types.child_policy
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.duration_in_seconds_optional
    import aws_sdk_swf.types.tag_list
    import aws_sdk_swf.types.task_list
    import aws_sdk_swf.types.task_priority
    import aws_sdk_swf.types.version


class ContinueAsNewWorkflowExecutionDecisionAttributes(TypedDict):
    input: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>The input provided to the new workflow execution.</p>"""
    execution_start_to_close_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>If set, specifies the total duration for this workflow execution. This overrides the <code>defaultExecutionStartToCloseTimeout</code> specified when registering the workflow type.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p> <note> <p>An execution start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this field. If neither this field is set nor a default execution start-to-close timeout was specified at registration time then a fault is returned.</p> </note>"""
    task_list: NotRequired["aws_sdk_swf.types.task_list.TaskList"]
    """<p>The task list to use for the decisions of the new (continued) workflow execution.</p>"""
    task_priority: NotRequired["aws_sdk_swf.types.task_priority.TaskPriority"]
    r"""<p> The task priority that, if set, specifies the priority for the decision tasks for this workflow execution. This overrides the defaultTaskPriority specified when registering the workflow type. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href=\"https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html\">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    task_start_to_close_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>Specifies the maximum duration of decision tasks for the new workflow execution. This parameter overrides the <code>defaultTaskStartToCloseTimout</code> specified when registering the workflow type using <a>RegisterWorkflowType</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p> <note> <p>A task start-to-close timeout for the new workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault is returned.</p> </note>"""
    child_policy: NotRequired["aws_sdk_swf.types.child_policy.ChildPolicy"]
    """<p>If set, specifies the policy to use for the child workflow executions of the new execution if it is terminated by calling the <a>TerminateWorkflowExecution</a> action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using <a>RegisterWorkflowType</a>.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul> <note> <p>A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.</p> </note>"""
    tag_list: NotRequired["aws_sdk_swf.types.tag_list.TagList"]
    """<p>The list of tags to associate with the new workflow execution. A maximum of 5 tags can be specified. You can list workflow executions with a specific tag by calling <a>ListOpenWorkflowExecutions</a> or <a>ListClosedWorkflowExecutions</a> and specifying a <a>TagFilter</a>.</p>"""
    workflow_type_version: NotRequired["aws_sdk_swf.types.version.Version"]
    """<p>The version of the workflow to start.</p>"""
    lambda_role: NotRequired["aws_sdk_swf.types.arn.Arn"]
    """<p>The IAM role to attach to the new (continued) execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ContinueAsNewWorkflowExecutionDecisionAttributes,
) -> dict:
    out: dict = {}
    if "input" in value:
        out["input"] = value["input"]
    if "execution_start_to_close_timeout" in value:
        out["executionStartToCloseTimeout"] = value["execution_start_to_close_timeout"]
    if "task_list" in value:
        import aws_sdk_swf.types.task_list

        out["taskList"] = aws_sdk_swf.types.task_list.serialize_aws_json_1_0(
            value["task_list"]
        )
    if "task_priority" in value:
        out["taskPriority"] = value["task_priority"]
    if "task_start_to_close_timeout" in value:
        out["taskStartToCloseTimeout"] = value["task_start_to_close_timeout"]
    if "child_policy" in value:
        import aws_sdk_swf.types.child_policy

        out["childPolicy"] = aws_sdk_swf.types.child_policy.serialize_aws_json_1_0(
            value["child_policy"]
        )
    if "tag_list" in value:
        import aws_sdk_swf.types.tag_list

        out["tagList"] = aws_sdk_swf.types.tag_list.serialize_aws_json_1_0(
            value["tag_list"]
        )
    if "workflow_type_version" in value:
        out["workflowTypeVersion"] = value["workflow_type_version"]
    if "lambda_role" in value:
        out["lambdaRole"] = value["lambda_role"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ContinueAsNewWorkflowExecutionDecisionAttributes:
    out: ContinueAsNewWorkflowExecutionDecisionAttributes = {}  # type: ignore[typeddict-item]
    if "input" in data:
        out["input"] = data["input"]
    if "executionStartToCloseTimeout" in data:
        out["execution_start_to_close_timeout"] = data["executionStartToCloseTimeout"]
    if "taskList" in data:
        import aws_sdk_swf.types.task_list

        out["task_list"] = aws_sdk_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    if "taskPriority" in data:
        out["task_priority"] = data["taskPriority"]
    if "taskStartToCloseTimeout" in data:
        out["task_start_to_close_timeout"] = data["taskStartToCloseTimeout"]
    if "childPolicy" in data:
        import aws_sdk_swf.types.child_policy

        out["child_policy"] = aws_sdk_swf.types.child_policy.deserialize_aws_json_1_0(
            data["childPolicy"]
        )
    if "tagList" in data:
        import aws_sdk_swf.types.tag_list

        out["tag_list"] = aws_sdk_swf.types.tag_list.deserialize_aws_json_1_0(
            data["tagList"]
        )
    if "workflowTypeVersion" in data:
        out["workflow_type_version"] = data["workflowTypeVersion"]
    if "lambdaRole" in data:
        out["lambda_role"] = data["lambdaRole"]
    return out
