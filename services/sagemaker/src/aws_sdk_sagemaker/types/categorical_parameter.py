"""Generated from Smithy shape ``com.amazonaws.sagemaker#CategoricalParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.categorical_parameter_range_values
    import aws_sdk_sagemaker.types.string64


class CategoricalParameter(TypedDict):
    name: NotRequired["aws_sdk_sagemaker.types.string64.String64"]
    """<p>The Name of the environment variable.</p>"""
    value: NotRequired[
        "aws_sdk_sagemaker.types.categorical_parameter_range_values.CategoricalParameterRangeValues"
    ]
    """<p>The list of values you can pass.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        import aws_sdk_sagemaker.types.categorical_parameter_range_values

        out["Value"] = (
            aws_sdk_sagemaker.types.categorical_parameter_range_values.serialize_aws_json_1_1(
                value["value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CategoricalParameter:
    out: CategoricalParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        import aws_sdk_sagemaker.types.categorical_parameter_range_values

        out["value"] = (
            aws_sdk_sagemaker.types.categorical_parameter_range_values.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    return out
