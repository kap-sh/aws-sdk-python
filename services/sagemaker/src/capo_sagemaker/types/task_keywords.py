"""Generated from Smithy shape ``com.amazonaws.sagemaker#TaskKeywords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.task_keyword

TaskKeywords: TypeAlias = list["capo_sagemaker.types.task_keyword.TaskKeyword"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskKeywords) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TaskKeywords:
    return list(data)
