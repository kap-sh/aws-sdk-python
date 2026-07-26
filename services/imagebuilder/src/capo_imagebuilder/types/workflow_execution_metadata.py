"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowExecutionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.parallel_group
    import capo_imagebuilder.types.workflow_build_version_arn
    import capo_imagebuilder.types.workflow_execution_id
    import capo_imagebuilder.types.workflow_execution_message
    import capo_imagebuilder.types.workflow_execution_status
    import capo_imagebuilder.types.workflow_step_count
    import capo_imagebuilder.types.workflow_type


class WorkflowExecutionMetadata(TypedDict, closed=True):
    workflow_build_version_arn: NotRequired[
        "capo_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the workflow resource build version that ran.</p>"""
    workflow_execution_id: NotRequired[
        "capo_imagebuilder.types.workflow_execution_id.WorkflowExecutionId"
    ]
    """<p>Unique identifier that Image Builder assigns to keep track of runtime resources each time it runs a workflow.</p>"""
    type: NotRequired["capo_imagebuilder.types.workflow_type.WorkflowType"]
    """<p>Indicates what type of workflow that Image Builder ran for this runtime instance of the workflow.</p>"""
    status: NotRequired[
        "capo_imagebuilder.types.workflow_execution_status.WorkflowExecutionStatus"
    ]
    """<p>The current runtime status for this workflow.</p>"""
    message: NotRequired[
        "capo_imagebuilder.types.workflow_execution_message.WorkflowExecutionMessage"
    ]
    """<p>The runtime output message from the workflow, if applicable.</p>"""
    total_step_count: "capo_imagebuilder.types.workflow_step_count.WorkflowStepCount"
    """<p>The total number of steps in the workflow. This should equal the sum of the step counts for steps that succeeded, were skipped, and failed.</p>"""
    total_steps_succeeded: (
        "capo_imagebuilder.types.workflow_step_count.WorkflowStepCount"
    )
    """<p>A runtime count for the number of steps in the workflow that ran successfully.</p>"""
    total_steps_failed: "capo_imagebuilder.types.workflow_step_count.WorkflowStepCount"
    """<p>A runtime count for the number of steps in the workflow that failed.</p>"""
    total_steps_skipped: "capo_imagebuilder.types.workflow_step_count.WorkflowStepCount"
    """<p>A runtime count for the number of steps in the workflow that were skipped.</p>"""
    start_time: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when the runtime instance of this workflow started.</p>"""
    end_time: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when this runtime instance of the workflow finished.</p>"""
    parallel_group: NotRequired["capo_imagebuilder.types.parallel_group.ParallelGroup"]
    """<p>The name of the test group that included the test workflow resource at runtime.</p>"""
    retried: NotRequired["capo_imagebuilder.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates retry status for this runtime instance of the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowExecutionMetadata) -> dict:
    out: dict = {}
    if "workflow_build_version_arn" in value:
        out["workflowBuildVersionArn"] = value["workflow_build_version_arn"]
    if "workflow_execution_id" in value:
        out["workflowExecutionId"] = value["workflow_execution_id"]
    if "type" in value:
        import capo_imagebuilder.types.workflow_type

        out["type"] = capo_imagebuilder.types.workflow_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import capo_imagebuilder.types.workflow_execution_status

        out["status"] = (
            capo_imagebuilder.types.workflow_execution_status.serialize_json(
                value["status"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    out["totalStepCount"] = value.get("total_step_count", 0)
    out["totalStepsSucceeded"] = value.get("total_steps_succeeded", 0)
    out["totalStepsFailed"] = value.get("total_steps_failed", 0)
    out["totalStepsSkipped"] = value.get("total_steps_skipped", 0)
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "end_time" in value:
        out["endTime"] = value["end_time"]
    if "parallel_group" in value:
        out["parallelGroup"] = value["parallel_group"]
    if "retried" in value:
        out["retried"] = value["retried"]
    return out


def deserialize_json(data: dict) -> WorkflowExecutionMetadata:
    out: WorkflowExecutionMetadata = {}  # type: ignore[typeddict-item]
    if "workflowBuildVersionArn" in data:
        out["workflow_build_version_arn"] = data["workflowBuildVersionArn"]
    if "workflowExecutionId" in data:
        out["workflow_execution_id"] = data["workflowExecutionId"]
    if "type" in data:
        import capo_imagebuilder.types.workflow_type

        out["type"] = capo_imagebuilder.types.workflow_type.deserialize_json(
            data["type"]
        )
    if "status" in data:
        import capo_imagebuilder.types.workflow_execution_status

        out["status"] = (
            capo_imagebuilder.types.workflow_execution_status.deserialize_json(
                data["status"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    if "totalStepCount" in data:
        out["total_step_count"] = data["totalStepCount"]
    else:
        out["total_step_count"] = 0
    if "totalStepsSucceeded" in data:
        out["total_steps_succeeded"] = data["totalStepsSucceeded"]
    else:
        out["total_steps_succeeded"] = 0
    if "totalStepsFailed" in data:
        out["total_steps_failed"] = data["totalStepsFailed"]
    else:
        out["total_steps_failed"] = 0
    if "totalStepsSkipped" in data:
        out["total_steps_skipped"] = data["totalStepsSkipped"]
    else:
        out["total_steps_skipped"] = 0
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    if "endTime" in data:
        out["end_time"] = data["endTime"]
    if "parallelGroup" in data:
        out["parallel_group"] = data["parallelGroup"]
    if "retried" in data:
        out["retried"] = data["retried"]
    return out
