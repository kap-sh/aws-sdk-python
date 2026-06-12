"""Generated from Smithy shape ``com.amazonaws.pinpoint#Condition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.list_of_simple_condition
    import aws_sdk_pinpoint.types.operator


class Condition(TypedDict):
    conditions: NotRequired[
        "aws_sdk_pinpoint.types.list_of_simple_condition.ListOfSimpleCondition"
    ]
    """<p>The conditions to evaluate for the activity.</p>"""
    operator: NotRequired["aws_sdk_pinpoint.types.operator.Operator"]
    """<p>Specifies how to handle multiple conditions for the activity. For example, if you specify two conditions for an activity, whether both or only one of the conditions must be met for the activity to be performed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    out: dict = {}
    if "conditions" in value:
        import aws_sdk_pinpoint.types.list_of_simple_condition

        out["Conditions"] = (
            aws_sdk_pinpoint.types.list_of_simple_condition.serialize_json(
                value["conditions"]
            )
        )
    if "operator" in value:
        import aws_sdk_pinpoint.types.operator

        out["Operator"] = aws_sdk_pinpoint.types.operator.serialize_json(
            value["operator"]
        )
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "Conditions" in data:
        import aws_sdk_pinpoint.types.list_of_simple_condition

        out["conditions"] = (
            aws_sdk_pinpoint.types.list_of_simple_condition.deserialize_json(
                data["Conditions"]
            )
        )
    if "Operator" in data:
        import aws_sdk_pinpoint.types.operator

        out["operator"] = aws_sdk_pinpoint.types.operator.deserialize_json(
            data["Operator"]
        )
    return out
