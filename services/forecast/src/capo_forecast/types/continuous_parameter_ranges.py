"""Generated from Smithy shape ``com.amazonaws.forecast#ContinuousParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.continuous_parameter_range

ContinuousParameterRanges: TypeAlias = list[
    "capo_forecast.types.continuous_parameter_range.ContinuousParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousParameterRanges) -> list:
    import capo_forecast.types.continuous_parameter_range

    out: list = []
    for item in value:
        out.append(
            capo_forecast.types.continuous_parameter_range.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContinuousParameterRanges:
    import capo_forecast.types.continuous_parameter_range

    out: ContinuousParameterRanges = []
    for item in data:
        out.append(
            capo_forecast.types.continuous_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
