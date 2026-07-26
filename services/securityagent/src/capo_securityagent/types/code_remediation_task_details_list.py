"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeRemediationTaskDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.code_remediation_task_details

CodeRemediationTaskDetailsList: TypeAlias = list[
    "capo_securityagent.types.code_remediation_task_details.CodeRemediationTaskDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeRemediationTaskDetailsList) -> list:
    import capo_securityagent.types.code_remediation_task_details

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.code_remediation_task_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CodeRemediationTaskDetailsList:
    import capo_securityagent.types.code_remediation_task_details

    out: CodeRemediationTaskDetailsList = []
    for item in data:
        out.append(
            capo_securityagent.types.code_remediation_task_details.deserialize_json(
                item
            )
        )
    return out
