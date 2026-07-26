"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.timestamp
    import capo_swf.types.workflow_execution_configuration
    import capo_swf.types.workflow_execution_info
    import capo_swf.types.workflow_execution_open_counts


class WorkflowExecutionDetail(TypedDict, closed=True):
    execution_info: "capo_swf.types.workflow_execution_info.WorkflowExecutionInfo"
    """<p>Information about the workflow execution.</p>"""
    execution_configuration: (
        "capo_swf.types.workflow_execution_configuration.WorkflowExecutionConfiguration"
    )
    """<p>The configuration settings for this workflow execution including timeout values, tasklist etc.</p>"""
    open_counts: (
        "capo_swf.types.workflow_execution_open_counts.WorkflowExecutionOpenCounts"
    )
    """<p>The number of tasks for this workflow execution. This includes open and closed tasks of all types.</p>"""
    latest_activity_task_timestamp: NotRequired["capo_swf.types.timestamp.Timestamp"]
    """<p>The time when the last activity task was scheduled for this workflow execution. You can use this information to determine if the workflow has not made progress for an unusually long period of time and might require a corrective action.</p>"""
    latest_execution_context: NotRequired["capo_swf.types.data.Data"]
    """<p>The latest executionContext provided by the decider for this workflow execution. A decider can provide an executionContext (a free-form string) when closing a decision task using <a>RespondDecisionTaskCompleted</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionDetail) -> dict:
    out: dict = {}
    import capo_swf.types.workflow_execution_info

    out["executionInfo"] = (
        capo_swf.types.workflow_execution_info.serialize_aws_json_1_0(
            value["execution_info"]
        )
    )
    import capo_swf.types.workflow_execution_configuration

    out["executionConfiguration"] = (
        capo_swf.types.workflow_execution_configuration.serialize_aws_json_1_0(
            value["execution_configuration"]
        )
    )
    import capo_swf.types.workflow_execution_open_counts

    out["openCounts"] = (
        capo_swf.types.workflow_execution_open_counts.serialize_aws_json_1_0(
            value["open_counts"]
        )
    )
    if "latest_activity_task_timestamp" in value:
        import capo_swf.types.timestamp

        out["latestActivityTaskTimestamp"] = (
            capo_swf.types.timestamp.serialize_aws_json_1_0(
                value["latest_activity_task_timestamp"]
            )
        )
    if "latest_execution_context" in value:
        out["latestExecutionContext"] = value["latest_execution_context"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionDetail:
    out: WorkflowExecutionDetail = {}  # type: ignore[typeddict-item]
    if "executionInfo" in data:
        import capo_swf.types.workflow_execution_info

        out["execution_info"] = (
            capo_swf.types.workflow_execution_info.deserialize_aws_json_1_0(
                data["executionInfo"]
            )
        )
    else:
        raise DeserializationError("WorkflowExecutionDetail.execution_info required")
    if "executionConfiguration" in data:
        import capo_swf.types.workflow_execution_configuration

        out["execution_configuration"] = (
            capo_swf.types.workflow_execution_configuration.deserialize_aws_json_1_0(
                data["executionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "WorkflowExecutionDetail.execution_configuration required"
        )
    if "openCounts" in data:
        import capo_swf.types.workflow_execution_open_counts

        out["open_counts"] = (
            capo_swf.types.workflow_execution_open_counts.deserialize_aws_json_1_0(
                data["openCounts"]
            )
        )
    else:
        raise DeserializationError("WorkflowExecutionDetail.open_counts required")
    if "latestActivityTaskTimestamp" in data:
        import capo_swf.types.timestamp

        out["latest_activity_task_timestamp"] = (
            capo_swf.types.timestamp.deserialize_aws_json_1_0(
                data["latestActivityTaskTimestamp"]
            )
        )
    if "latestExecutionContext" in data:
        out["latest_execution_context"] = data["latestExecutionContext"]
    return out
