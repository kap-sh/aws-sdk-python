"""Generated from Smithy shape ``com.amazonaws.wafregional#ExcludedRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.resource_id


class ExcludedRule(TypedDict):
    rule_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The unique identifier for the rule to exclude from the rule group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludedRule) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExcludedRule:
    out: ExcludedRule = {}  # type: ignore[typeddict-item]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("ExcludedRule.rule_id required")
    return out
