"""Generated from Smithy shape ``com.amazonaws.sagemaker#CategoricalParameterRangeSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.parameter_values


class CategoricalParameterRangeSpecification(TypedDict, closed=True):
    values: NotRequired["capo_sagemaker.types.parameter_values.ParameterValues"]
    """<p>The allowed categories for the hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameterRangeSpecification) -> dict:
    out: dict = {}
    if "values" in value:
        import capo_sagemaker.types.parameter_values

        out["Values"] = capo_sagemaker.types.parameter_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CategoricalParameterRangeSpecification:
    out: CategoricalParameterRangeSpecification = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import capo_sagemaker.types.parameter_values

        out["values"] = capo_sagemaker.types.parameter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    return out
