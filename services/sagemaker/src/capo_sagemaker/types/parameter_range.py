"""Generated from Smithy shape ``com.amazonaws.sagemaker#ParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.categorical_parameter_range_specification
    import capo_sagemaker.types.continuous_parameter_range_specification
    import capo_sagemaker.types.integer_parameter_range_specification


class ParameterRange(TypedDict, closed=True):
    integer_parameter_range_specification: NotRequired[
        "capo_sagemaker.types.integer_parameter_range_specification.IntegerParameterRangeSpecification"
    ]
    """<p>A <code>IntegerParameterRangeSpecification</code> object that defines the possible values for an integer hyperparameter.</p>"""
    continuous_parameter_range_specification: NotRequired[
        "capo_sagemaker.types.continuous_parameter_range_specification.ContinuousParameterRangeSpecification"
    ]
    """<p>A <code>ContinuousParameterRangeSpecification</code> object that defines the possible values for a continuous hyperparameter.</p>"""
    categorical_parameter_range_specification: NotRequired[
        "capo_sagemaker.types.categorical_parameter_range_specification.CategoricalParameterRangeSpecification"
    ]
    """<p>A <code>CategoricalParameterRangeSpecification</code> object that defines the possible values for a categorical hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterRange) -> dict:
    out: dict = {}
    if "integer_parameter_range_specification" in value:
        import capo_sagemaker.types.integer_parameter_range_specification

        out["IntegerParameterRangeSpecification"] = (
            capo_sagemaker.types.integer_parameter_range_specification.serialize_aws_json_1_1(
                value["integer_parameter_range_specification"]
            )
        )
    if "continuous_parameter_range_specification" in value:
        import capo_sagemaker.types.continuous_parameter_range_specification

        out["ContinuousParameterRangeSpecification"] = (
            capo_sagemaker.types.continuous_parameter_range_specification.serialize_aws_json_1_1(
                value["continuous_parameter_range_specification"]
            )
        )
    if "categorical_parameter_range_specification" in value:
        import capo_sagemaker.types.categorical_parameter_range_specification

        out["CategoricalParameterRangeSpecification"] = (
            capo_sagemaker.types.categorical_parameter_range_specification.serialize_aws_json_1_1(
                value["categorical_parameter_range_specification"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterRange:
    out: ParameterRange = {}  # type: ignore[typeddict-item]
    if "IntegerParameterRangeSpecification" in data:
        import capo_sagemaker.types.integer_parameter_range_specification

        out["integer_parameter_range_specification"] = (
            capo_sagemaker.types.integer_parameter_range_specification.deserialize_aws_json_1_1(
                data["IntegerParameterRangeSpecification"]
            )
        )
    if "ContinuousParameterRangeSpecification" in data:
        import capo_sagemaker.types.continuous_parameter_range_specification

        out["continuous_parameter_range_specification"] = (
            capo_sagemaker.types.continuous_parameter_range_specification.deserialize_aws_json_1_1(
                data["ContinuousParameterRangeSpecification"]
            )
        )
    if "CategoricalParameterRangeSpecification" in data:
        import capo_sagemaker.types.categorical_parameter_range_specification

        out["categorical_parameter_range_specification"] = (
            capo_sagemaker.types.categorical_parameter_range_specification.deserialize_aws_json_1_1(
                data["CategoricalParameterRangeSpecification"]
            )
        )
    return out
