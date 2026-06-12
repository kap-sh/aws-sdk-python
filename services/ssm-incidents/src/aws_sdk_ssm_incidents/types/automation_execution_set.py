"""Generated from Smithy shape ``com.amazonaws.ssmincidents#AutomationExecutionSet``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.automation_execution

AutomationExecutionSet: TypeAlias = list["aws_sdk_ssm_incidents.types.automation_execution.AutomationExecution"]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationExecutionSet) -> list:
    import aws_sdk_ssm_incidents.types.automation_execution
    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_incidents.types.automation_execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> AutomationExecutionSet:
    import aws_sdk_ssm_incidents.types.automation_execution
    out: AutomationExecutionSet = []
    for item in data:
        out.append(aws_sdk_ssm_incidents.types.automation_execution.deserialize_json(item))
    return out