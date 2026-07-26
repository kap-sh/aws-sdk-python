"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.action_condition
    import capo_observabilityadmin.types.label_name_condition


class Condition(TypedDict, closed=True):
    action_condition: NotRequired[
        "capo_observabilityadmin.types.action_condition.ActionCondition"
    ]
    """<p> Matches log records based on the WAF rule action taken (ALLOW, BLOCK, COUNT, etc.). </p>"""
    label_name_condition: NotRequired[
        "capo_observabilityadmin.types.label_name_condition.LabelNameCondition"
    ]
    """<p> Matches log records based on WAF rule labels applied to the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    out: dict = {}
    if "action_condition" in value:
        import capo_observabilityadmin.types.action_condition

        out["ActionCondition"] = (
            capo_observabilityadmin.types.action_condition.serialize_json(
                value["action_condition"]
            )
        )
    if "label_name_condition" in value:
        import capo_observabilityadmin.types.label_name_condition

        out["LabelNameCondition"] = (
            capo_observabilityadmin.types.label_name_condition.serialize_json(
                value["label_name_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "ActionCondition" in data:
        import capo_observabilityadmin.types.action_condition

        out["action_condition"] = (
            capo_observabilityadmin.types.action_condition.deserialize_json(
                data["ActionCondition"]
            )
        )
    if "LabelNameCondition" in data:
        import capo_observabilityadmin.types.label_name_condition

        out["label_name_condition"] = (
            capo_observabilityadmin.types.label_name_condition.deserialize_json(
                data["LabelNameCondition"]
            )
        )
    return out
