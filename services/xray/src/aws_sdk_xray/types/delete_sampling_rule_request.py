"""Generated from Smithy shape ``com.amazonaws.xray#DeleteSamplingRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.string


class DeleteSamplingRuleRequest(TypedDict):
    rule_name: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The name of the sampling rule. Specify a rule by either name or ARN, but not both.</p>"""
    rule_arn: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSamplingRuleRequest) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_arn" in value:
        out["RuleARN"] = value["rule_arn"]
    return out


def deserialize_json(data: dict) -> DeleteSamplingRuleRequest:
    out: DeleteSamplingRuleRequest = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "RuleARN" in data:
        out["rule_arn"] = data["RuleARN"]
    return out
