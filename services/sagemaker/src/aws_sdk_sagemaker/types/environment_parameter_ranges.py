"""Generated from Smithy shape ``com.amazonaws.sagemaker#EnvironmentParameterRanges``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.categorical_parameters


class EnvironmentParameterRanges(TypedDict):
    categorical_parameter_ranges: NotRequired[
        "aws_sdk_sagemaker.types.categorical_parameters.CategoricalParameters"
    ]
    """<p>Specified a list of parameters for each category.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentParameterRanges) -> dict:
    out: dict = {}
    if "categorical_parameter_ranges" in value:
        import aws_sdk_sagemaker.types.categorical_parameters

        out["CategoricalParameterRanges"] = (
            aws_sdk_sagemaker.types.categorical_parameters.serialize_aws_json_1_1(
                value["categorical_parameter_ranges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentParameterRanges:
    out: EnvironmentParameterRanges = {}  # type: ignore[typeddict-item]
    if "CategoricalParameterRanges" in data:
        import aws_sdk_sagemaker.types.categorical_parameters

        out["categorical_parameter_ranges"] = (
            aws_sdk_sagemaker.types.categorical_parameters.deserialize_aws_json_1_1(
                data["CategoricalParameterRanges"]
            )
        )
    return out
