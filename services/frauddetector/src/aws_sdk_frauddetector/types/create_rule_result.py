"""Generated from Smithy shape ``com.amazonaws.frauddetector#CreateRuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.rule


class CreateRuleResult(TypedDict, closed=True):
    rule: NotRequired["aws_sdk_frauddetector.types.rule.Rule"]
    """<p>The created rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRuleResult) -> dict:
    out: dict = {}
    if "rule" in value:
        import aws_sdk_frauddetector.types.rule

        out["rule"] = aws_sdk_frauddetector.types.rule.serialize_aws_json_1_1(
            value["rule"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRuleResult:
    out: CreateRuleResult = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import aws_sdk_frauddetector.types.rule

        out["rule"] = aws_sdk_frauddetector.types.rule.deserialize_aws_json_1_1(
            data["rule"]
        )
    return out
