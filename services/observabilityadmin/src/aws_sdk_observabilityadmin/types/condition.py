"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Condition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.action_condition
    import aws_sdk_observabilityadmin.types.label_name_condition


class Condition(TypedDict):
    action_condition: NotRequired[
        "aws_sdk_observabilityadmin.types.action_condition.ActionCondition"
    ]
    """<p> Matches log records based on the WAF rule action taken (ALLOW, BLOCK, COUNT, etc.). </p>"""
    label_name_condition: NotRequired[
        "aws_sdk_observabilityadmin.types.label_name_condition.LabelNameCondition"
    ]
    """<p> Matches log records based on WAF rule labels applied to the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    out: dict = {}
    if "action_condition" in value:
        import aws_sdk_observabilityadmin.types.action_condition

        out["ActionCondition"] = (
            aws_sdk_observabilityadmin.types.action_condition.serialize_json(
                value["action_condition"]
            )
        )
    if "label_name_condition" in value:
        import aws_sdk_observabilityadmin.types.label_name_condition

        out["LabelNameCondition"] = (
            aws_sdk_observabilityadmin.types.label_name_condition.serialize_json(
                value["label_name_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "ActionCondition" in data:
        import aws_sdk_observabilityadmin.types.action_condition

        out["action_condition"] = (
            aws_sdk_observabilityadmin.types.action_condition.deserialize_json(
                data["ActionCondition"]
            )
        )
    if "LabelNameCondition" in data:
        import aws_sdk_observabilityadmin.types.label_name_condition

        out["label_name_condition"] = (
            aws_sdk_observabilityadmin.types.label_name_condition.deserialize_json(
                data["LabelNameCondition"]
            )
        )
    return out
