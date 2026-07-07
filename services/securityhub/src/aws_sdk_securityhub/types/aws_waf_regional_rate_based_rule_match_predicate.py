"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalRateBasedRuleMatchPredicate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafRegionalRateBasedRuleMatchPredicate(TypedDict, closed=True):
    data_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier for the predicate.</p>"""
    negated: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>If set to <code>true</code>, then the rule actions are performed on requests that match the predicate settings.</p> <p>If set to <code>false</code>, then the rule actions are performed on all requests except those that match the predicate settings.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of predicate. Valid values are as follows:</p> <ul> <li> <p> <code>ByteMatch</code> </p> </li> <li> <p> <code>GeoMatch</code> </p> </li> <li> <p> <code>IPMatch</code> </p> </li> <li> <p> <code>RegexMatch</code> </p> </li> <li> <p> <code>SizeConstraint</code> </p> </li> <li> <p> <code>SqlInjectionMatch</code> </p> </li> <li> <p> <code>XssMatch</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalRateBasedRuleMatchPredicate) -> dict:
    out: dict = {}
    if "data_id" in value:
        out["DataId"] = value["data_id"]
    if "negated" in value:
        out["Negated"] = value["negated"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsWafRegionalRateBasedRuleMatchPredicate:
    out: AwsWafRegionalRateBasedRuleMatchPredicate = {}  # type: ignore[typeddict-item]
    if "DataId" in data:
        out["data_id"] = data["DataId"]
    if "Negated" in data:
        out["negated"] = data["Negated"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
