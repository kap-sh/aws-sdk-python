"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateRuleVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.rule


class UpdateRuleVersionResult(TypedDict, closed=True):
    rule: NotRequired["capo_frauddetector.types.rule.Rule"]
    """<p>The new rule version that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuleVersionResult) -> dict:
    out: dict = {}
    if "rule" in value:
        import capo_frauddetector.types.rule

        out["rule"] = capo_frauddetector.types.rule.serialize_aws_json_1_1(
            value["rule"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuleVersionResult:
    out: UpdateRuleVersionResult = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import capo_frauddetector.types.rule

        out["rule"] = capo_frauddetector.types.rule.deserialize_aws_json_1_1(
            data["rule"]
        )
    return out
