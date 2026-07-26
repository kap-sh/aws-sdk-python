"""Generated from Smithy shape ``com.amazonaws.ssm#StepExecutionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.step_execution_filter

StepExecutionFilterList: TypeAlias = list[
    "capo_ssm.types.step_execution_filter.StepExecutionFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepExecutionFilterList) -> list:
    import capo_ssm.types.step_execution_filter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.step_execution_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StepExecutionFilterList:
    import capo_ssm.types.step_execution_filter

    out: StepExecutionFilterList = []
    for item in data:
        out.append(capo_ssm.types.step_execution_filter.deserialize_aws_json_1_1(item))
    return out
