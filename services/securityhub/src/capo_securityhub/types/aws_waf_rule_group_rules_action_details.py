"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRuleGroupRulesActionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsWafRuleGroupRulesActionDetails(TypedDict, closed=True):
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The action that WAF should take on a web request when it matches the rule's statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRuleGroupRulesActionDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsWafRuleGroupRulesActionDetails:
    out: AwsWafRuleGroupRulesActionDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
