"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_filter_value

AutomationExecutionFilterValueList: TypeAlias = list[
    "capo_ssm.types.automation_execution_filter_value.AutomationExecutionFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AutomationExecutionFilterValueList:
    return list(data)
