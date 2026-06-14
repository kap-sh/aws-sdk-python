"""Generated from Smithy shape ``com.amazonaws.sagemaker#ParameterRanges``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_parameters
    import aws_sdk_sagemaker.types.categorical_parameter_ranges
    import aws_sdk_sagemaker.types.continuous_parameter_ranges
    import aws_sdk_sagemaker.types.integer_parameter_ranges


class ParameterRanges(TypedDict):
    integer_parameter_ranges: NotRequired[
        "aws_sdk_sagemaker.types.integer_parameter_ranges.IntegerParameterRanges"
    ]
    r"""<p>The array of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html\">IntegerParameterRange</a> objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.</p>"""
    continuous_parameter_ranges: NotRequired[
        "aws_sdk_sagemaker.types.continuous_parameter_ranges.ContinuousParameterRanges"
    ]
    r"""<p>The array of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContinuousParameterRange.html\">ContinuousParameterRange</a> objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.</p>"""
    categorical_parameter_ranges: NotRequired[
        "aws_sdk_sagemaker.types.categorical_parameter_ranges.CategoricalParameterRanges"
    ]
    r"""<p>The array of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html\">CategoricalParameterRange</a> objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.</p>"""
    auto_parameters: NotRequired[
        "aws_sdk_sagemaker.types.auto_parameters.AutoParameters"
    ]
    """<p>A list containing hyperparameter names and example values to be used by Autotune to determine optimal ranges for your tuning job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterRanges) -> dict:
    out: dict = {}
    if "integer_parameter_ranges" in value:
        import aws_sdk_sagemaker.types.integer_parameter_ranges

        out["IntegerParameterRanges"] = (
            aws_sdk_sagemaker.types.integer_parameter_ranges.serialize_aws_json_1_1(
                value["integer_parameter_ranges"]
            )
        )
    if "continuous_parameter_ranges" in value:
        import aws_sdk_sagemaker.types.continuous_parameter_ranges

        out["ContinuousParameterRanges"] = (
            aws_sdk_sagemaker.types.continuous_parameter_ranges.serialize_aws_json_1_1(
                value["continuous_parameter_ranges"]
            )
        )
    if "categorical_parameter_ranges" in value:
        import aws_sdk_sagemaker.types.categorical_parameter_ranges

        out["CategoricalParameterRanges"] = (
            aws_sdk_sagemaker.types.categorical_parameter_ranges.serialize_aws_json_1_1(
                value["categorical_parameter_ranges"]
            )
        )
    if "auto_parameters" in value:
        import aws_sdk_sagemaker.types.auto_parameters

        out["AutoParameters"] = (
            aws_sdk_sagemaker.types.auto_parameters.serialize_aws_json_1_1(
                value["auto_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterRanges:
    out: ParameterRanges = {}  # type: ignore[typeddict-item]
    if "IntegerParameterRanges" in data:
        import aws_sdk_sagemaker.types.integer_parameter_ranges

        out["integer_parameter_ranges"] = (
            aws_sdk_sagemaker.types.integer_parameter_ranges.deserialize_aws_json_1_1(
                data["IntegerParameterRanges"]
            )
        )
    if "ContinuousParameterRanges" in data:
        import aws_sdk_sagemaker.types.continuous_parameter_ranges

        out["continuous_parameter_ranges"] = (
            aws_sdk_sagemaker.types.continuous_parameter_ranges.deserialize_aws_json_1_1(
                data["ContinuousParameterRanges"]
            )
        )
    if "CategoricalParameterRanges" in data:
        import aws_sdk_sagemaker.types.categorical_parameter_ranges

        out["categorical_parameter_ranges"] = (
            aws_sdk_sagemaker.types.categorical_parameter_ranges.deserialize_aws_json_1_1(
                data["CategoricalParameterRanges"]
            )
        )
    if "AutoParameters" in data:
        import aws_sdk_sagemaker.types.auto_parameters

        out["auto_parameters"] = (
            aws_sdk_sagemaker.types.auto_parameters.deserialize_aws_json_1_1(
                data["AutoParameters"]
            )
        )
    return out
