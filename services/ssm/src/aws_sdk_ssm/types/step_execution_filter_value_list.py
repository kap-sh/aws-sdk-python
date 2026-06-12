"""Generated from Smithy shape ``com.amazonaws.ssm#StepExecutionFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.step_execution_filter_value

StepExecutionFilterValueList: TypeAlias = list[
    "aws_sdk_ssm.types.step_execution_filter_value.StepExecutionFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepExecutionFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StepExecutionFilterValueList:
    return list(data)
