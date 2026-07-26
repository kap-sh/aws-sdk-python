"""Generated from Smithy shape ``com.amazonaws.personalize#CategoricalHyperParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.categorical_hyper_parameter_range

CategoricalHyperParameterRanges: TypeAlias = list[
    "capo_personalize.types.categorical_hyper_parameter_range.CategoricalHyperParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalHyperParameterRanges) -> list:
    import capo_personalize.types.categorical_hyper_parameter_range

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.categorical_hyper_parameter_range.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CategoricalHyperParameterRanges:
    import capo_personalize.types.categorical_hyper_parameter_range

    out: CategoricalHyperParameterRanges = []
    for item in data:
        out.append(
            capo_personalize.types.categorical_hyper_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
