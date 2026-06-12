"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetBlueprintNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.orchestration_name_string

BatchGetBlueprintNames: TypeAlias = list[
    "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetBlueprintNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BatchGetBlueprintNames:
    return list(data)
