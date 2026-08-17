"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.automation_parameter_value

AutomationParameterValueList: TypeAlias = list[
    "capo_ssm.types.automation_parameter_value.AutomationParameterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationParameterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AutomationParameterValueList:
    return [item for item in data if item is not None]
