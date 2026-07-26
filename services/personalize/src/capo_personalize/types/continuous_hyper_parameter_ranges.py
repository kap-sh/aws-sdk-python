"""Generated from Smithy shape ``com.amazonaws.personalize#ContinuousHyperParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.continuous_hyper_parameter_range

ContinuousHyperParameterRanges: TypeAlias = list[
    "capo_personalize.types.continuous_hyper_parameter_range.ContinuousHyperParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousHyperParameterRanges) -> list:
    import capo_personalize.types.continuous_hyper_parameter_range

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.continuous_hyper_parameter_range.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContinuousHyperParameterRanges:
    import capo_personalize.types.continuous_hyper_parameter_range

    out: ContinuousHyperParameterRanges = []
    for item in data:
        out.append(
            capo_personalize.types.continuous_hyper_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
