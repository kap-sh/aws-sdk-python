"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetCodeReviewJobTasksInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.task_id_list


class BatchGetCodeReviewJobTasksInput(TypedDict):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the tasks.</p>"""
    code_review_job_task_ids: "aws_sdk_securityagent.types.task_id_list.TaskIdList"
    """<p>The list of task identifiers to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCodeReviewJobTasksInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import aws_sdk_securityagent.types.task_id_list

    out["codeReviewJobTaskIds"] = (
        aws_sdk_securityagent.types.task_id_list.serialize_json(
            value["code_review_job_task_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetCodeReviewJobTasksInput:
    out: BatchGetCodeReviewJobTasksInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError(
            "BatchGetCodeReviewJobTasksInput.agent_space_id required"
        )
    if "codeReviewJobTaskIds" in data:
        import aws_sdk_securityagent.types.task_id_list

        out["code_review_job_task_ids"] = (
            aws_sdk_securityagent.types.task_id_list.deserialize_json(
                data["codeReviewJobTaskIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetCodeReviewJobTasksInput.code_review_job_task_ids required"
        )
    return out
