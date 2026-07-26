"""Generated from Smithy shape ``com.amazonaws.waf#ListRateBasedRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.next_marker
    import capo_waf.types.rule_summaries


class ListRateBasedRulesResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_waf.types.next_marker.NextMarker"]
    """<p>If you have more <code>Rules</code> than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>Rules</code>, submit another <code>ListRateBasedRules</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    rules: NotRequired["capo_waf.types.rule_summaries.RuleSummaries"]
    """<p>An array of <a>RuleSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRateBasedRulesResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "rules" in value:
        import capo_waf.types.rule_summaries

        out["Rules"] = capo_waf.types.rule_summaries.serialize_aws_json_1_1(
            value["rules"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRateBasedRulesResponse:
    out: ListRateBasedRulesResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Rules" in data:
        import capo_waf.types.rule_summaries

        out["rules"] = capo_waf.types.rule_summaries.deserialize_aws_json_1_1(
            data["Rules"]
        )
    return out
