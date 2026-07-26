"""Generated from Smithy shape ``com.amazonaws.sagemaker#CategoricalParameterRangeValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.string128

CategoricalParameterRangeValues: TypeAlias = list[
    "capo_sagemaker.types.string128.String128"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameterRangeValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CategoricalParameterRangeValues:
    return list(data)
