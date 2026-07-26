"""Generated from Smithy shape ``com.amazonaws.datazone#RejectRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.reject_rule_behavior


class RejectRule(TypedDict, closed=True):
    rule: NotRequired["capo_datazone.types.reject_rule_behavior.RejectRuleBehavior"]
    """<p>Specifies whether you want to reject the top prediction for all targets or none.</p>"""
    threshold: NotRequired["float"]
    """<p>The confidence score that specifies the condition at which a prediction can be rejected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectRule) -> dict:
    out: dict = {}
    if "rule" in value:
        import capo_datazone.types.reject_rule_behavior

        out["rule"] = capo_datazone.types.reject_rule_behavior.serialize_json(
            value["rule"]
        )
    if "threshold" in value:
        out["threshold"] = value["threshold"]
    return out


def deserialize_json(data: dict) -> RejectRule:
    out: RejectRule = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import capo_datazone.types.reject_rule_behavior

        out["rule"] = capo_datazone.types.reject_rule_behavior.deserialize_json(
            data["rule"]
        )
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    return out
