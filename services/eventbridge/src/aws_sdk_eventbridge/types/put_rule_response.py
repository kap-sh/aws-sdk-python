"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.rule_arn


class PutRuleResponse(TypedDict, closed=True):
    rule_arn: NotRequired["aws_sdk_eventbridge.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRuleResponse) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRuleResponse:
    out: PutRuleResponse = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    return out
