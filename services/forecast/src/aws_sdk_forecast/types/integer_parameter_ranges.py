"""Generated from Smithy shape ``com.amazonaws.forecast#IntegerParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.integer_parameter_range

IntegerParameterRanges: TypeAlias = list[
    "aws_sdk_forecast.types.integer_parameter_range.IntegerParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegerParameterRanges) -> list:
    import aws_sdk_forecast.types.integer_parameter_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.integer_parameter_range.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IntegerParameterRanges:
    import aws_sdk_forecast.types.integer_parameter_range

    out: IntegerParameterRanges = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.integer_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
