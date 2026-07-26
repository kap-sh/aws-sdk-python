"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionExecutionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.action_execution_detail

ActionExecutionDetailList: TypeAlias = list[
    "capo_codepipeline.types.action_execution_detail.ActionExecutionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionExecutionDetailList) -> list:
    import capo_codepipeline.types.action_execution_detail

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.action_execution_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ActionExecutionDetailList:
    import capo_codepipeline.types.action_execution_detail

    out: ActionExecutionDetailList = []
    for item in data:
        out.append(
            capo_codepipeline.types.action_execution_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
