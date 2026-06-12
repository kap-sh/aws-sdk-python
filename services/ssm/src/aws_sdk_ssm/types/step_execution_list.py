"""Generated from Smithy shape ``com.amazonaws.ssm#StepExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.step_execution

StepExecutionList: TypeAlias = list["aws_sdk_ssm.types.step_execution.StepExecution"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepExecutionList) -> list:
    import aws_sdk_ssm.types.step_execution

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.step_execution.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StepExecutionList:
    import aws_sdk_ssm.types.step_execution

    out: StepExecutionList = []
    for item in data:
        out.append(aws_sdk_ssm.types.step_execution.deserialize_aws_json_1_1(item))
    return out
