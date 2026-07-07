"""Generated from Smithy shape ``com.amazonaws.glue#ConditionExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.databrew_condition
    import aws_sdk_glue.types.databrew_condition_value
    import aws_sdk_glue.types.target_column


class ConditionExpression(TypedDict, closed=True):
    condition: "aws_sdk_glue.types.databrew_condition.DatabrewCondition"
    """<p>The condition of the condition expression.</p>"""
    value: NotRequired[
        "aws_sdk_glue.types.databrew_condition_value.DatabrewConditionValue"
    ]
    """<p>The value of the condition expression.</p>"""
    target_column: "aws_sdk_glue.types.target_column.TargetColumn"
    """<p>The target column of the condition expressions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionExpression) -> dict:
    out: dict = {}
    out["Condition"] = value["condition"]
    if "value" in value:
        out["Value"] = value["value"]
    out["TargetColumn"] = value["target_column"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConditionExpression:
    out: ConditionExpression = {}  # type: ignore[typeddict-item]
    if "Condition" in data:
        out["condition"] = data["Condition"]
    else:
        raise DeserializationError("ConditionExpression.condition required")
    if "Value" in data:
        out["value"] = data["Value"]
    if "TargetColumn" in data:
        out["target_column"] = data["TargetColumn"]
    else:
        raise DeserializationError("ConditionExpression.target_column required")
    return out
