"""Generated from Smithy shape ``com.amazonaws.wafv2#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.action_condition
    import capo_wafv2.types.label_name_condition


class Condition(TypedDict, closed=True):
    action_condition: NotRequired["capo_wafv2.types.action_condition.ActionCondition"]
    """<p>A single action condition. This is the action setting that a log record must contain in order to meet the condition.</p>"""
    label_name_condition: NotRequired[
        "capo_wafv2.types.label_name_condition.LabelNameCondition"
    ]
    """<p>A single label name condition. This is the fully qualified label name that a log record must contain in order to meet the condition. Fully qualified labels have a prefix, optional namespaces, and label name. The prefix identifies the rule group or web ACL context of the rule that added the label. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Condition) -> dict:
    out: dict = {}
    if "action_condition" in value:
        import capo_wafv2.types.action_condition

        out["ActionCondition"] = (
            capo_wafv2.types.action_condition.serialize_aws_json_1_1(
                value["action_condition"]
            )
        )
    if "label_name_condition" in value:
        import capo_wafv2.types.label_name_condition

        out["LabelNameCondition"] = (
            capo_wafv2.types.label_name_condition.serialize_aws_json_1_1(
                value["label_name_condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "ActionCondition" in data:
        import capo_wafv2.types.action_condition

        out["action_condition"] = (
            capo_wafv2.types.action_condition.deserialize_aws_json_1_1(
                data["ActionCondition"]
            )
        )
    if "LabelNameCondition" in data:
        import capo_wafv2.types.label_name_condition

        out["label_name_condition"] = (
            capo_wafv2.types.label_name_condition.deserialize_aws_json_1_1(
                data["LabelNameCondition"]
            )
        )
    return out
