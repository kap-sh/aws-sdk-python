"""Generated from Smithy shape ``com.amazonaws.sagemaker#CategoricalParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.parameter_key
    import capo_sagemaker.types.parameter_values


class CategoricalParameterRange(TypedDict, closed=True):
    name: NotRequired["capo_sagemaker.types.parameter_key.ParameterKey"]
    """<p>The name of the categorical hyperparameter to tune.</p>"""
    values: NotRequired["capo_sagemaker.types.parameter_values.ParameterValues"]
    """<p>A list of the categories for the hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameterRange) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import capo_sagemaker.types.parameter_values

        out["Values"] = capo_sagemaker.types.parameter_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CategoricalParameterRange:
    out: CategoricalParameterRange = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import capo_sagemaker.types.parameter_values

        out["values"] = capo_sagemaker.types.parameter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    return out
