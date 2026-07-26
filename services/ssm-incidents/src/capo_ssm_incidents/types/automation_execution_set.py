"""Generated from Smithy shape ``com.amazonaws.ssmincidents#AutomationExecutionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.automation_execution

AutomationExecutionSet: TypeAlias = list[
    "capo_ssm_incidents.types.automation_execution.AutomationExecution"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationExecutionSet) -> list:
    import capo_ssm_incidents.types.automation_execution

    out: list = []
    for item in value:
        out.append(capo_ssm_incidents.types.automation_execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> AutomationExecutionSet:
    import capo_ssm_incidents.types.automation_execution

    out: AutomationExecutionSet = []
    for item in data:
        out.append(capo_ssm_incidents.types.automation_execution.deserialize_json(item))
    return out
