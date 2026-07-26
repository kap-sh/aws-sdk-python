"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.accept_rule_behavior


class AcceptRule(TypedDict, closed=True):
    rule: NotRequired["capo_datazone.types.accept_rule_behavior.AcceptRuleBehavior"]
    """<p>Specifies whether you want to accept the top prediction for all targets or none.</p>"""
    threshold: NotRequired["float"]
    """<p>The confidence score that specifies the condition at which a prediction can be accepted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptRule) -> dict:
    out: dict = {}
    if "rule" in value:
        import capo_datazone.types.accept_rule_behavior

        out["rule"] = capo_datazone.types.accept_rule_behavior.serialize_json(
            value["rule"]
        )
    if "threshold" in value:
        out["threshold"] = value["threshold"]
    return out


def deserialize_json(data: dict) -> AcceptRule:
    out: AcceptRule = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import capo_datazone.types.accept_rule_behavior

        out["rule"] = capo_datazone.types.accept_rule_behavior.deserialize_json(
            data["rule"]
        )
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    return out
