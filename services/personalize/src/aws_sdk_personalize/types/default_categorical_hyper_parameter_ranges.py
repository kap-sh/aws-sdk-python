"""Generated from Smithy shape ``com.amazonaws.personalize#DefaultCategoricalHyperParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.default_categorical_hyper_parameter_range

DefaultCategoricalHyperParameterRanges: TypeAlias = list[
    "aws_sdk_personalize.types.default_categorical_hyper_parameter_range.DefaultCategoricalHyperParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultCategoricalHyperParameterRanges) -> list:
    import aws_sdk_personalize.types.default_categorical_hyper_parameter_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.default_categorical_hyper_parameter_range.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DefaultCategoricalHyperParameterRanges:
    import aws_sdk_personalize.types.default_categorical_hyper_parameter_range

    out: DefaultCategoricalHyperParameterRanges = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.default_categorical_hyper_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
