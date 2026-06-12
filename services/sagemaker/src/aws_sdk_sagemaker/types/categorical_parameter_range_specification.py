"""Generated from Smithy shape ``com.amazonaws.sagemaker#CategoricalParameterRangeSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.parameter_values


class CategoricalParameterRangeSpecification(TypedDict):
    values: NotRequired["aws_sdk_sagemaker.types.parameter_values.ParameterValues"]
    """<p>The allowed categories for the hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameterRangeSpecification) -> dict:
    out: dict = {}
    if "values" in value:
        import aws_sdk_sagemaker.types.parameter_values

        out["Values"] = aws_sdk_sagemaker.types.parameter_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CategoricalParameterRangeSpecification:
    out: CategoricalParameterRangeSpecification = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import aws_sdk_sagemaker.types.parameter_values

        out["values"] = (
            aws_sdk_sagemaker.types.parameter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
