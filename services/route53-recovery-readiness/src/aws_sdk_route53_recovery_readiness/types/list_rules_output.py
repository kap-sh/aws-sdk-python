"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string_max64
    import aws_sdk_route53_recovery_readiness.types.__string_max256


class ListRulesOutput(TypedDict, closed=True):
    resource_type: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string_max64.__stringMax64"
    ]
    """<p>The resource type that the readiness rule applies to.</p>"""
    rule_description: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string_max256.__stringMax256"
    ]
    """<p>The description of a readiness rule.</p>"""
    rule_id: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string_max64.__stringMax64"
    ]
    """<p>The ID for the readiness rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesOutput) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "rule_description" in value:
        out["ruleDescription"] = value["rule_description"]
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> ListRulesOutput:
    out: ListRulesOutput = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "ruleDescription" in data:
        out["rule_description"] = data["ruleDescription"]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    return out
