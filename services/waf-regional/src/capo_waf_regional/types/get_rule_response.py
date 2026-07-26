"""Generated from Smithy shape ``com.amazonaws.wafregional#GetRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.rule


class GetRuleResponse(TypedDict, closed=True):
    rule: NotRequired["capo_waf_regional.types.rule.Rule"]
    """<p>Information about the <a>Rule</a> that you specified in the <code>GetRule</code> request. For more information, see the following topics:</p> <ul> <li> <p> <a>Rule</a>: Contains <code>MetricName</code>, <code>Name</code>, an array of <code>Predicate</code> objects, and <code>RuleId</code> </p> </li> <li> <p> <a>Predicate</a>: Each <code>Predicate</code> object contains <code>DataId</code>, <code>Negated</code>, and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRuleResponse) -> dict:
    out: dict = {}
    if "rule" in value:
        import capo_waf_regional.types.rule

        out["Rule"] = capo_waf_regional.types.rule.serialize_aws_json_1_1(value["rule"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRuleResponse:
    out: GetRuleResponse = {}  # type: ignore[typeddict-item]
    if "Rule" in data:
        import capo_waf_regional.types.rule

        out["rule"] = capo_waf_regional.types.rule.deserialize_aws_json_1_1(
            data["Rule"]
        )
    return out
