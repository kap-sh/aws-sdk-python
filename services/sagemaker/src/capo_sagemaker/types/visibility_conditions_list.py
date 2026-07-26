"""Generated from Smithy shape ``com.amazonaws.sagemaker#VisibilityConditionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.visibility_conditions

VisibilityConditionsList: TypeAlias = list[
    "capo_sagemaker.types.visibility_conditions.VisibilityConditions"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VisibilityConditionsList) -> list:
    import capo_sagemaker.types.visibility_conditions

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.visibility_conditions.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VisibilityConditionsList:
    import capo_sagemaker.types.visibility_conditions

    out: VisibilityConditionsList = []
    for item in data:
        out.append(
            capo_sagemaker.types.visibility_conditions.deserialize_aws_json_1_1(item)
        )
    return out
