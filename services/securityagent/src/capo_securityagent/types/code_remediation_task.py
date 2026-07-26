"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeRemediationTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.code_remediation_task_details_list
    import capo_securityagent.types.code_remediation_task_status


class CodeRemediationTask(TypedDict, closed=True):
    status: "capo_securityagent.types.code_remediation_task_status.CodeRemediationTaskStatus"
    """<p>The current status of the code remediation task.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the code remediation task.</p>"""
    task_details: NotRequired[
        "capo_securityagent.types.code_remediation_task_details_list.CodeRemediationTaskDetailsList"
    ]
    """<p>The list of details for the code remediation task, including repository name, code diff link, and pull request link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeRemediationTask) -> dict:
    out: dict = {}
    import capo_securityagent.types.code_remediation_task_status

    out["status"] = (
        capo_securityagent.types.code_remediation_task_status.serialize_json(
            value["status"]
        )
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "task_details" in value:
        import capo_securityagent.types.code_remediation_task_details_list

        out["taskDetails"] = (
            capo_securityagent.types.code_remediation_task_details_list.serialize_json(
                value["task_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodeRemediationTask:
    out: CodeRemediationTask = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_securityagent.types.code_remediation_task_status

        out["status"] = (
            capo_securityagent.types.code_remediation_task_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CodeRemediationTask.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "taskDetails" in data:
        import capo_securityagent.types.code_remediation_task_details_list

        out["task_details"] = (
            capo_securityagent.types.code_remediation_task_details_list.deserialize_json(
                data["taskDetails"]
            )
        )
    return out
