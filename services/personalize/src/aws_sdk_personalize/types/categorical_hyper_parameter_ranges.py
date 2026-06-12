"""Generated from Smithy shape ``com.amazonaws.personalize#CategoricalHyperParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.categorical_hyper_parameter_range

CategoricalHyperParameterRanges: TypeAlias = list[
    "aws_sdk_personalize.types.categorical_hyper_parameter_range.CategoricalHyperParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalHyperParameterRanges) -> list:
    import aws_sdk_personalize.types.categorical_hyper_parameter_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.categorical_hyper_parameter_range.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CategoricalHyperParameterRanges:
    import aws_sdk_personalize.types.categorical_hyper_parameter_range

    out: CategoricalHyperParameterRanges = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.categorical_hyper_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
