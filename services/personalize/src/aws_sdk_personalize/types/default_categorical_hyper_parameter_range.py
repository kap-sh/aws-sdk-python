"""Generated from Smithy shape ``com.amazonaws.personalize#DefaultCategoricalHyperParameterRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.categorical_values
    import aws_sdk_personalize.types.parameter_name
    import aws_sdk_personalize.types.tunable


class DefaultCategoricalHyperParameterRange(TypedDict):
    name: NotRequired["aws_sdk_personalize.types.parameter_name.ParameterName"]
    """<p>The name of the hyperparameter.</p>"""
    values: NotRequired[
        "aws_sdk_personalize.types.categorical_values.CategoricalValues"
    ]
    """<p>A list of the categories for the hyperparameter.</p>"""
    is_tunable: "aws_sdk_personalize.types.tunable.Tunable"
    """<p>Whether the hyperparameter is tunable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultCategoricalHyperParameterRange) -> dict:
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
    out["isTunable"] = value.get("is_tunable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultCategoricalHyperParameterRange:
    out: DefaultCategoricalHyperParameterRange = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "values" in data:
        import aws_sdk_personalize.types.categorical_values

        out["values"] = (
            aws_sdk_personalize.types.categorical_values.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    if "isTunable" in data:
        out["is_tunable"] = data["isTunable"]
    else:
        out["is_tunable"] = False
    return out
