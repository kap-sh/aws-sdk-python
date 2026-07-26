"""Generated from Smithy shape ``com.amazonaws.wafv2#OverrideAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.count_action
    import capo_wafv2.types.none_action


class OverrideAction(TypedDict, closed=True):
    count: NotRequired["capo_wafv2.types.count_action.CountAction"]
    """<p>Override the rule group evaluation result to count only. </p> <note> <p>This option is usually set to none. It does not affect how the rules in the rule group are evaluated. If you want the rules in the rule group to only count matches, do not use this and instead use the rule action override option, with <code>Count</code> action, in your rule group reference statement settings. </p> </note>"""
    none: NotRequired["capo_wafv2.types.none_action.NoneAction"]
    """<p>Don't override the rule group evaluation result. This is the most common setting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverrideAction) -> dict:
    out: dict = {}
    if "count" in value:
        import capo_wafv2.types.count_action

        out["Count"] = capo_wafv2.types.count_action.serialize_aws_json_1_1(
            value["count"]
        )
    if "none" in value:
        import capo_wafv2.types.none_action

        out["None"] = capo_wafv2.types.none_action.serialize_aws_json_1_1(value["none"])
    return out


def deserialize_aws_json_1_1(data: dict) -> OverrideAction:
    out: OverrideAction = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        import capo_wafv2.types.count_action

        out["count"] = capo_wafv2.types.count_action.deserialize_aws_json_1_1(
            data["Count"]
        )
    if "None" in data:
        import capo_wafv2.types.none_action

        out["none"] = capo_wafv2.types.none_action.deserialize_aws_json_1_1(
            data["None"]
        )
    return out
