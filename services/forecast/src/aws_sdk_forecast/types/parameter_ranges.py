"""Generated from Smithy shape ``com.amazonaws.forecast#ParameterRanges``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.categorical_parameter_ranges
    import aws_sdk_forecast.types.continuous_parameter_ranges
    import aws_sdk_forecast.types.integer_parameter_ranges


class ParameterRanges(TypedDict):
    categorical_parameter_ranges: NotRequired[
        "aws_sdk_forecast.types.categorical_parameter_ranges.CategoricalParameterRanges"
    ]
    """<p>Specifies the tunable range for each categorical hyperparameter.</p>"""
    continuous_parameter_ranges: NotRequired[
        "aws_sdk_forecast.types.continuous_parameter_ranges.ContinuousParameterRanges"
    ]
    """<p>Specifies the tunable range for each continuous hyperparameter.</p>"""
    integer_parameter_ranges: NotRequired[
        "aws_sdk_forecast.types.integer_parameter_ranges.IntegerParameterRanges"
    ]
    """<p>Specifies the tunable range for each integer hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterRanges) -> dict:
    out: dict = {}
    if "categorical_parameter_ranges" in value:
        import aws_sdk_forecast.types.categorical_parameter_ranges

        out["CategoricalParameterRanges"] = (
            aws_sdk_forecast.types.categorical_parameter_ranges.serialize_aws_json_1_1(
                value["categorical_parameter_ranges"]
            )
        )
    if "continuous_parameter_ranges" in value:
        import aws_sdk_forecast.types.continuous_parameter_ranges

        out["ContinuousParameterRanges"] = (
            aws_sdk_forecast.types.continuous_parameter_ranges.serialize_aws_json_1_1(
                value["continuous_parameter_ranges"]
            )
        )
    if "integer_parameter_ranges" in value:
        import aws_sdk_forecast.types.integer_parameter_ranges

        out["IntegerParameterRanges"] = (
            aws_sdk_forecast.types.integer_parameter_ranges.serialize_aws_json_1_1(
                value["integer_parameter_ranges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterRanges:
    out: ParameterRanges = {}  # type: ignore[typeddict-item]
    if "CategoricalParameterRanges" in data:
        import aws_sdk_forecast.types.categorical_parameter_ranges

        out["categorical_parameter_ranges"] = (
            aws_sdk_forecast.types.categorical_parameter_ranges.deserialize_aws_json_1_1(
                data["CategoricalParameterRanges"]
            )
        )
    if "ContinuousParameterRanges" in data:
        import aws_sdk_forecast.types.continuous_parameter_ranges

        out["continuous_parameter_ranges"] = (
            aws_sdk_forecast.types.continuous_parameter_ranges.deserialize_aws_json_1_1(
                data["ContinuousParameterRanges"]
            )
        )
    if "IntegerParameterRanges" in data:
        import aws_sdk_forecast.types.integer_parameter_ranges

        out["integer_parameter_ranges"] = (
            aws_sdk_forecast.types.integer_parameter_ranges.deserialize_aws_json_1_1(
                data["IntegerParameterRanges"]
            )
        )
    return out
