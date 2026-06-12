"""Generated from Smithy shape ``com.amazonaws.sagemaker#CategoricalParameterRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.parameter_key
    import aws_sdk_sagemaker.types.parameter_values


class CategoricalParameterRange(TypedDict):
    name: NotRequired["aws_sdk_sagemaker.types.parameter_key.ParameterKey"]
    """<p>The name of the categorical hyperparameter to tune.</p>"""
    values: NotRequired["aws_sdk_sagemaker.types.parameter_values.ParameterValues"]
    """<p>A list of the categories for the hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameterRange) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import aws_sdk_sagemaker.types.parameter_values

        out["Values"] = aws_sdk_sagemaker.types.parameter_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CategoricalParameterRange:
    out: CategoricalParameterRange = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import aws_sdk_sagemaker.types.parameter_values

        out["values"] = (
            aws_sdk_sagemaker.types.parameter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
