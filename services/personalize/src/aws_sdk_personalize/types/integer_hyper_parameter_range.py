"""Generated from Smithy shape ``com.amazonaws.personalize#IntegerHyperParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.integer_max_value
    import aws_sdk_personalize.types.integer_min_value
    import aws_sdk_personalize.types.parameter_name


class IntegerHyperParameterRange(TypedDict, closed=True):
    name: NotRequired["aws_sdk_personalize.types.parameter_name.ParameterName"]
    """<p>The name of the hyperparameter.</p>"""
    min_value: "aws_sdk_personalize.types.integer_min_value.IntegerMinValue"
    """<p>The minimum allowable value for the hyperparameter.</p>"""
    max_value: "aws_sdk_personalize.types.integer_max_value.IntegerMaxValue"
    """<p>The maximum allowable value for the hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegerHyperParameterRange) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["minValue"] = value.get("min_value", 0)
    out["maxValue"] = value.get("max_value", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegerHyperParameterRange:
    out: IntegerHyperParameterRange = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "minValue" in data:
        out["min_value"] = data["minValue"]
    else:
        out["min_value"] = 0
    if "maxValue" in data:
        out["max_value"] = data["maxValue"]
    else:
        out["max_value"] = 0
    return out
