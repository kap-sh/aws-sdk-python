"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.parameter_key
    import aws_sdk_sagemaker.types.parameter_value


class AutoParameter(TypedDict, closed=True):
    name: NotRequired["aws_sdk_sagemaker.types.parameter_key.ParameterKey"]
    """<p>The name of the hyperparameter to optimize using Autotune.</p>"""
    value_hint: NotRequired["aws_sdk_sagemaker.types.parameter_value.ParameterValue"]
    """<p>An example value of the hyperparameter to optimize using Autotune.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value_hint" in value:
        out["ValueHint"] = value["value_hint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoParameter:
    out: AutoParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ValueHint" in data:
        out["value_hint"] = data["ValueHint"]
    return out
