"""Generated from Smithy shape ``com.amazonaws.personalize#ContinuousHyperParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.continuous_hyper_parameter_range

ContinuousHyperParameterRanges: TypeAlias = list[
    "aws_sdk_personalize.types.continuous_hyper_parameter_range.ContinuousHyperParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousHyperParameterRanges) -> list:
    import aws_sdk_personalize.types.continuous_hyper_parameter_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.continuous_hyper_parameter_range.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContinuousHyperParameterRanges:
    import aws_sdk_personalize.types.continuous_hyper_parameter_range

    out: ContinuousHyperParameterRanges = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.continuous_hyper_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
