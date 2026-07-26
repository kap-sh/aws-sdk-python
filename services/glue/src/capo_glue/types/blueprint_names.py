"""Generated from Smithy shape ``com.amazonaws.glue#BlueprintNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.orchestration_name_string

BlueprintNames: TypeAlias = list[
    "capo_glue.types.orchestration_name_string.OrchestrationNameString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BlueprintNames:
    return list(data)
