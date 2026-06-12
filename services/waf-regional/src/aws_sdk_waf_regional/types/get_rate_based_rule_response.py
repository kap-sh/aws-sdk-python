"""Generated from Smithy shape ``com.amazonaws.wafregional#GetRateBasedRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.rate_based_rule


class GetRateBasedRuleResponse(TypedDict):
    rule: NotRequired["aws_sdk_waf_regional.types.rate_based_rule.RateBasedRule"]
    """<p>Information about the <a>RateBasedRule</a> that you specified in the <code>GetRateBasedRule</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRateBasedRuleResponse) -> dict:
    out: dict = {}
    if "rule" in value:
        import aws_sdk_waf_regional.types.rate_based_rule

        out["Rule"] = aws_sdk_waf_regional.types.rate_based_rule.serialize_aws_json_1_1(
            value["rule"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRateBasedRuleResponse:
    out: GetRateBasedRuleResponse = {}  # type: ignore[typeddict-item]
    if "Rule" in data:
        import aws_sdk_waf_regional.types.rate_based_rule

        out["rule"] = (
            aws_sdk_waf_regional.types.rate_based_rule.deserialize_aws_json_1_1(
                data["Rule"]
            )
        )
    return out
