"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetWorkflowExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.date_time
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.parallel_group
    import aws_sdk_imagebuilder.types.workflow_build_version_arn
    import aws_sdk_imagebuilder.types.workflow_execution_id
    import aws_sdk_imagebuilder.types.workflow_execution_message
    import aws_sdk_imagebuilder.types.workflow_execution_status
    import aws_sdk_imagebuilder.types.workflow_step_count
    import aws_sdk_imagebuilder.types.workflow_type


class GetWorkflowExecutionResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    workflow_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the build version for the Image Builder workflow resource that defines the specified runtime instance of the workflow.</p>"""
    workflow_execution_id: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_execution_id.WorkflowExecutionId"
    ]
    """<p>The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.</p>"""
    image_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image resource build version that the specified runtime instance of the workflow created.</p>"""
    type: NotRequired["aws_sdk_imagebuilder.types.workflow_type.WorkflowType"]
    """<p>The type of workflow that Image Builder ran for the specified runtime instance of the workflow.</p>"""
    status: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_execution_status.WorkflowExecutionStatus"
    ]
    """<p>The current runtime status for the specified runtime instance of the workflow.</p>"""
    message: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_execution_message.WorkflowExecutionMessage"
    ]
    """<p>The output message from the specified runtime instance of the workflow, if applicable.</p>"""
    total_step_count: "aws_sdk_imagebuilder.types.workflow_step_count.WorkflowStepCount"
    """<p>The total number of steps in the specified runtime instance of the workflow that ran. This number should equal the sum of the step counts for steps that succeeded, were skipped, and failed.</p>"""
    total_steps_succeeded: (
        "aws_sdk_imagebuilder.types.workflow_step_count.WorkflowStepCount"
    )
    """<p>A runtime count for the number of steps that ran successfully in the specified runtime instance of the workflow.</p>"""
    total_steps_failed: (
        "aws_sdk_imagebuilder.types.workflow_step_count.WorkflowStepCount"
    )
    """<p>A runtime count for the number of steps that failed in the specified runtime instance of the workflow.</p>"""
    total_steps_skipped: (
        "aws_sdk_imagebuilder.types.workflow_step_count.WorkflowStepCount"
    )
    """<p>A runtime count for the number of steps that were skipped in the specified runtime instance of the workflow.</p>"""
    start_time: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when the specified runtime instance of the workflow started.</p>"""
    end_time: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when the specified runtime instance of the workflow finished.</p>"""
    parallel_group: NotRequired[
        "aws_sdk_imagebuilder.types.parallel_group.ParallelGroup"
    ]
    """<p>Test workflows are defined within named runtime groups. The parallel group is a named group that contains one or more test workflows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowExecutionResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "workflow_build_version_arn" in value:
        out["workflowBuildVersionArn"] = value["workflow_build_version_arn"]
    if "workflow_execution_id" in value:
        out["workflowExecutionId"] = value["workflow_execution_id"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "type" in value:
        import aws_sdk_imagebuilder.types.workflow_type

        out["type"] = aws_sdk_imagebuilder.types.workflow_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import aws_sdk_imagebuilder.types.workflow_execution_status

        out["status"] = (
            aws_sdk_imagebuilder.types.workflow_execution_status.serialize_json(
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
    return out


def deserialize_json(data: dict) -> GetWorkflowExecutionResponse:
    out: GetWorkflowExecutionResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "workflowBuildVersionArn" in data:
        out["workflow_build_version_arn"] = data["workflowBuildVersionArn"]
    if "workflowExecutionId" in data:
        out["workflow_execution_id"] = data["workflowExecutionId"]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    if "type" in data:
        import aws_sdk_imagebuilder.types.workflow_type

        out["type"] = aws_sdk_imagebuilder.types.workflow_type.deserialize_json(
            data["type"]
        )
    if "status" in data:
        import aws_sdk_imagebuilder.types.workflow_execution_status

        out["status"] = (
            aws_sdk_imagebuilder.types.workflow_execution_status.deserialize_json(
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
    return out
