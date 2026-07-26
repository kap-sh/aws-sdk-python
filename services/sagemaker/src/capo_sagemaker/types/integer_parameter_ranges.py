"""Generated from Smithy shape ``com.amazonaws.sagemaker#IntegerParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.integer_parameter_range

IntegerParameterRanges: TypeAlias = list[
    "capo_sagemaker.types.integer_parameter_range.IntegerParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegerParameterRanges) -> list:
    import capo_sagemaker.types.integer_parameter_range

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.integer_parameter_range.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IntegerParameterRanges:
    import capo_sagemaker.types.integer_parameter_range

    out: IntegerParameterRanges = []
    for item in data:
        out.append(
            capo_sagemaker.types.integer_parameter_range.deserialize_aws_json_1_1(item)
        )
    return out
