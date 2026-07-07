"""Generated from Smithy shape ``com.amazonaws.personalize#CategoricalHyperParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.categorical_values
    import aws_sdk_personalize.types.parameter_name


class CategoricalHyperParameterRange(TypedDict, closed=True):
    name: NotRequired["aws_sdk_personalize.types.parameter_name.ParameterName"]
    """<p>The name of the hyperparameter.</p>"""
    values: NotRequired[
        "aws_sdk_personalize.types.categorical_values.CategoricalValues"
    ]
    """<p>A list of the categories for the hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalHyperParameterRange) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "values" in value:
        import aws_sdk_personalize.types.categorical_values

        out["values"] = (
            aws_sdk_personalize.types.categorical_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CategoricalHyperParameterRange:
    out: CategoricalHyperParameterRange = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "values" in data:
        import aws_sdk_personalize.types.categorical_values

        out["values"] = (
            aws_sdk_personalize.types.categorical_values.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    return out
