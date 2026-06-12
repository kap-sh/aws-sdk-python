"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_datazone.types.accept_rule_behavior

class AcceptRule(TypedDict):
    rule: NotRequired["aws_sdk_datazone.types.accept_rule_behavior.AcceptRuleBehavior"]
    """<p>Specifies whether you want to accept the top prediction for all targets or none.</p>"""
    threshold: NotRequired["float"]
    """<p>The confidence score that specifies the condition at which a prediction can be accepted.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AcceptRule) -> dict:
    out: dict = {}
    if "rule" in value:
        import aws_sdk_datazone.types.accept_rule_behavior
        out["rule"] = aws_sdk_datazone.types.accept_rule_behavior.serialize_json(value["rule"])
    if "threshold" in value:
        out["threshold"] = value["threshold"]
    return out


def deserialize_json(data: dict) -> AcceptRule:
    out: AcceptRule = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import aws_sdk_datazone.types.accept_rule_behavior
        out["rule"] = aws_sdk_datazone.types.accept_rule_behavior.deserialize_json(data["rule"])
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    return out