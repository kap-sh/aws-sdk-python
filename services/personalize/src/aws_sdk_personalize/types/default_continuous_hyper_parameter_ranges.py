"""Generated from Smithy shape ``com.amazonaws.personalize#DefaultContinuousHyperParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.default_continuous_hyper_parameter_range

DefaultContinuousHyperParameterRanges: TypeAlias = list[
    "aws_sdk_personalize.types.default_continuous_hyper_parameter_range.DefaultContinuousHyperParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultContinuousHyperParameterRanges) -> list:
    import aws_sdk_personalize.types.default_continuous_hyper_parameter_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.default_continuous_hyper_parameter_range.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DefaultContinuousHyperParameterRanges:
    import aws_sdk_personalize.types.default_continuous_hyper_parameter_range

    out: DefaultContinuousHyperParameterRanges = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.default_continuous_hyper_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
