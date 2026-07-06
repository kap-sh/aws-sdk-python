"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetCodeReviewJobTasksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.code_review_job_task_list
    import aws_sdk_securityagent.types.task_id_list


class BatchGetCodeReviewJobTasksOutput(TypedDict, closed=True):
    code_review_job_tasks: NotRequired[
        "aws_sdk_securityagent.types.code_review_job_task_list.CodeReviewJobTaskList"
    ]
    """<p>The list of code review job tasks that were found.</p>"""
    not_found: NotRequired["aws_sdk_securityagent.types.task_id_list.TaskIdList"]
    """<p>The list of task identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCodeReviewJobTasksOutput) -> dict:
    out: dict = {}
    if "code_review_job_tasks" in value:
        import aws_sdk_securityagent.types.code_review_job_task_list

        out["codeReviewJobTasks"] = (
            aws_sdk_securityagent.types.code_review_job_task_list.serialize_json(
                value["code_review_job_tasks"]
            )
        )
    if "not_found" in value:
        import aws_sdk_securityagent.types.task_id_list

        out["notFound"] = aws_sdk_securityagent.types.task_id_list.serialize_json(
            value["not_found"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetCodeReviewJobTasksOutput:
    out: BatchGetCodeReviewJobTasksOutput = {}  # type: ignore[typeddict-item]
    if "codeReviewJobTasks" in data:
        import aws_sdk_securityagent.types.code_review_job_task_list

        out["code_review_job_tasks"] = (
            aws_sdk_securityagent.types.code_review_job_task_list.deserialize_json(
                data["codeReviewJobTasks"]
            )
        )
    if "notFound" in data:
        import aws_sdk_securityagent.types.task_id_list

        out["not_found"] = aws_sdk_securityagent.types.task_id_list.deserialize_json(
            data["notFound"]
        )
    return out
