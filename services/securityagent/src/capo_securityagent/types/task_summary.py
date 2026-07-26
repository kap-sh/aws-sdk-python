"""Generated from Smithy shape ``com.amazonaws.securityagent#TaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.risk_type
    import capo_securityagent.types.task_execution_status


class TaskSummary(TypedDict, closed=True):
    task_id: "str"
    """<p>The unique identifier of the task.</p>"""
    pentest_id: NotRequired["str"]
    """<p>The unique identifier of the pentest associated with the task.</p>"""
    pentest_job_id: NotRequired["str"]
    """<p>The unique identifier of the pentest job that contains the task.</p>"""
    agent_space_id: NotRequired["str"]
    """<p>The unique identifier of the agent space.</p>"""
    title: NotRequired["str"]
    """<p>The title of the task.</p>"""
    risk_type: NotRequired["capo_securityagent.types.risk_type.RiskType"]
    """<p>The type of security risk the task is testing for.</p>"""
    execution_status: NotRequired[
        "capo_securityagent.types.task_execution_status.TaskExecutionStatus"
    ]
    """<p>The current execution status of the task.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the task was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the task was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskSummary) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    if "pentest_id" in value:
        out["pentestId"] = value["pentest_id"]
    if "pentest_job_id" in value:
        out["pentestJobId"] = value["pentest_job_id"]
    if "agent_space_id" in value:
        out["agentSpaceId"] = value["agent_space_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "risk_type" in value:
        import capo_securityagent.types.risk_type

        out["riskType"] = capo_securityagent.types.risk_type.serialize_json(
            value["risk_type"]
        )
    if "execution_status" in value:
        import capo_securityagent.types.task_execution_status

        out["executionStatus"] = (
            capo_securityagent.types.task_execution_status.serialize_json(
                value["execution_status"]
            )
        )
    if "created_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["createdAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["updatedAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> TaskSummary:
    out: TaskSummary = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("TaskSummary.task_id required")
    if "pentestId" in data:
        out["pentest_id"] = data["pentestId"]
    if "pentestJobId" in data:
        out["pentest_job_id"] = data["pentestJobId"]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    if "title" in data:
        out["title"] = data["title"]
    if "riskType" in data:
        import capo_securityagent.types.risk_type

        out["risk_type"] = capo_securityagent.types.risk_type.deserialize_json(
            data["riskType"]
        )
    if "executionStatus" in data:
        import capo_securityagent.types.task_execution_status

        out["execution_status"] = (
            capo_securityagent.types.task_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    if "createdAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["created_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
