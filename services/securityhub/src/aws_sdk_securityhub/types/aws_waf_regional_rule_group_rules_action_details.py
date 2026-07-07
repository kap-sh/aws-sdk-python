"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalRuleGroupRulesActionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafRegionalRuleGroupRulesActionDetails(TypedDict, closed=True):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the <code>ByteMatchSet</code>, <code>IPSet</code>, <code>SqlInjectionMatchSet</code>, <code>XssMatchSet</code>, <code>RegexMatchSet</code>, <code>GeoMatchSet</code>, and <code>SizeConstraintSet</code> objects that you want to add to a rule and, for each object, indicates whether you want to negate the settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalRuleGroupRulesActionDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsWafRegionalRuleGroupRulesActionDetails:
    out: AwsWafRegionalRuleGroupRulesActionDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
