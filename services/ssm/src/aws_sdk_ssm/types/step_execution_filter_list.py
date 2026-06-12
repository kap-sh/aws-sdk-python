"""Generated from Smithy shape ``com.amazonaws.ssm#StepExecutionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.step_execution_filter

StepExecutionFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.step_execution_filter.StepExecutionFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepExecutionFilterList) -> list:
    import aws_sdk_ssm.types.step_execution_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.step_execution_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StepExecutionFilterList:
    import aws_sdk_ssm.types.step_execution_filter

    out: StepExecutionFilterList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.step_execution_filter.deserialize_aws_json_1_1(item)
        )
    return out
