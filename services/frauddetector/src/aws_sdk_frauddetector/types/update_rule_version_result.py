"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateRuleVersionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.rule


class UpdateRuleVersionResult(TypedDict):
    rule: NotRequired["aws_sdk_frauddetector.types.rule.Rule"]
    """<p>The new rule version that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuleVersionResult) -> dict:
    out: dict = {}
    if "rule" in value:
        import aws_sdk_frauddetector.types.rule

        out["rule"] = aws_sdk_frauddetector.types.rule.serialize_aws_json_1_1(
            value["rule"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuleVersionResult:
    out: UpdateRuleVersionResult = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import aws_sdk_frauddetector.types.rule

        out["rule"] = aws_sdk_frauddetector.types.rule.deserialize_aws_json_1_1(
            data["rule"]
        )
    return out
