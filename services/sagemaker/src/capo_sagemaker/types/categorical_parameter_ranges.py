"""Generated from Smithy shape ``com.amazonaws.sagemaker#CategoricalParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.categorical_parameter_range

CategoricalParameterRanges: TypeAlias = list[
    "capo_sagemaker.types.categorical_parameter_range.CategoricalParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameterRanges) -> list:
    import capo_sagemaker.types.categorical_parameter_range

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.categorical_parameter_range.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CategoricalParameterRanges:
    import capo_sagemaker.types.categorical_parameter_range

    out: CategoricalParameterRanges = []
    for item in data:
        out.append(
            capo_sagemaker.types.categorical_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
