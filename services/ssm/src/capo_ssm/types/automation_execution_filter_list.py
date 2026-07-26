"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_filter

AutomationExecutionFilterList: TypeAlias = list[
    "capo_ssm.types.automation_execution_filter.AutomationExecutionFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionFilterList) -> list:
    import capo_ssm.types.automation_execution_filter

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.automation_execution_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutomationExecutionFilterList:
    import capo_ssm.types.automation_execution_filter

    out: AutomationExecutionFilterList = []
    for item in data:
        out.append(
            capo_ssm.types.automation_execution_filter.deserialize_aws_json_1_1(item)
        )
    return out
