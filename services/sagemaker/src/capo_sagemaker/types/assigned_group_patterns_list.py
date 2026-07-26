"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssignedGroupPatternsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.group_name_pattern

AssignedGroupPatternsList: TypeAlias = list[
    "capo_sagemaker.types.group_name_pattern.GroupNamePattern"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssignedGroupPatternsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AssignedGroupPatternsList:
    return list(data)
