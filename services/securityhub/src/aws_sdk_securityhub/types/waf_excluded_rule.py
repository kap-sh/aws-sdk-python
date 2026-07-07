"""Generated from Smithy shape ``com.amazonaws.securityhub#WafExcludedRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class WafExcludedRule(TypedDict, closed=True):
    rule_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier for the rule to exclude from the rule group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WafExcludedRule) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> WafExcludedRule:
    out: WafExcludedRule = {}  # type: ignore[typeddict-item]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    return out
