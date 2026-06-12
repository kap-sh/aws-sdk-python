"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalRulePredicateListDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafRegionalRulePredicateListDetails(TypedDict):
    data_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A unique identifier for a predicate in a rule, such as <code>ByteMatchSetId</code> or <code>IPSetId</code>. </p>"""
    negated: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Specifies if you want WAF to allow, block, or count requests based on the settings in the <code>ByteMatchSet</code>, <code>IPSet</code>, <code>SqlInjectionMatchSet</code>, <code>XssMatchSet</code>, <code>RegexMatchSet</code>, <code>GeoMatchSet</code>, or <code>SizeConstraintSet</code>. </p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of predicate in a rule, such as <code>ByteMatch</code> or <code>IPSet</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalRulePredicateListDetails) -> dict:
    out: dict = {}
    if "data_id" in value:
        out["DataId"] = value["data_id"]
    if "negated" in value:
        out["Negated"] = value["negated"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsWafRegionalRulePredicateListDetails:
    out: AwsWafRegionalRulePredicateListDetails = {}  # type: ignore[typeddict-item]
    if "DataId" in data:
        out["data_id"] = data["DataId"]
    if "Negated" in data:
        out["negated"] = data["Negated"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
