"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.stage_execution

StageExecutionList: TypeAlias = list[
    "aws_sdk_codepipeline.types.stage_execution.StageExecution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageExecutionList) -> list:
    import aws_sdk_codepipeline.types.stage_execution

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.stage_execution.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StageExecutionList:
    import aws_sdk_codepipeline.types.stage_execution

    out: StageExecutionList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.stage_execution.deserialize_aws_json_1_1(item)
        )
    return out
