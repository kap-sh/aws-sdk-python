"""Generated from Smithy shape ``com.amazonaws.sagemaker#FlowDefinitionTaskKeywords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.flow_definition_task_keyword

FlowDefinitionTaskKeywords: TypeAlias = list[
    "capo_sagemaker.types.flow_definition_task_keyword.FlowDefinitionTaskKeyword"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowDefinitionTaskKeywords) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FlowDefinitionTaskKeywords:
    return list(data)
